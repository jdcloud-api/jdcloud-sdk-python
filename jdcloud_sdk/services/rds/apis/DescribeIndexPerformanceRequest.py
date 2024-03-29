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


class DescribeIndexPerformanceRequest(JDCloudRequest):
    """
    根据用户定义的查询条件，获取索引性能的统计信息，并提供缺失索引及索引创建建议。用户可以根据这些信息查找与索引相关的性能瓶颈，并进行优化。<br>- 仅支持SQL Server
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeIndexPerformanceRequest, self).__init__(
            '/regions/{regionId}/instances/{instanceId}/performance:describeIndexPerformance', 'GET', header, version)
        self.parameters = parameters


class DescribeIndexPerformanceParameters(object):

    def __init__(self,regionId, instanceId, queryType, ):
        """
        :param regionId: 地域代码，取值范围参见[《各地域及可用区对照表》](../Enum-Definitions/Regions-AZ.md)
        :param instanceId: RDS 实例ID，唯一标识一个RDS实例
        :param queryType: 查询类型，不同的查询类型按照相应的字段从高到低返回结果。<br>支持如下类型：<br>Missing：缺失索引<br>Size：索引大小，单位KB<br>Updates：索引更新次数<br>Scans：表扫描次数<br>Used：最少使用<br>
        """

        self.regionId = regionId
        self.instanceId = instanceId
        self.queryType = queryType
        self.db = None
        self.pageNumber = None
        self.pageSize = None

    def setDb(self, db):
        """
        :param db: (Optional) 需要查询的数据库名，多个数据库名之间用英文逗号分隔，默认所有数据库
        """
        self.db = db

    def setPageNumber(self, pageNumber):
        """
        :param pageNumber: (Optional) 显示数据的页码，默认为1，取值范围：[-1,∞]。pageNumber为-1时，返回所有数据页码；
        """
        self.pageNumber = pageNumber

    def setPageSize(self, pageSize):
        """
        :param pageSize: (Optional) 每页显示的数据条数，默认为50，取值范围：[1,100]，只能为10的倍数，用于查询列表的接口
        """
        self.pageSize = pageSize

