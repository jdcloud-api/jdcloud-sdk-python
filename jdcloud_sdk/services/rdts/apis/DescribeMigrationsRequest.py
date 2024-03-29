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


class DescribeMigrationsRequest(JDCloudRequest):
    """
    迁移任务列表，可分页、可排序、可搜索、可过滤
    """

    def __init__(self, parameters, header=None, version="v2"):
        super(DescribeMigrationsRequest, self).__init__(
            '/regions/{regionId}/instance', 'GET', header, version)
        self.parameters = parameters


class DescribeMigrationsParameters(object):

    def __init__(self, regionId,):
        """
        :param regionId: 迁移任务所在区域的Region ID。华北-北京(cn-north-1)，华东-上海(cn-east-2)，华南-广州(cn-south-1)
        """

        self.regionId = regionId
        self.pageNumber = None
        self.pageSize = None
        self.filters = None
        self.sorts = None

    def setPageNumber(self, pageNumber):
        """
        :param pageNumber: (Optional) 页码：取值范围[1,∞)，默认为1
        """
        self.pageNumber = pageNumber

    def setPageSize(self, pageSize):
        """
        :param pageSize: (Optional) 分页大小：取值范围[10,100]，默认为10
        """
        self.pageSize = pageSize

    def setFilters(self, filters):
        """
        :param filters: (Optional) 过滤条件：
- instanceIds：迁移任务ID，精确匹配，可选择多个
- migrationName：迁移任务名称，模糊匹配
- migrationStatuses：迁移任务状态，精确匹配，可选择多个（具体可参考迁移任务详情中的迁移状态）

        """
        self.filters = filters

    def setSorts(self, sorts):
        """
        :param sorts: (Optional) 排序属性：
- createdTime：按创建时间排序(asc表示按时间正序，desc表示按时间倒序)

        """
        self.sorts = sorts

