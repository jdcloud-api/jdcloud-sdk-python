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


class FormulaBillSummary(object):

    def __init__(self, pin=None, resourceId=None, appCode=None, appCodeName=None, serviceCode=None, serviceCodeName=None, region=None, regionName=None, currency=None, billingType=None, billingTypeName=None, networkOperator=None, property=None, propertyName=None, propertyUnit=None, startTime=None, endTime=None, billDate=None, actualUsage=None, deductUsage=None, billingUsage=None, billFee=None, discountFee=None, actualFee=None, cashCouponPayFee=None, balancePayFee=None, cashPayFee=None):
        """
        :param pin: (Optional) 用户pin
        :param resourceId: (Optional) 资源id
        :param appCode: (Optional) 产品线代码
        :param appCodeName: (Optional) 产品线代码名称
        :param serviceCode: (Optional) 产品代码
        :param serviceCodeName: (Optional) 产品代码名称
        :param region: (Optional) 区域
        :param regionName: (Optional) 区域名称
        :param currency: (Optional) 币种
        :param billingType: (Optional) 计费类型
        :param billingTypeName: (Optional) 计费类型描述
        :param networkOperator: (Optional) 网络类型
        :param property: (Optional) 属性
        :param propertyName: (Optional) 属性名称
        :param propertyUnit: (Optional) 属性单位
        :param startTime: (Optional) 计费开始时间
        :param endTime: (Optional) 计费结束时间
        :param billDate: (Optional) 出账月份
        :param actualUsage: (Optional) 实际用量
        :param deductUsage: (Optional) 抵扣用量
        :param billingUsage: (Optional) 计费用量
        :param billFee: (Optional) 优惠前费用
        :param discountFee: (Optional) 优惠金额
        :param actualFee: (Optional) 应付金额
        :param cashCouponPayFee: (Optional) 代金券支付金额
        :param balancePayFee: (Optional) 余额支付金额
        :param cashPayFee: (Optional) 现金支付金额
        """

        self.pin = pin
        self.resourceId = resourceId
        self.appCode = appCode
        self.appCodeName = appCodeName
        self.serviceCode = serviceCode
        self.serviceCodeName = serviceCodeName
        self.region = region
        self.regionName = regionName
        self.currency = currency
        self.billingType = billingType
        self.billingTypeName = billingTypeName
        self.networkOperator = networkOperator
        self.property = property
        self.propertyName = propertyName
        self.propertyUnit = propertyUnit
        self.startTime = startTime
        self.endTime = endTime
        self.billDate = billDate
        self.actualUsage = actualUsage
        self.deductUsage = deductUsage
        self.billingUsage = billingUsage
        self.billFee = billFee
        self.discountFee = discountFee
        self.actualFee = actualFee
        self.cashCouponPayFee = cashCouponPayFee
        self.balancePayFee = balancePayFee
        self.cashPayFee = cashPayFee