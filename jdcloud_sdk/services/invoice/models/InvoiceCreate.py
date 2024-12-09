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


class InvoiceCreate(object):

    def __init__(self, orderIds=None, deductOrderIds=None, mediumType=None, createInvoiceType=None, remark=None, invoiceAll=None, orderStartTime=None, orderEndTime=None, monthGroups=None, amount=None):
        """
        :param orderIds: (Optional) 需要开票的订单号列表，以逗号分隔
        :param deductOrderIds: (Optional) 抵扣单据单号列表，以逗号分隔
        :param mediumType: (Optional) 发票类型[电子-electronic]
        :param createInvoiceType: (Optional) 开票类型[按明细开票-consume，按月账单开票-month，指定金额开票-money(mediumType=paper生效)]
        :param remark: (Optional) 开票备注
        :param invoiceAll: (Optional) 是否全部开票[全部开票-1 不需要传orderIds 需要传 开始、结束时间]
        :param orderStartTime: (Optional) 开票订单的开始时间(开票标识为 全部开票 时不需要传)
        :param orderEndTime: (Optional) 开票订单的结束时间(开票标识为 全部开票 时不需要传)
        :param monthGroups: (Optional) 开票月份 仅按月账单开票生效 例（202407,202406）多个月份用逗号分隔
        :param amount: (Optional) 指定金额开票时 传入金额 开票类型=money时必传
        """

        self.orderIds = orderIds
        self.deductOrderIds = deductOrderIds
        self.mediumType = mediumType
        self.createInvoiceType = createInvoiceType
        self.remark = remark
        self.invoiceAll = invoiceAll
        self.orderStartTime = orderStartTime
        self.orderEndTime = orderEndTime
        self.monthGroups = monthGroups
        self.amount = amount