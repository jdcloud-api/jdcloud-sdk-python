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


class DescribeNodesRequest(JDCloudRequest):
    """
    获取某个实例下的所有节点的主要性能信息，如CPU，内存，存储空间等。 该性能信息从云监控获取，为上一个监控周期的数据。
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeNodesRequest, self).__init__(
            '/regions/{regionId}/instances/{instanceId}/nodes', 'GET', header, version)
        self.parameters = parameters


class DescribeNodesParameters(object):

    def __init__(self,regionId, instanceId, ):
        """
        :param regionId: 地域代码
        :param instanceId: 实例ID
        """

        self.regionId = regionId
        self.instanceId = instanceId
        self.pageNumber = None
        self.pageSize = None
        self.sorts = None
        self.filters = None

    def setPageNumber(self, pageNumber):
        """
        :param pageNumber: (Optional) 显示数据的页码，默认为1，取值范围：[-1,∞)。pageNumber为-1时，返回所有数据页码；超过总页数时，显示最后一页;
        """
        self.pageNumber = pageNumber

    def setPageSize(self, pageSize):
        """
        :param pageSize: (Optional) 每页显示的数据条数，默认为50，取值范围：[50,100]，用于查询列表的接口
        """
        self.pageSize = pageSize

    def setSorts(self, sorts):
        """
        :param sorts: (Optional) cpuUtil - CPU使用率
memeryUtil - 内存使用率
diskUsage - 磁盘使用率

        """
        self.sorts = sorts

    def setFilters(self, filters):
        """
        :param filters: (Optional) nodeType, 支持operator选项：eq,ne
nodeStatus, 支持operator选项：eq ne

        """
        self.filters = filters

