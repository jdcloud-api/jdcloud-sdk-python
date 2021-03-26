# coding=utf8

# Copyright 2018 JDCLOUD.COM
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import datetime
import time
import hashlib
import hmac
import re
import uuid
from . import const
from .logger import INFO
from .util import quote, unquote_plus, parse_url


class Signer(object):
    ignored_headers = ['authorization', 'user-agent']

    def __init__(self, logger):
        self.__logger = logger

    def sign(self, method, service, region, uri, headers, data, credential, security_token):
        uri_dict = self.__url_path_to_dict(uri)
        host = uri_dict['host']
        port = uri_dict['port']
        path = uri_dict['path']
        query = uri_dict['query']

        if port and port not in ['80', '443']:
            full_host = host + ':' + port
        else:
            full_host = host
        return self.signV3(method, service, region, full_host, path, query, headers, data, credential, security_token)

    def signV3(self, method, service, region, host, path, query, headers, data, credential, security_token):
        canonical_host = self.__build_canonical_host(host)
        now = self.__now()
        nonce = str(uuid.uuid4())
        jdcloud_date = now.strftime('%Y%m%dT%H%M%SZ')
        if const.JDCLOUD_DATE in headers:
            jdcloud_date = headers[const.JDCLOUD_DATE]
        if const.JDCLOUD_NONCE in headers:
            nonce = headers[const.JDCLOUD_NONCE]
        date_str = jdcloud_date[:8]

        canonical_querystring = self.__normalize_query_string(query)
        canonical_headers, signed_headers = self.__build_canonical_headers(headers, security_token, canonical_host)

        payload_hash = self.__sha256_hash(data)

        canonical_request = (method + '\n' +
                             self.__build_canonical_uri(path) + '\n' +
                             canonical_querystring + '\n' +
                             canonical_headers + '\n' +
                             signed_headers + '\n' +
                             payload_hash)

        algorithm = const.JDCLOUD3_ALGORITHM
        credential_scope = (date_str + '/' +
                            region + '/' +
                            service + '/' +
                            const.JDCLOUD3_REQUEST)
        string_to_sign = (algorithm + '\n' +
                          jdcloud_date + '\n' +
                          credential_scope + '\n' +
                          self.__sha256_hash(canonical_request))

        self.__logger.log(INFO, '---canonical_request---\n' + canonical_request)
        self.__logger.log(INFO, '----string_to_sign---\n' + string_to_sign)

        signing_key = self.__get_signature_key(credential.secret_key, date_str, region, service)
        encoded = string_to_sign.encode('utf-8')
        signature = hmac.new(signing_key, encoded, hashlib.sha256).hexdigest()

        authorization_header = (
                algorithm + ' ' +
                'Credential=' + credential.access_key + '/' + credential_scope + ', ' +
                'SignedHeaders=' + signed_headers + ', ' +
                'Signature=' + signature
        )

        headers.update({
            const.JDCLOUD_AUTH: authorization_header,
            const.JDCLOUD_DATE: jdcloud_date,
            const.JDCLOUD_CONTENT_SHA256: payload_hash,
            const.JDCLOUD3_ALGORITHM: const.JDCLOUD3_ALGORITHM,
            const.JDCLOUD_NONCE: nonce
        })

        if security_token:
            headers.update({const.JDCLOUD_SECURITY_TOKEN: security_token})

    def __build_canonical_host(self, full_host):
        if full_host.lower().find('http://') == 0:
            full_host = full_host[7:]
        elif full_host.lower().find('https://') == 0:
            full_host = full_host[8:]
        return full_host

    def __normalize_query_string(self, query):
        params = []
        if isinstance(query, str):
            for s in query.split('&'):
                if len(s) <= 0:
                    continue
                list = []
                for val in s.split('='):
                    list.append(self.__urlencode(self.__urldecode(val)))
                params.append(list)
        elif isinstance(query, dict):
            for key in query.keys():
                list = []
                list.append(self.__urlencode(self.__urldecode(key)))
                list.append(self.__urlencode(self.__urldecode(query[key])))
                params.append(list)

        normalized = ''
        for p in sorted(params):
            if p[0] == '':
                continue
            elif len(p) == 2:
                normalized += '%s=%s&' % (p[0], p[1])
            elif len(p) > 2:
                normalized += '%3D'.join(p[1:]) + '&'
        if normalized.endswith('&'):
            normalized = normalized[:normalized.__len__()-1]
        return normalized

    def __now(self):
        return datetime.datetime.utcfromtimestamp(time.time())

    def __url_path_to_dict(self, path):
        """http://stackoverflow.com/a/17892757/142207"""

        # pattern = (r'^'
        #            r'((?P<schema>.+?)://)?'
        #            r'((?P<user>.+?)(:(?P<password>.*?))?@)?'
        #            r'(?P<host>.*?)'
        #            r'(:(?P<port>\d+?))?'
        #            r'(?P<path>/.*?)?'
        #            r'(\?(?P<query>.*?))?'
        #            r'$')
        # regex = re.compile(pattern)
        # match = regex.match(path)
        # group_dict = match.groupdict() if match is not None else None
        #
        # if group_dict['path'] is None:
        #     group_dict['path'] = '/'
        #
        # if group_dict['query'] is None:
        #     group_dict['query'] = ''
        # return group_dict
        return parse_url(path)

    def __sign(self, key, msg):
        return hmac.new(key, msg.encode('utf-8'), hashlib.sha256).digest()

    def __get_signature_key(self, key, date_stamp, region_name, service_name):
        k_date = self.__sign((const.JDCLOUD3 + key).encode('utf-8'), date_stamp)
        k_region = self.__sign(k_date, region_name)
        k_service = self.__sign(k_region, service_name)
        k_signing = self.__sign(k_service, const.JDCLOUD3_REQUEST)
        return k_signing

    def __sha256_hash(self, val):
        return hashlib.sha256(val.encode('utf-8')).hexdigest()

    def __build_canonical_uri(self, path):
        reg = re.compile('/+')
        decoded_path = reg.sub('/', self.__urldecode(path))
        if decoded_path == '':
            return '/'
        encoded_path = self.__urlencode_ignore_slashes(decoded_path)
        if encoded_path.startswith('/'):
            return encoded_path
        return '/' + encoded_path

    def __urlencode(self, value):
        return quote(value, '~')

    def __urlencode_ignore_slashes(self, value):
        return quote(value, '/~')

    def __urldecode(self, value):
        return unquote_plus(value)

    def __build_canonical_headers(self, req_headers, security_token, full_host):
        headers = ['host']  # add host header first
        signed_values = {}

        for key in req_headers.keys():
            value = req_headers[key]

            lower_key = key.lower()
            if lower_key in Signer.ignored_headers:
                continue

            headers.append(lower_key)
            signed_values[lower_key] = value

        headers.sort()
        signed_headers = ';'.join(headers)

        canonical_values = []
        for key in headers:
            if key == 'host':
                canonical_values.append('host:' + full_host.strip())
            else:
                # canonical_values.append(key + ':' + )
                header_value = signed_values[key]
                if isinstance(header_value, str):
                    canonical_values.append(key + ':' + header_value.strip())
                elif isinstance(header_value, list):
                    arr = []
                    for val in header_value:
                        arr.append(val.strip())
                    canonical_values.append(key + ':' + ','.join(arr))


        canonical_headers = '\n'.join(canonical_values) + '\n'

        return canonical_headers, signed_headers
