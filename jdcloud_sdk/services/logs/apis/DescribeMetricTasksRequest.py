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


class DescribeMetricTasksRequest(JDCloudRequest):
    """
    查询监控任务列表，返回该主题下的所有监控任务信息。
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeMetricTasksRequest, self).__init__(
            '/regions/{regionId}/logsets/{logsetUID}/logtopics/{logtopicUID}/metrictasks', 'GET', header, version)
        self.parameters = parameters


class DescribeMetricTasksParameters(object):

    def __init__(self,regionId, logsetUID, logtopicUID, ):
        """
        :param regionId: 地域 Id
        :param logsetUID: 日志集 UID
        :param logtopicUID: 日志主题 UID
        """

        self.regionId = regionId
        self.logsetUID = logsetUID
        self.logtopicUID = logtopicUID
        self.pageNumber = None
        self.pageSize = None

    def setPageNumber(self, pageNumber):
        """
        :param pageNumber: (Optional) 当前所在页，默认为1
in: query
        """
        self.pageNumber = pageNumber

    def setPageSize(self, pageSize):
        """
        :param pageSize: (Optional) 页面大小，默认为20；取值范围[1, 100]
in: query
        """
        self.pageSize = pageSize

