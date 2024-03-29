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


class ExchangeInstanceDnsRequest(JDCloudRequest):
    """
    交换两个实例的域名，包括内网域名和外网域名。如果一个实例有外网域名，一个没有，则不允许交换。<br>- 仅支持SQL Server
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(ExchangeInstanceDnsRequest, self).__init__(
            '/regions/{regionId}/instances/{instanceId}:exchangeInstanceDns', 'POST', header, version)
        self.parameters = parameters


class ExchangeInstanceDnsParameters(object):

    def __init__(self,regionId, instanceId, targetInstanceId):
        """
        :param regionId: 地域代码，取值范围参见[《各地域及可用区对照表》](../Enum-Definitions/Regions-AZ.md)
        :param instanceId: RDS 实例ID，唯一标识一个RDS实例
        :param targetInstanceId: 要交换的实例ID
        """

        self.regionId = regionId
        self.instanceId = instanceId
        self.targetInstanceId = targetInstanceId

