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


class ClientException(Exception):
    def __init__(self, message):
        super(ClientException, self).__init__()
        self.message = message

    def __str__(self):
        return self.message


class ServerException(Exception):
    def __init__(self, status, code, message):
        super(ServerException, self).__init__()
        self.code = code
        self.message = message
        self.status = status

    def __str__(self):
        return str(self.code) + "::" + self.status+"::" + self.message
