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


class DescribeInstanceListRequest(JDCloudRequest):
    """
    获取数据库审计实例列表
pageNumber: 页码
pageSize: 每页数量
nameFilter: 按名称查询
filters: 按instanceId 查询，只支持eq，单个instanceId匹配

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeInstanceListRequest, self).__init__(
            '/regions/{regionId}/instances', 'GET', header, version)
        self.parameters = parameters


class DescribeInstanceListParameters(object):

    def __init__(self, regionId, ):
        """
        :param regionId: 地域 Id
        """

        self.regionId = regionId
        self.pageNumber = None
        self.pageSize = None
        self.nameFilter = None
        self.filters = None

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

    def setNameFilter(self, nameFilter):
        """
        :param nameFilter: (Optional) 列表过滤条件：数据库审计名称
        """
        self.nameFilter = nameFilter

    def setFilters(self, filters):
        """
        :param filters: (Optional) 按instanceId 过滤
        """
        self.filters = filters
