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


class QueryAdminStatisticsRequest(JDCloudRequest):
    """
    设备基本数据统计，包括设备数，激活数，在线数
    """

    def __init__(self, parameters, header=None, version="v2"):
        super(QueryAdminStatisticsRequest, self).__init__(
            '/regions/{regionId}/instances/{instanceId}/device:queryAdminStatistics', 'GET', header, version)
        self.parameters = parameters


class QueryAdminStatisticsParameters(object):

    def __init__(self, instanceId, regionId, ):
        """
        :param instanceId: 设备归属的实例ID
        :param regionId: 设备归属的实例所在区域
        """

        self.instanceId = instanceId
        self.regionId = regionId
        self.productKey = None
        self.parentId = None
        self.deviceCollectorType = None

    def setProductKey(self, productKey):
        """
        :param productKey: (Optional) 过滤条件，产品Key
        """
        self.productKey = productKey

    def setParentId(self, parentId):
        """
        :param parentId: (Optional) 针对parentId下的子设备进行统计
        """
        self.parentId = parentId

    def setDeviceCollectorType(self, deviceCollectorType):
        """
        :param deviceCollectorType: (Optional) 采集器类型
        """
        self.deviceCollectorType = deviceCollectorType

