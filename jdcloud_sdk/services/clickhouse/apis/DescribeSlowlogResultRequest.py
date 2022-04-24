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


class DescribeSlowlogResultRequest(JDCloudRequest):
    """
    查询 Clickhouse audit列表信息
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeSlowlogResultRequest, self).__init__(
            '/regions/{regionId}/instances/{instanceId}/slowlog:describeSlowlogResult', 'GET', header, version)
        self.parameters = parameters


class DescribeSlowlogResultParameters(object):

    def __init__(self, regionId,instanceId,):
        """
        :param regionId: 地域代码
        :param instanceId: 实例ID
        """

        self.regionId = regionId
        self.instanceId = instanceId
        self.pageNumber = None
        self.pageSize = None
        self.startTime = None
        self.endTime = None
        self.segmentName = None
        self.queryTime = None
        self.filters = None

    def setPageNumber(self, pageNumber):
        """
        :param pageNumber: (Optional) 显示数据的页码，默认为1，取值范围：[-1,∞)。pageNumber为-1时，返回所有数据页码；超过总页数时，显示最后一页;
        """
        self.pageNumber = pageNumber

    def setPageSize(self, pageSize):
        """
        :param pageSize: (Optional) 每页显示的数据条数，默认为10，取值范围：[10,100]，用于查询列表的接口
        """
        self.pageSize = pageSize

    def setStartTime(self, startTime):
        """
        :param startTime: (Optional) 开始时间
        """
        self.startTime = startTime

    def setEndTime(self, endTime):
        """
        :param endTime: (Optional) 结束时间
        """
        self.endTime = endTime

    def setSegmentName(self, segmentName):
        """
        :param segmentName: (Optional) 节点名称
        """
        self.segmentName = segmentName

    def setQueryTime(self, queryTime):
        """
        :param queryTime: (Optional) 查询时间
        """
        self.queryTime = queryTime

    def setFilters(self, filters):
        """
        :param filters: (Optional) 
        """
        self.filters = filters
