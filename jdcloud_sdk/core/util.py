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

import sys
import base64
import re
if sys.version_info.major == 2:
    from urllib import quote # 遵循RFC 2396
    from urllib import quote_plus # /会进行编码
    from urllib import unquote
    from urllib import unquote_plus # +会解码为空格
    from urlparse import urlparse
elif sys.version_info.major == 3:
    from urllib.parse import quote # 遵循RFC 2396
    from urllib.parse import quote_plus # /会进行编码
    from urllib.parse import unquote
    from urllib.parse import unquote_plus # +会解码为空格
    from urllib.parse import urlparse


# base64 encode
def base64encode(value):
    if sys.version_info.major == 2:
        return base64.b64encode(value)
    elif sys.version_info.major == 3:
        encoded_value = base64.b64encode(value.encode('utf-8'))
        return str(encoded_value, 'utf-8')


# byte to string
def byte_to_str(string):
    if sys.version_info.major == 2:
        return string
    elif sys.version_info.major == 3:
        return str(string, 'utf-8')


# parse url
def parse_url(url):
    scheme, netloc, path, params, query, fragment = urlparse(url)
    pattern = (r'^'
               r'((?P<user>.+?)(:(?P<password>.*?))?@)?'
               r'(?P<host>.*?)'
               r'(:(?P<port>\d+?))?'
               r'$')
    regex = re.compile(pattern)
    match = regex.match(netloc)
    group_dict = match.groupdict() if match is not None else None
    if path is None:
        path = '/'
    if query is None:
        query = ''
    group_dict['path'] = path
    group_dict['schema'] = scheme
    group_dict['query'] = query
    group_dict['fragment'] = fragment
    return group_dict