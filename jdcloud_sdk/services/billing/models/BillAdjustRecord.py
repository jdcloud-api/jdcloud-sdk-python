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


class BillAdjustRecord(object):

    def __init__(self, pin=None, serviceCode=None, resourceId=None, actualFee=None, adjustFee=None, property=None, usage=None, adjustUsage=None, usageUnit=None, opType=None, billDate=None, state=None, reason=None, file1Name=None, file1Url=None, file2Name=None, file2Url=None, file3Name=None, file3Url=None, erp=None, createTime=None, updateTime=None):
        """
        :param pin: (Optional) pin
        :param serviceCode: (Optional) 产品
        :param resourceId: (Optional) 资源ID
        :param actualFee: (Optional) 应付金额
        :param adjustFee: (Optional) 调整金额
        :param property: (Optional) 计费项
        :param usage: (Optional) 用量
        :param adjustUsage: (Optional) 调整用量
        :param usageUnit: (Optional) 用量单位
        :param opType: (Optional) 操作类型 1 调整金额 2 调整用量 3 调账
        :param billDate: (Optional) 调整月份(yyyyMM)
        :param state: (Optional) 状态 1调整中 2调整完成 3 失败
        :param reason: (Optional) 调整原因
        :param file1Name: (Optional) 附件1名称
        :param file1Url: (Optional) 附件1url
        :param file2Name: (Optional) 附件2名称
        :param file2Url: (Optional) 附件2url
        :param file3Name: (Optional) 附件3名称
        :param file3Url: (Optional) 附件3url
        :param erp: (Optional) erp
        :param createTime: (Optional) createTime
        :param updateTime: (Optional) updateTime
        """

        self.pin = pin
        self.serviceCode = serviceCode
        self.resourceId = resourceId
        self.actualFee = actualFee
        self.adjustFee = adjustFee
        self.property = property
        self.usage = usage
        self.adjustUsage = adjustUsage
        self.usageUnit = usageUnit
        self.opType = opType
        self.billDate = billDate
        self.state = state
        self.reason = reason
        self.file1Name = file1Name
        self.file1Url = file1Url
        self.file2Name = file2Name
        self.file2Url = file2Url
        self.file3Name = file3Name
        self.file3Url = file3Url
        self.erp = erp
        self.createTime = createTime
        self.updateTime = updateTime
