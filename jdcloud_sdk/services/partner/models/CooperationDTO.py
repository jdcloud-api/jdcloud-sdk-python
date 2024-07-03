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


class CooperationDTO(object):

    def __init__(self, name, partnerType, cooperationModel, business, targetCustomer, valueProposition, coreValue, prospectiveEarnings, orgCode, orgName, companyName=None, status=None, followPerson=None, dockingPeoples=None, followRecords=None, cooperationCompanys=None):
        """
        :param name:  合作名称
        :param companyName: (Optional) 公司名称
        :param partnerType:  伙伴类型
        :param cooperationModel:  合作模式
        :param business:  合作领域
        :param targetCustomer:  目标客户
        :param valueProposition:  合作价值主张
        :param coreValue:  合作伙伴核心价值
        :param prospectiveEarnings:  合作预期收益
        :param status: (Optional) 合作状态
        :param orgCode:  合作部门code
        :param orgName:  合作部门名称
        :param followPerson: (Optional) 跟进人
        :param dockingPeoples: (Optional) 对接人列表
        :param followRecords: (Optional) 跟进记录
        :param cooperationCompanys: (Optional) 合作公司
        """

        self.name = name
        self.companyName = companyName
        self.partnerType = partnerType
        self.cooperationModel = cooperationModel
        self.business = business
        self.targetCustomer = targetCustomer
        self.valueProposition = valueProposition
        self.coreValue = coreValue
        self.prospectiveEarnings = prospectiveEarnings
        self.status = status
        self.orgCode = orgCode
        self.orgName = orgName
        self.followPerson = followPerson
        self.dockingPeoples = dockingPeoples
        self.followRecords = followRecords
        self.cooperationCompanys = cooperationCompanys
