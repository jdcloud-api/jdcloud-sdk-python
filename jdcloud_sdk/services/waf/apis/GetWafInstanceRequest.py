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


class GetWafInstanceRequest(JDCloudRequest):
    """
    获取实例ID及相关信息列表
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(GetWafInstanceRequest, self).__init__(
            '/regions/{regionId}/user:getWafInstance', 'GET', header, version)
        self.parameters = parameters


class GetWafInstanceParameters(object):

    def __init__(self, regionId, ):
        """
        :param regionId: 实例所属的地域ID
        """

        self.regionId = regionId
        self.idc = None
        self.pageNumber = None
        self.pageSize = None
        self.filters = None
        self.sourceIds = None

    def setIdc(self, idc):
        """
        :param idc: (Optional) 所属地区， 模糊匹配
        """
        self.idc = idc

    def setPageNumber(self, pageNumber):
        """
        :param pageNumber: (Optional) 页码
        """
        self.pageNumber = pageNumber

    def setPageSize(self, pageSize):
        """
        :param pageSize: (Optional) 分页大小
        """
        self.pageSize = pageSize

    def setFilters(self, filters):
        """
        :param filters: (Optional) wafInstanceId - 实例id
        """
        self.filters = filters

    def setSourceIds(self, sourceIds):
        """
        :param sourceIds: (Optional) 资源id 多个时，以逗号,分隔。
        """
        self.sourceIds = sourceIds
