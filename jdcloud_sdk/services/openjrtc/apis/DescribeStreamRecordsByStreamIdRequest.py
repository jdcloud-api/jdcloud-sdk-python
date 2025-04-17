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


class DescribeStreamRecordsByStreamIdRequest(JDCloudRequest):
    """
    根据流ID查询推流历史记录
允许通过条件过滤查询，支持的过滤字段如下：
           - startTime[eq] 用户推流开始时间-UTC时间  startTime,endTime同时指定时生效
           - endTime[eq]   用户推流结束时间-UTC时间  startTime,endTime同时指定时生效

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeStreamRecordsByStreamIdRequest, self).__init__(
            '/describeStreamRecordsByStreamId/{appId}', 'GET', header, version)
        self.parameters = parameters


class DescribeStreamRecordsByStreamIdParameters(object):

    def __init__(self,appId, streamId, ):
        """
        :param appId: 应用ID
        :param streamId: 流ID
        """

        self.appId = appId
        self.pageNumber = None
        self.pageSize = None
        self.streamId = streamId
        self.filters = None

    def setPageNumber(self, pageNumber):
        """
        :param pageNumber: (Optional) 页码；默认值为 1
        """
        self.pageNumber = pageNumber

    def setPageSize(self, pageSize):
        """
        :param pageSize: (Optional) 分页大小；默认值为 10；取值范围 [10, 100]
        """
        self.pageSize = pageSize

    def setFilters(self, filters):
        """
        :param filters: (Optional) 传参字段描述:
- startTime[eq] 用户推流开始时间-UTC时间  startTime,endTime同时指定时生效
- endTime[eq]   用户推流结束时间-UTC时间  startTime,endTime同时指定时生效

        """
        self.filters = filters

