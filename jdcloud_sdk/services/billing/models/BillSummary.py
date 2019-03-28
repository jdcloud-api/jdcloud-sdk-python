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


class BillSummary(object):

    def __init__(self, pin=None, appCode=None, appCodeName=None, serviceCode=None, serviceCodeName=None, billingType=None, billingTypeName=None, resourceId=None, resourceName=None, region=None, actionTypeName=None, formula=None, startTime=None, endTime=None, billTime=None, totalFee=None, discountFee=None, realTotalFee=None, cashCouponPayFee=None, balancePayFee=None, cashPayFee=None, arrearFee=None):
        """
        :param pin: (Optional) 用户pin
        :param appCode: (Optional) appCode
        :param appCodeName: (Optional) 产品线代码名称
        :param serviceCode: (Optional) serviceCode
        :param serviceCodeName: (Optional) 产品代码名称
        :param billingType: (Optional) 计费类型
        :param billingTypeName: (Optional) 计费类型描述
        :param resourceId: (Optional) 资源id
        :param resourceName: (Optional) 资源名称
        :param region: (Optional) 区域
        :param actionTypeName: (Optional) 费用类型
        :param formula: (Optional) 规格
        :param startTime: (Optional) 计费开始时间
        :param endTime: (Optional) 计费结束时间
        :param billTime: (Optional) 账单生成时间
        :param totalFee: (Optional) 账单总额
        :param discountFee: (Optional) 优惠金额
        :param realTotalFee: (Optional) 优惠后总价金额
        :param cashCouponPayFee: (Optional) 代金券支付金额
        :param balancePayFee: (Optional) 余额支付金额
        :param cashPayFee: (Optional) 现金支付金额
        :param arrearFee: (Optional) 欠费金额
        """

        self.pin = pin
        self.appCode = appCode
        self.appCodeName = appCodeName
        self.serviceCode = serviceCode
        self.serviceCodeName = serviceCodeName
        self.billingType = billingType
        self.billingTypeName = billingTypeName
        self.resourceId = resourceId
        self.resourceName = resourceName
        self.region = region
        self.actionTypeName = actionTypeName
        self.formula = formula
        self.startTime = startTime
        self.endTime = endTime
        self.billTime = billTime
        self.totalFee = totalFee
        self.discountFee = discountFee
        self.realTotalFee = realTotalFee
        self.cashCouponPayFee = cashCouponPayFee
        self.balancePayFee = balancePayFee
        self.cashPayFee = cashPayFee
        self.arrearFee = arrearFee