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


class DistributorBillReturnDTO(object):

    def __init__(self, id=None, distributorId=None, distributorPin=None, summaryDate=None, billType=None, origId=None, pin=None, appCode=None, serviceCode=None, billFee2=None, discountFee=None, actualFee=None, payCouponFee=None, freeCouponFee=None, balancePayFee=None, cashPayFee=None, performanceFee=None, discountRatio=None, returnRatio=None, reFundFlag=None, monthAmount=None, monthReturnRatio=None, monthReturnAmount=None, origMonthReturnAmount=None, quarterAmount=None, quarterReturnRatio=None, currentQuarterReturnRatio=None, currentQuarterReturnAmount=None, origQuarterReturnAmount=None, remark=None, returnBillId=None, quarterReturnBillId=None, returnOrderId=None, monthDataSourceId=None, quarterDataSourceId=None, settlementNo=None, status=None, fileUuids=None, createTime=None, createUser=None, updateTime=None, updateUser=None, yn=None):
        """
        :param id: (Optional) ID(调账修改、删除操作必须传递)
        :param distributorId: (Optional) 服务商ID
        :param distributorPin: (Optional) 服务商pin
        :param summaryDate: (Optional) 生成时间
        :param billType: (Optional) 账单类型
        :param origId: (Optional) 原账单id
        :param pin: (Optional) pin
        :param appCode: (Optional) 业务线
        :param serviceCode: (Optional) 产品线
        :param billFee2: (Optional) 原价
        :param discountFee: (Optional) 折扣金额
        :param actualFee: (Optional) 优惠后金额
        :param payCouponFee: (Optional) 付费代金券金额
        :param freeCouponFee: (Optional) 免费代金券金额
        :param balancePayFee: (Optional) 余额支付金额
        :param cashPayFee: (Optional) 在线支付金额
        :param performanceFee: (Optional) 业绩金额
        :param discountRatio: (Optional) 折扣率
        :param returnRatio: (Optional) 返还率
        :param reFundFlag: (Optional) 状态
        :param monthAmount: (Optional) 月业绩金额
        :param monthReturnRatio: (Optional) 月返还率
        :param monthReturnAmount: (Optional) 实际月返还金额(调账修改必须传递)
        :param origMonthReturnAmount: (Optional) 月返还金额
        :param quarterAmount: (Optional) 季度业绩金额
        :param quarterReturnRatio: (Optional) 季度返还率
        :param currentQuarterReturnRatio: (Optional) 当季度返还率
        :param currentQuarterReturnAmount: (Optional) 当季度返还金额(调账修改必须传递)
        :param origQuarterReturnAmount: (Optional) 季度返还金额
        :param remark: (Optional) 调账原因
        :param returnBillId: (Optional) 月返还明细ID
        :param quarterReturnBillId: (Optional) 季度返还明细ID
        :param returnOrderId: (Optional) 返还单ID
        :param monthDataSourceId: (Optional) 月数据源id
        :param quarterDataSourceId: (Optional) 季度数据源id
        :param settlementNo: (Optional) 结算单号
        :param status: (Optional) 状态
        :param fileUuids: (Optional) 附件文件唯一标识
        :param createTime: (Optional) 创建时间
        :param createUser: (Optional) 创建人
        :param updateTime: (Optional) 修改时间
        :param updateUser: (Optional) 修改人
        :param yn: (Optional) 是否删除0未删除,1已删除
        """

        self.id = id
        self.distributorId = distributorId
        self.distributorPin = distributorPin
        self.summaryDate = summaryDate
        self.billType = billType
        self.origId = origId
        self.pin = pin
        self.appCode = appCode
        self.serviceCode = serviceCode
        self.billFee2 = billFee2
        self.discountFee = discountFee
        self.actualFee = actualFee
        self.payCouponFee = payCouponFee
        self.freeCouponFee = freeCouponFee
        self.balancePayFee = balancePayFee
        self.cashPayFee = cashPayFee
        self.performanceFee = performanceFee
        self.discountRatio = discountRatio
        self.returnRatio = returnRatio
        self.reFundFlag = reFundFlag
        self.monthAmount = monthAmount
        self.monthReturnRatio = monthReturnRatio
        self.monthReturnAmount = monthReturnAmount
        self.origMonthReturnAmount = origMonthReturnAmount
        self.quarterAmount = quarterAmount
        self.quarterReturnRatio = quarterReturnRatio
        self.currentQuarterReturnRatio = currentQuarterReturnRatio
        self.currentQuarterReturnAmount = currentQuarterReturnAmount
        self.origQuarterReturnAmount = origQuarterReturnAmount
        self.remark = remark
        self.returnBillId = returnBillId
        self.quarterReturnBillId = quarterReturnBillId
        self.returnOrderId = returnOrderId
        self.monthDataSourceId = monthDataSourceId
        self.quarterDataSourceId = quarterDataSourceId
        self.settlementNo = settlementNo
        self.status = status
        self.fileUuids = fileUuids
        self.createTime = createTime
        self.createUser = createUser
        self.updateTime = updateTime
        self.updateUser = updateUser
        self.yn = yn