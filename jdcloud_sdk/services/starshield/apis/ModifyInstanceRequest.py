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


class ModifyInstanceRequest(JDCloudRequest):
    """
    升级套餐实例
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(ModifyInstanceRequest, self).__init__(
            '/regions/{regionId}/instance/{instanceId}', 'PUT', header, version)
        self.parameters = parameters


class ModifyInstanceParameters(object):

    def __init__(self,regionId, instanceId, ):
        """
        :param regionId: 地域ID
        :param instanceId: 实例ID
        """

        self.regionId = regionId
        self.instanceId = instanceId
        self.packType = None
        self.zonePackNum = None
        self.returnUrl = None
        self.buyScenario = None

    def setPackType(self, packType):
        """
        :param packType: (Optional) 套餐类型
        """
        self.packType = packType

    def setZonePackNum(self, zonePackNum):
        """
        :param zonePackNum: (Optional) 域名增量包数量
        """
        self.zonePackNum = zonePackNum

    def setReturnUrl(self, returnUrl):
        """
        :param returnUrl: (Optional) 支付成功后返回到该路径
        """
        self.returnUrl = returnUrl

    def setBuyScenario(self, buyScenario):
        """
        :param buyScenario: (Optional) 购买上下文JSON字符串
        """
        self.buyScenario = buyScenario

