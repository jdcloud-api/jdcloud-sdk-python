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
#
# NOTE: This class is auto generated by the jdcloud code generator program.


class Credentials(object):

    def __init__(self, accessKey=None, secretKey=None, sessionToken=None, expiration=None):
        """
        :param accessKey: (Optional) 临时accessKey
        :param secretKey: (Optional) 临时secretKey
        :param sessionToken: (Optional) 临时安全令牌
        :param expiration: (Optional) 失效时间，格式：yyyy-MM-dd HH:mm:ss(eg 2019-01-01 00:00:00)
        """

        self.accessKey = accessKey
        self.secretKey = secretKey
        self.sessionToken = sessionToken
        self.expiration = expiration
