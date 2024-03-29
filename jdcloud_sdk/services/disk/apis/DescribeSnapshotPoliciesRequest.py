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


class DescribeSnapshotPoliciesRequest(JDCloudRequest):
    """
    查询快照策略
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeSnapshotPoliciesRequest, self).__init__(
            '/regions/{regionId}/snapshotPolicies:describe', 'POST', header, version)
        self.parameters = parameters


class DescribeSnapshotPoliciesParameters(object):

    def __init__(self,regionId, ):
        """
        :param regionId: 地域ID
        """

        self.regionId = regionId
        self.name = None
        self.policyId = None
        self.status = None
        self.order = None
        self.pageNumber = None
        self.pageSize = None

    def setName(self, name):
        """
        :param name: (Optional) 策略名称,默认为空
        """
        self.name = name

    def setPolicyId(self, policyId):
        """
        :param policyId: (Optional) 策略ID,默认为空
        """
        self.policyId = policyId

    def setStatus(self, status):
        """
        :param status: (Optional) 策略状态。1: 启用 2：禁用
        """
        self.status = status

    def setOrder(self, order):
        """
        :param order: (Optional) 排序字段，只支持create_time和update_time字段
        """
        self.order = order

    def setPageNumber(self, pageNumber):
        """
        :param pageNumber: (Optional) 页码, 默认为1, 取值范围：[1,∞)
        """
        self.pageNumber = pageNumber

    def setPageSize(self, pageSize):
        """
        :param pageSize: (Optional) 分页大小，默认为20，取值范围：[10,100]
        """
        self.pageSize = pageSize

