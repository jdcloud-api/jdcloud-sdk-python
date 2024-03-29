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


class DescribeEdgeIpProvidersRequest(JDCloudRequest):
    """
    查询边缘公网IP可用线路列表
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeEdgeIpProvidersRequest, self).__init__(
            '/regions/{regionId}/edgeIpProviders/', 'GET', header, version)
        self.parameters = parameters


class DescribeEdgeIpProvidersParameters(object):

    def __init__(self,regionId, ):
        """
        :param regionId: Region ID
        """

        self.regionId = regionId
        self.pageNumber = None
        self.pageSize = None
        self.filters = None

    def setPageNumber(self, pageNumber):
        """
        :param pageNumber: (Optional) 页码, 默认为1, 取值范围：[1,∞), 页码超过总页数时, 显示最后一页
        """
        self.pageNumber = pageNumber

    def setPageSize(self, pageSize):
        """
        :param pageSize: (Optional) 分页大小，默认为20，取值范围：[10,100]
        """
        self.pageSize = pageSize

    def setFilters(self, filters):
        """
        :param filters: (Optional) providers - 边缘公网IP的线路，命名规则：[线路接入区].[资源关联范围].[服务类型]，示例如cn-n1-jinan1.ez.bgp，支持多个
pointsOfAccess - 边缘公网IP的线路接入区，提供线路接入区具体位置信息，支持多个
associationScope	- 边缘公网IP的资源关联范围，取值ez(边缘可用区)和az(中心可用区，暂不支持),支持单个
serviceTypes - 边缘公网IP的服务类型，取值：bgp(动态)，unicom(联通)，telecom(电信)，mobile(移动)，支持多个
azs - 边缘公网IP的可用区，分为全可用区（暂不支持）和边缘可用区ID(同线路接入区])，示例如cn-n1-sqxx1，支持多个

        """
        self.filters = filters

