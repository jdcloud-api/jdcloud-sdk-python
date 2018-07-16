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

import json


class JDCloudResponse(object):

    def __init__(self):
        self.request_id = None
        self.error = None
        self.result = None

    def __getitem__(self, key):
        return getattr(self, key)

    def fill_value(self, resp):
        return json.loads(resp, object_hook=self.load_hook)

    def load_hook(self, resp_dict):
        request_id = resp_dict.get('requestId')
        if request_id:
            self.request_id = request_id

            error = resp_dict.get('error')
            if error:
                self.error = ErrorResponse(error.get('status'), error.get('code'), error.get('message'))

            result = resp_dict.get('result')
            if result:
                self.result = resp_dict['result']
            return self
        return resp_dict


class ErrorResponse(object):

    def __init__(self, status, code, message):
        self.status = status
        self.code = code
        self.message = message
