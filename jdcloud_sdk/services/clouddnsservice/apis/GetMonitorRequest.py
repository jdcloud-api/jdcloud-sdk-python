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


class GetMonitorRequest(JDCloudRequest):
    """
    查看主域名的监控项的配置以及状态
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(GetMonitorRequest, self).__init__(
            '/regions/{regionId}/domain/{domainId}/monitor', 'GET', header, version)
        self.parameters = parameters


class GetMonitorParameters(object):

    def __init__(self, regionId, domainId, ):
        """
        :param regionId: 实例所属的地域ID
        :param domainId: 域名ID，请使用getDomains接口获取。
        """

        self.regionId = regionId
        self.domainId = domainId
        self.pageIndex = None
        self.pageSize = None
        self.searchValue = None

    def setPageIndex(self, pageIndex):
        """
        :param pageIndex: (Optional) 当前页数，起始值为1，默认为1
        """
        self.pageIndex = pageIndex

    def setPageSize(self, pageSize):
        """
        :param pageSize: (Optional) 分页查询时设置的每页行数
        """
        self.pageSize = pageSize

    def setSearchValue(self, searchValue):
        """
        :param searchValue: (Optional) 查询的值
        """
        self.searchValue = searchValue

