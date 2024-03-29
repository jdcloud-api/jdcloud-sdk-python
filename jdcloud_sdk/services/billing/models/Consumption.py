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


class Consumption(object):

    def __init__(self, billingType=None, payType=None, actualFee=None, cashPayFee=None, balancePayFee=None, cashCouponPayFee=None, arrearFee=None, billFee2=None, discountFee=None, groupTagValue=None):
        """
        :param billingType: (Optional) 计费类型
        :param payType: (Optional) 支付类型
        :param actualFee: (Optional) 优惠后金额
        :param cashPayFee: (Optional) 现金支付
        :param balancePayFee: (Optional) 余额支付
        :param cashCouponPayFee: (Optional) 优惠券支付金额
        :param arrearFee: (Optional) 欠费金额
        :param billFee2: (Optional) 原价
        :param discountFee: (Optional) 优惠金额
        :param groupTagValue: (Optional) 分组显示值
        """

        self.billingType = billingType
        self.payType = payType
        self.actualFee = actualFee
        self.cashPayFee = cashPayFee
        self.balancePayFee = balancePayFee
        self.cashCouponPayFee = cashCouponPayFee
        self.arrearFee = arrearFee
        self.billFee2 = billFee2
        self.discountFee = discountFee
        self.groupTagValue = groupTagValue
