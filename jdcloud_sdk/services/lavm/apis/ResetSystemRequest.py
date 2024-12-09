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


class ResetSystemRequest(JDCloudRequest):
    """
    轻量应用云主机重置系统。

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(ResetSystemRequest, self).__init__(
            '/regions/{regionId}/instances/{instanceId}:resetSystem', 'POST', header, version)
        self.parameters = parameters


class ResetSystemParameters(object):

    def __init__(self,instanceId, regionId, ):
        """
        :param instanceId: 轻量应用云主机的实例ID

        :param regionId: 地域

        """

        self.instanceId = instanceId
        self.regionId = regionId
        self.imageId = None
        self.keyNames = None
        self.password = None
        self.passwordAuth = None

    def setImageId(self, imageId):
        """
        :param imageId: (Optional) 目标镜像ID

        """
        self.imageId = imageId

    def setKeyNames(self, keyNames):
        """
        :param keyNames: (Optional) 密钥对名称。仅Linux系统下该参数生效，当前仅支持输入单个密钥。

        """
        self.keyNames = keyNames

    def setPassword(self, password):
        """
        :param password: (Optional) 密码

        """
        self.password = password

    def setPasswordAuth(self, passwordAuth):
        """
        :param passwordAuth: (Optional) 密码授权，若存在密匙，则根据此参数决定是否使用密码，若没有密匙，此参数无效，会强制使用密码。
若不使用密码，且密匙对解绑后，用户需重置密码，方可使用密码登录。
此参数在windows系统中必须为yes。

        """
        self.passwordAuth = passwordAuth
