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


class SaveMultiEvidenceRequest(JDCloudRequest):
    """
    多证据链存证接口
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(SaveMultiEvidenceRequest, self).__init__(
            '/evidence:evidenceMultisave', 'POST', header, version)
        self.parameters = parameters


class SaveMultiEvidenceParameters(object):

    def __init__(self,businessId, file, ):
        """
        :param businessId: 业务流水号
        :param file: 存证数据json字符串的Base64
        """

        self.businessId = businessId
        self.file = file
        self.businessCode = None
        self.lender = None
        self.messageId = None
        self.evidenceType = None
        self.messageDate = None

    def setBusinessCode(self, businessCode):
        """
        :param businessCode: (Optional) 证据链代码
        """
        self.businessCode = businessCode

    def setLender(self, lender):
        """
        :param lender: (Optional) 资方信息（借钱传：ZY；票据传 PJ_SHOUXIN--授信,PJ_JIEKUAN--借款）
        """
        self.lender = lender

    def setMessageId(self, messageId):
        """
        :param messageId: (Optional) 请求流水号
        """
        self.messageId = messageId

    def setEvidenceType(self, evidenceType):
        """
        :param evidenceType: (Optional) 业务类型（JIEQIAN–借钱；PIAOJU--票据）
        """
        self.evidenceType = evidenceType

    def setMessageDate(self, messageDate):
        """
        :param messageDate: (Optional) 请求时间
        """
        self.messageDate = messageDate

