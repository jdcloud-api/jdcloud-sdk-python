# coding=utf8

# Copyright 2018-2025 JDCLOUD.COM
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http:#www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import abc
import re
import json


class ParameterBuilder(object):

    @abc.abstractmethod
    def build_url(self, request, scheme, endpoint):
        pass

    @abc.abstractmethod
    def build_body(self, request):
        pass

    def _build_req_params(self, parameters):
        if parameters is None:
            return {}

        pairs = {}
        for key in parameters.__dict__.keys():
            value = parameters.__dict__[key]
            if isinstance(value, list) or value is None:
                continue
            pairs.update({key: value})
        return pairs

    # remove path params
    def _build_query_params(self, parameters, url):
        result = ''
        result_dict = self._build_params(parameters.__dict__, url, '', [])
        if len(result_dict) != 0:
            result += '?'

        return result + '&'.join(result_dict)

    def _build_params(self, param_dict, url, prefix, result_list):
        for key in param_dict:
            value = param_dict[key]

            if url.find("{"+key+"}") != -1: continue
            if value is None: continue

            if isinstance(value, list):
                i = 1
                for item in value:
                    sub_prefix = "%s.%d." % (key, i)
                    if isinstance(item, str) or isinstance(item, int):
                        result_list.append("%s%s.%d=%s" % (prefix, key, i, item))
                    elif isinstance(item, dict):
                        result_list = self._build_params(item, url, sub_prefix, result_list)
                    else:
                        result_list = self._build_params(item.__dict__, url, sub_prefix, result_list)
                    i += 1
            else:
                result_list.append("%s%s=%s" % (prefix, key, value))

        return result_list

    def _replace_url_with_value(self, url, params_obj):
        if url.count('{') == 0:
            return url

        params = self._build_req_params(params_obj)
        pattern = r'{([a-zA-Z0-9-_]+)}'
        matches = re.findall(pattern, url)
        for match in matches:
            url = url.replace('{' + match + '}', self.__get_path_param_value(params, match))
        return url

    def __get_path_param_value(self, params, field):
        return params.get(field, '')


# GET/DELETE
class WithoutBodyBuilder(ParameterBuilder):

    def build_url(self, request, scheme, endpoint):
        query_params = self._build_query_params(request.parameters, request.url)
        url = self._replace_url_with_value(request.url, request.parameters)
        return '%s://%s/%s%s%s' % (scheme, endpoint, request.version, url, query_params)

    def build_body(self, request):
        return ''


# PUT/POST/PATCH
class WithBodyBuilder(ParameterBuilder):

    def build_url(self, request, scheme, endpoint):
        url = self._replace_url_with_value(request.url, request.parameters)
        return '%s://%s/%s%s' % (scheme, endpoint, request.version, url)

    def build_body(self, request):
        return json.dumps(request.parameters, cls=ParametersEncoder)


class ParametersEncoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__
