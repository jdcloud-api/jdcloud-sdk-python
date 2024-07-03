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


class PartnerQuery(object):

    def __init__(self, id=None, partnerId=None, companyName=None, registeredOffice=None, source=None, industryField=None, activityId=None, applyId=None, followPerson=None, status=None, cooperationFlag=None, cooperationProductFlag=None, industry=None, businessProduct=None, pin=None, partnerTag=None, partnerLevel=None, queryType=None, pageIndex=None, pageSize=None, offset=None):
        """
        :param id: (Optional) id
        :param partnerId: (Optional) 合作伙伴ID
        :param companyName: (Optional) 公司名称
        :param registeredOffice: (Optional) 注册地
        :param source: (Optional) 伙伴来源
        :param industryField: (Optional) 行业领域
        :param activityId: (Optional) 活动ID
        :param applyId: (Optional) 线索ID
        :param followPerson: (Optional) 跟进人
        :param status: (Optional) 状态
        :param cooperationFlag: (Optional) 合作信息标识（0无1有）
        :param cooperationProductFlag: (Optional) 合作产品标识（0无1有）
        :param industry: (Optional) 所属行业
        :param businessProduct: (Optional) 核心产品及业务
        :param pin: (Optional) 合作伙伴用户pin
        :param partnerTag: (Optional) 伙伴标签
        :param partnerLevel: (Optional) 合作伙伴级别
        :param queryType: (Optional) 查询类型
        :param pageIndex: (Optional) 当前页序号
        :param pageSize: (Optional) 每页结果数量
        :param offset: (Optional) 
        """

        self.id = id
        self.partnerId = partnerId
        self.companyName = companyName
        self.registeredOffice = registeredOffice
        self.source = source
        self.industryField = industryField
        self.activityId = activityId
        self.applyId = applyId
        self.followPerson = followPerson
        self.status = status
        self.cooperationFlag = cooperationFlag
        self.cooperationProductFlag = cooperationProductFlag
        self.industry = industry
        self.businessProduct = businessProduct
        self.pin = pin
        self.partnerTag = partnerTag
        self.partnerLevel = partnerLevel
        self.queryType = queryType
        self.pageIndex = pageIndex
        self.pageSize = pageSize
        self.offset = offset
