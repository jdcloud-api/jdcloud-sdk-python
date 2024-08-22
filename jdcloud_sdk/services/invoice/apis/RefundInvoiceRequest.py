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


class RefundInvoiceRequest(JDCloudRequest):
    """
    退票
    """

    def __init__(self, parameters, header=None, version="v2"):
        super(RefundInvoiceRequest, self).__init__(
            '/regions/{regionId}/invoice/{invoiceNumber}:refund', 'POST', header, version)
        self.parameters = parameters


class RefundInvoiceParameters(object):

    def __init__(self,regionId, invoiceNumber, ):
        """
        :param regionId: 地域编码，参考OpenAPI公共说明
        :param invoiceNumber: 发票申请单号
        """

        self.regionId = regionId
        self.invoiceNumber = invoiceNumber
        self.refundReason = None
        self.remark = None
        self.logisticsCompany = None
        self.logisticsOrderNumber = None
        self.mediumType = None

    def setRefundReason(self, refundReason):
        """
        :param refundReason: (Optional) 退票原因
        """
        self.refundReason = refundReason

    def setRemark(self, remark):
        """
        :param remark: (Optional) 备注信息
        """
        self.remark = remark

    def setLogisticsCompany(self, logisticsCompany):
        """
        :param logisticsCompany: (Optional) 物流公司
        """
        self.logisticsCompany = logisticsCompany

    def setLogisticsOrderNumber(self, logisticsOrderNumber):
        """
        :param logisticsOrderNumber: (Optional) 物流单号
        """
        self.logisticsOrderNumber = logisticsOrderNumber

    def setMediumType(self, mediumType):
        """
        :param mediumType: (Optional) [纸质-paper，电子-electronic]
        """
        self.mediumType = mediumType

