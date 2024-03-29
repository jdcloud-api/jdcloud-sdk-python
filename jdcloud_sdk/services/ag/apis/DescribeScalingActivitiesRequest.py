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


class DescribeScalingActivitiesRequest(JDCloudRequest):
    """
    使用过滤条件查询一个或多个弹性伸缩活动
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeScalingActivitiesRequest, self).__init__(
            '/regions/{regionId}/autoScaling/{agId}:describeScalingActivities', 'GET', header, version)
        self.parameters = parameters


class DescribeScalingActivitiesParameters(object):

    def __init__(self,regionId, agId, ):
        """
        :param regionId: 地域
        :param agId: 高可用组 ID
        """

        self.regionId = regionId
        self.agId = agId
        self.pageNumber = None
        self.pageSize = None
        self.filters = None
        self.sorts = None

    def setPageNumber(self, pageNumber):
        """
        :param pageNumber: (Optional) 页码；默认为1
        """
        self.pageNumber = pageNumber

    def setPageSize(self, pageSize):
        """
        :param pageSize: (Optional) 分页大小；默认为20；取值范围[10, 100]
        """
        self.pageSize = pageSize

    def setFilters(self, filters):
        """
        :param filters: (Optional) status - 状态，包括成功：SUCCESS,拒绝：REJECTED,失败：FAILED,执行中：RUNNING,部分成功：WARN，精确匹配
beginTime - 开始时间，精确匹配，查询大于等于这个时间的记录
endTime - 结束时间，精确匹配，查询小于等于这个时间的记录
以上每个filter项仅支持单个值查询,如果传多个值仅取第一个值

        """
        self.filters = filters

    def setSorts(self, sorts):
        """
        :param sorts: (Optional) 排序条件列表，目前只支持单个排序条件，不支持多个排序条件，默认按照 `startTime` 降序排序
支持使用以下关键字进行排序
- `startTime`: 活动开始时间

        """
        self.sorts = sorts

