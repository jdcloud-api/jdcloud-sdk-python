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


class DescribeAlarmsRequest(JDCloudRequest):
    """
    查询报警规则列表
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeAlarmsRequest, self).__init__(
            '/alarms', 'GET', header, version)
        self.parameters = parameters


class DescribeAlarmsParameters(object):

    def __init__(self,):
        """
        """

        self.pageNumber = None
        self.pageSize = None
        self.resourceType = None
        self.resourceId = None
        self.idc = None
        self.status = None
        self.filters = None

    def setPageNumber(self, pageNumber):
        """
        :param pageNumber: (Optional) 页码, 默认为1
        """
        self.pageNumber = pageNumber

    def setPageSize(self, pageSize):
        """
        :param pageSize: (Optional) 分页大小，默认为20
        """
        self.pageSize = pageSize

    def setResourceType(self, resourceType):
        """
        :param resourceType: (Optional) 资源类型 bandwidth:带宽
        """
        self.resourceType = resourceType

    def setResourceId(self, resourceId):
        """
        :param resourceId: (Optional) 资源ID，指定resourceId时须指定resourceType
        """
        self.resourceId = resourceId

    def setIdc(self, idc):
        """
        :param idc: (Optional) 机房英文标识
        """
        self.idc = idc

    def setStatus(self, status):
        """
        :param status: (Optional) 规则状态 disabled:禁用 enabled:启用
        """
        self.status = status

    def setFilters(self, filters):
        """
        :param filters: (Optional) alarmId - 规则实施ID，精确匹配，支持多个

        """
        self.filters = filters

