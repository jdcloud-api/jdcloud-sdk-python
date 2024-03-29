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


class ServiceBillAdjust(object):

    def __init__(self, appCode, serviceCode, billDate, region, billingType, adjustFee, ):
        """
        :param appCode:  产品线
        :param serviceCode:  产品
        :param billDate:  调整月份,格式：yyyyMM
        :param region:  地域
        :param billingType:  计费类型 1按配置 2按用量 3包年包月 4按次
        :param adjustFee:  调整金额
        """

        self.appCode = appCode
        self.serviceCode = serviceCode
        self.billDate = billDate
        self.region = region
        self.billingType = billingType
        self.adjustFee = adjustFee
