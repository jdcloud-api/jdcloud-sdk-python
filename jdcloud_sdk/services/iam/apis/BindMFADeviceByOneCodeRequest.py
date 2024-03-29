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


class BindMFADeviceByOneCodeRequest(JDCloudRequest):
    """
    绑定虚拟MFA设备（一组动态密码）
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(BindMFADeviceByOneCodeRequest, self).__init__(
            '/virtualMFADevice:bindByOneCode', 'POST', header, version)
        self.parameters = parameters


class BindMFADeviceByOneCodeParameters(object):

    def __init__(self,authenticationCode):
        """
        :param authenticationCode: 一组动态密码
        """

        self.boundAccount = None
        self.authenticationCode = authenticationCode

    def setBoundAccount(self, boundAccount):
        """
        :param boundAccount: (Optional) 被绑定的账号（目前支持：默认不填的情况表示给自己绑定，填写子用户名表示主账号给子用户绑定)
        """
        self.boundAccount = boundAccount

