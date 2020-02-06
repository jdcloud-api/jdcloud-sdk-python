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


class DescribeBackendsRequest(JDCloudRequest):
    """
    查询后端服务列表
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeBackendsRequest, self).__init__(
            '/regions/{regionId}/backends/', 'GET', header, version)
        self.parameters = parameters


class DescribeBackendsParameters(object):

    def __init__(self, regionId, ):
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
        :param filters: (Optional) backendIds - 后端服务Id列表，支持多个
backendNames - 后端服务名称列表，支持多个
loadBalancerId - 负载均衡器Id，支持单个
agId - 高可用组Id，支持单个
loadBalancerType - 负载均衡类型，取值为：alb、nlb、dnlb，默认alb，支持单个
protocol - 后端服务的协议【alb】支持Http、Tcp，【nlb&dnlb】支持Tcp，默认查询所有，支持单个

        """
        self.filters = filters

