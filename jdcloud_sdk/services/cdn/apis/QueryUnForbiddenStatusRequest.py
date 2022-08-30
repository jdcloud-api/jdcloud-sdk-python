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


class QueryUnForbiddenStatusRequest(JDCloudRequest):
    """
    查询解封状态
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(QueryUnForbiddenStatusRequest, self).__init__(
            '/unForbiddenStatus', 'GET', header, version)
        self.parameters = parameters


class QueryUnForbiddenStatusParameters(object):

    def __init__(self,):
        """
        """

        self.domain = None
        self.url = None
        self.taskId = None
        self.pageNumber = None
        self.pageSize = None

    def setDomain(self, domain):
        """
        :param domain: (Optional) 根据域名进行匹配
        """
        self.domain = domain

    def setUrl(self, url):
        """
        :param url: (Optional) 根据url进行匹配
        """
        self.url = url

    def setTaskId(self, taskId):
        """
        :param taskId: (Optional) 解封的任务id
        """
        self.taskId = taskId

    def setPageNumber(self, pageNumber):
        """
        :param pageNumber: (Optional) pageNumber,默认值1
        """
        self.pageNumber = pageNumber

    def setPageSize(self, pageSize):
        """
        :param pageSize: (Optional) pageSize,最大值50,默认值10
        """
        self.pageSize = pageSize

