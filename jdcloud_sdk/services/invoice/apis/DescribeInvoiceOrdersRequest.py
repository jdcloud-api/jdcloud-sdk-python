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


class DescribeInvoiceOrdersRequest(JDCloudRequest):
    """
    开票单据列表
    """

    def __init__(self, parameters, header=None, version="v2"):
        super(DescribeInvoiceOrdersRequest, self).__init__(
            '/regions/{regionId}/invoiceorder:list', 'POST', header, version)
        self.parameters = parameters


class DescribeInvoiceOrdersParameters(object):

    def __init__(self,regionId, ):
        """
        :param regionId: 地域编码，参考OpenAPI公共说明
        """

        self.regionId = regionId
        self.searchStartTime = None
        self.searchEndTime = None
        self.pageNumber = None
        self.pageSize = None
        self.receiptType = None
        self.payType = None

    def setSearchStartTime(self, searchStartTime):
        """
        :param searchStartTime: (Optional) 开始时间
        """
        self.searchStartTime = searchStartTime

    def setSearchEndTime(self, searchEndTime):
        """
        :param searchEndTime: (Optional) 结束时间
        """
        self.searchEndTime = searchEndTime

    def setPageNumber(self, pageNumber):
        """
        :param pageNumber: (Optional) 页码
        """
        self.pageNumber = pageNumber

    def setPageSize(self, pageSize):
        """
        :param pageSize: (Optional) 页大小
        """
        self.pageSize = pageSize

    def setReceiptType(self, receiptType):
        """
        :param receiptType: (Optional) 单据类型[订单-order，账单-bill 月结算单-month]
        """
        self.receiptType = receiptType

    def setPayType(self, payType):
        """
        :param payType: (Optional) 交易(支付)类型 1-代付 2-自付
        """
        self.payType = payType
