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


class CreateInstanceByTimeRequest(JDCloudRequest):
    """
    根据源实例备份创建一个新实例，并通过追加日志的方式，将新实例的数据恢复到跟源实例指定时间点的数据状态一样。<br>例如根据实例A在“2018-06-18 23:00:00”时间点创建一个实例B，就是新建一个实例B，该实例B的数据跟实例A在“2018-06-18 23:00:00”这个时间点的数据完全一致。<br>对于SQL Server，主备切换后30分钟内，不支持按时间点恢复/创建，例如在10:05分用户进行了主备切换，那么10:05 ~ 10:35这个时间段不能进行按时间点恢复/创建。
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(CreateInstanceByTimeRequest, self).__init__(
            '/regions/{regionId}/instances/{instanceId}:createInstanceByTime', 'POST', header, version)
        self.parameters = parameters


class CreateInstanceByTimeParameters(object):

    def __init__(self,regionId, instanceId, restoreTime, instanceSpec):
        """
        :param regionId: 地域代码，取值范围参见[《各地域及可用区对照表》](../Enum-Definitions/Regions-AZ.md)
        :param instanceId: RDS 实例ID，唯一标识一个RDS实例
        :param restoreTime: 根据源实例的哪个时间点创建新实例
        :param instanceSpec: 新建实例规格
        """

        self.regionId = regionId
        self.instanceId = instanceId
        self.restoreTime = restoreTime
        self.instanceSpec = instanceSpec

