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


class ModifyNetworkInterfaceRequest(JDCloudRequest):
    """
    修改弹性网卡信息
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(ModifyNetworkInterfaceRequest, self).__init__(
            '/regions/{regionId}/networkInterfaces/{networkInterfaceId}', 'PATCH', header, version)
        self.parameters = parameters


class ModifyNetworkInterfaceParameters(object):

    def __init__(self,regionId, networkInterfaceId, ):
        """
        :param regionId: Region ID
        :param networkInterfaceId: networkInterface ID
        """

        self.regionId = regionId
        self.networkInterfaceId = networkInterfaceId
        self.networkInterfaceName = None
        self.description = None
        self.securityGroups = None

    def setNetworkInterfaceName(self, networkInterfaceName):
        """
        :param networkInterfaceName: (Optional) 弹性网卡名称,只允许输入中文、数字、大小写字母、英文下划线“_”及中划线“-”，不允许为空且不超过32字符
        """
        self.networkInterfaceName = networkInterfaceName

    def setDescription(self, description):
        """
        :param description: (Optional) 描述,允许输入UTF-8编码下的全部字符，不超过256字符
        """
        self.description = description

    def setSecurityGroups(self, securityGroups):
        """
        :param securityGroups: (Optional) 以覆盖原有安全组的方式更新的安全组。如果更新安全组ID列表，最多5个安全组
        """
        self.securityGroups = securityGroups

