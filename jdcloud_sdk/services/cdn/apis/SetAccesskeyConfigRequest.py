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

from jdcloud_sdk.core.jdcloudrequest import JDCloudRequest


class SetAccesskeyConfigRequest(JDCloudRequest):
    """
    设置url鉴权
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(SetAccesskeyConfigRequest, self).__init__(
            '/domain/{domain}/accesskeyConfig', 'POST', header, version)
        self.parameters = parameters


class SetAccesskeyConfigParameters(object):

    def __init__(self,domain, ):
        """
        :param domain: 用户域名
        """

        self.domain = domain
        self.accesskeyType = None
        self.accesskeyKey = None
        self.accesskeyKeep = None

    def setAccesskeyType(self, accesskeyType):
        """
        :param accesskeyType: (Optional) 鉴权类型，0表示无鉴权，1表示参数鉴权，2表示路径鉴权
        """
        self.accesskeyType = accesskeyType

    def setAccesskeyKey(self, accesskeyKey):
        """
        :param accesskeyKey: (Optional) 密码，长度为8到32
        """
        self.accesskeyKey = accesskeyKey

    def setAccesskeyKeep(self, accesskeyKeep):
        """
        :param accesskeyKeep: (Optional) 是否是回源鉴权 0表示是 1表示否
        """
        self.accesskeyKeep = accesskeyKeep

