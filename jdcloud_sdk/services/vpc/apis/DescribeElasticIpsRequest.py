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


class DescribeElasticIpsRequest(JDCloudRequest):
    """
    查询弹性公网IP列表
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeElasticIpsRequest, self).__init__(
            '/regions/{regionId}/elasticIps/', 'GET', header, version)
        self.parameters = parameters


class DescribeElasticIpsParameters(object):

    def __init__(self,regionId, ):
        """
        :param regionId: Region ID
        """

        self.regionId = regionId
        self.pageNumber = None
        self.pageSize = None
        self.filters = None
        self.tags = None
        self.resourceGroupIds = None

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
        :param filters: (Optional) elasticIpIds - elasticip id数组条件，支持多个
elasticIpAddress - eip的IP地址，支持单个
chargeStatus	- eip的费用支付状态,normal(正常状态) or overdue(预付费已到期) or arrear(欠费状态)，支持单个
ipType - eip类型，取值：all(所有类型)、standard(标准弹性IP)、edge(边缘弹性IP)，默认standard，支持单个
azs - eip可用区，支持多个
bandwidthPackageId - 共享带宽包ID，支持单个
status - IP是否被绑定，取值：ASSOCIATED（被绑定）、NOT_ASSOCIATED（未被绑定）、ALL（全部）。支持单个

        """
        self.filters = filters

    def setTags(self, tags):
        """
        :param tags: (Optional) Tag筛选条件
        """
        self.tags = tags

    def setResourceGroupIds(self, resourceGroupIds):
        """
        :param resourceGroupIds: (Optional) 资源组筛选条件
        """
        self.resourceGroupIds = resourceGroupIds

