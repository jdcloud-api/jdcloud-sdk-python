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


class RefundResourceFee(object):

    def __init__(self, resourceId=None, fee=None, cashFee=None, balanceFee=None, couponFee=None, orderFees=None):
        """
        :param resourceId: (Optional) 资源id
        :param fee: (Optional) 资源退款金额
        :param cashFee: (Optional) 现金退款金额
        :param balanceFee: (Optional) 余额退款金额
        :param couponFee: (Optional) 代金券退款金额
        :param orderFees: (Optional) 退款订单列表
        """

        self.resourceId = resourceId
        self.fee = fee
        self.cashFee = cashFee
        self.balanceFee = balanceFee
        self.couponFee = couponFee
        self.orderFees = orderFees
