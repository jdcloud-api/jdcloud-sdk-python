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


class BillSummaryTrend(object):

    def __init__(self, billDate=None, billFee=None, discountFee=None, actualFee=None, cashPayFee=None, payCouponFee=None, freeCouponFee=None):
        """
        :param billDate: (Optional) 账期，yyyy-MM
        :param billFee: (Optional) 原价
        :param discountFee: (Optional) 优惠金额
        :param actualFee: (Optional) 应付费用
        :param cashPayFee: (Optional) 现金
        :param payCouponFee: (Optional) 付费代金券
        :param freeCouponFee: (Optional) 免费代金券
        """

        self.billDate = billDate
        self.billFee = billFee
        self.discountFee = discountFee
        self.actualFee = actualFee
        self.cashPayFee = cashPayFee
        self.payCouponFee = payCouponFee
        self.freeCouponFee = freeCouponFee
