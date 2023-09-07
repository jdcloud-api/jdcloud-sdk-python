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


class DescribeParameterModifyRecordsRequest(JDCloudRequest):
    """
    查看参数的修改历史<br>- 仅支持MySQL，Percona，MariaDB，PostgreSQL
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeParameterModifyRecordsRequest, self).__init__(
            '/regions/{regionId}/parameterGroups/{parameterGroupId}/records', 'GET', header, version)
        self.parameters = parameters


class DescribeParameterModifyRecordsParameters(object):

    def __init__(self,regionId, parameterGroupId, ):
        """
        :param regionId: Region ID
        :param parameterGroupId: Parameter Group ID
        """

        self.regionId = regionId
        self.parameterGroupId = parameterGroupId
        self.pageNumber = None
        self.pageSize = None
        self.startTime = None
        self.endTime = None

    def setPageNumber(self, pageNumber):
        """
        :param pageNumber: (Optional) 显示数据的页码，默认为1，取值范围：[-1,∞)。pageNumber为-1时，返回所有数据页码；
        """
        self.pageNumber = pageNumber

    def setPageSize(self, pageSize):
        """
        :param pageSize: (Optional) 每页显示的数据条数，默认为10，取值范围：[10,100]，且为10的整数倍
        """
        self.pageSize = pageSize

    def setStartTime(self, startTime):
        """
        :param startTime: (Optional) 查询开始时间，格式为：YYYY-MM-DD HH:mm:ss
        """
        self.startTime = startTime

    def setEndTime(self, endTime):
        """
        :param endTime: (Optional) 查询结束时间，格式为：YYYY-MM-DD HH:mm:ss
        """
        self.endTime = endTime

