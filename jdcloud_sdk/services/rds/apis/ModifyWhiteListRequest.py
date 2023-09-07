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


class ModifyWhiteListRequest(JDCloudRequest):
    """
    修改允许访问实例的IP白名单。白名单是允许访问当前实例的IP/IP段列表，缺省情况下，白名单对本VPC开放。如果用户开启了外网访问的功能，还需要对外网的IP配置白名单。
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(ModifyWhiteListRequest, self).__init__(
            '/regions/{regionId}/instances/{instanceId}/whiteList', 'PUT', header, version)
        self.parameters = parameters


class ModifyWhiteListParameters(object):

    def __init__(self,regionId, instanceId, ips):
        """
        :param regionId: 地域代码，取值范围参见[《各地域及可用区对照表》](../Enum-Definitions/Regions-AZ.md)
        :param instanceId: RDS 实例ID，唯一标识一个RDS实例
        :param ips: IP或IP段，不同的IP/IP段之间用英文逗号分隔，例如0.0.0.0/0,192.168.0.10
        """

        self.regionId = regionId
        self.instanceId = instanceId
        self.whiteListName = None
        self.ips = ips

    def setWhiteListName(self, whiteListName):
        """
        :param whiteListName: (Optional) 白名单名称，默认Default
        """
        self.whiteListName = whiteListName

