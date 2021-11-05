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


class DescribeActionLogsRequest(JDCloudRequest):
    """
    查询操作日志

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeActionLogsRequest, self).__init__(
            '/regions/{regionId}/actionLogs', 'GET', header, version)
        self.parameters = parameters


class DescribeActionLogsParameters(object):

    def __init__(self, regionId, start, end, ):
        """
        :param regionId: 地域ID
        :param start: 起始时间，格式：UTC时间例如2017-11-10T23:00:00Z
        :param end: 结束时间，格式：UTC时间例如2017-11-10T23:00:00Z
        """

        self.regionId = regionId
        self.pageSize = None
        self.pageNumber = None
        self.start = start
        self.end = end
        self.keyWord = None
        self.success = None
        self.actionType = None

    def setPageSize(self, pageSize):
        """
        :param pageSize: (Optional) 页容量，默认10，取值范围(1 - 100)
        """
        self.pageSize = pageSize

    def setPageNumber(self, pageNumber):
        """
        :param pageNumber: (Optional) 页序号，默认值1，不能小于1
        """
        self.pageNumber = pageNumber

    def setKeyWord(self, keyWord):
        """
        :param keyWord: (Optional) 日志模糊匹配的关键词
        """
        self.keyWord = keyWord

    def setSuccess(self, success):
        """
        :param success: (Optional) 操作结果 false->失败 true->成功
        """
        self.success = success

    def setActionType(self, actionType):
        """
        :param actionType: (Optional) 日志类型，支持的类型有：CREATE_ZONE、DELETE_ZONE、LOCK_ZONE、CREATE_RR、MODIFY_RR、DELETE_RR、SET_RR_STATUS、RETRY_RECURSE_ZONE
        """
        self.actionType = actionType

