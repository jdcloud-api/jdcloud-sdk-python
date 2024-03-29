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


class UnbindMFADeviceRequest(JDCloudRequest):
    """
    解绑虚拟MFA设备
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(UnbindMFADeviceRequest, self).__init__(
            '/virtualMFADevice:unbind', 'DELETE', header, version)
        self.parameters = parameters


class UnbindMFADeviceParameters(object):

    def __init__(self,):
        """
        """

        self.unboundAccount = None

    def setUnboundAccount(self, unboundAccount):
        """
        :param unboundAccount: (Optional) 被解绑的账号（目前支持：默认不填的情况表示给自己解绑，填写子用户名表示为子用户解绑)
        """
        self.unboundAccount = unboundAccount

