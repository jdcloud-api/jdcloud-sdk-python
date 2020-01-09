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


class DescribeBackupsRequest(JDCloudRequest):
    """
    查询缓存Redis实例的备份任务（文件）列表，可分页、可指定起止时间或备份任务ID
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeBackupsRequest, self).__init__(
            '/regions/{regionId}/cacheInstance/{cacheInstanceId}/backup', 'GET', header, version)
        self.parameters = parameters


class DescribeBackupsParameters(object):

    def __init__(self, regionId, cacheInstanceId, ):
        """
        :param regionId: 缓存Redis实例所在区域的Region ID。目前有华北-北京、华南-广州、华东-上海三个区域，Region ID分别为cn-north-1、cn-south-1、cn-east-2
        :param cacheInstanceId: 缓存Redis实例ID，是访问实例的唯一标识
        """

        self.regionId = regionId
        self.cacheInstanceId = cacheInstanceId
        self.pageNumber = None
        self.pageSize = None
        self.startTime = None
        self.endTime = None
        self.baseId = None

    def setPageNumber(self, pageNumber):
        """
        :param pageNumber: (Optional) 页码；默认为1
        """
        self.pageNumber = pageNumber

    def setPageSize(self, pageSize):
        """
        :param pageSize: (Optional) 分页大小；默认为10；取值范围[10, 100]
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

    def setBaseId(self, baseId):
        """
        :param baseId: (Optional) 备份任务ID
        """
        self.baseId = baseId

