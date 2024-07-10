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


class ContractSpec(object):

    def __init__(self, personStamps=None, companyStamps=None, contractContent=None, templateContent=None, templateId=None, contractTitle=None, caType=None, stampStyle=None, certExpire=None, businessId=None, needStorage=None, needContract=None, dept=None, pageRange=None):
        """
        :param personStamps: (Optional) 个人用户盖章信息(个人用户盖章信息、企业用户盖章信息 至少存在一项)
        :param companyStamps: (Optional) 企业用户盖章信息(个人用户盖章信息、企业用户盖章信息 至少存在一项)
        :param contractContent: (Optional) 合同文件（base64）
        :param templateContent: (Optional) 合同模板文件（base64）
        :param templateId: (Optional) 合同模板文件ID
        :param contractTitle: (Optional) 合同标题或名称
        :param caType: (Optional) 证书类型
        :param stampStyle: (Optional) 自定义签章类型（如需增加时间戳，此字段传time）
        :param certExpire: (Optional) 0：普通证书 1：事件证书（默认为0，普通证书）
        :param businessId: (Optional) 证书类型
        :param needStorage: (Optional) 签署完的合同是否在京东云存储（默认为false，不存储）
        :param needContract: (Optional) 是否需要返回已签署的合同（默认为true）
        :param dept: (Optional) 部门信息
        :param pageRange: (Optional) 页范围，仅在坐标签章生效(personStamps,companyStamps中的该属性优先生效) 1. all，表示所有页码;2. 数字以逗号分隔，形如："1,2,3""1,2,3";3. 以短横线：以短横线'-'分隔的两个数字，会被扩展为⼀段范围，形如："2-4";4：规则2和3可以混用，形如："2-4,7"
        """

        self.personStamps = personStamps
        self.companyStamps = companyStamps
        self.contractContent = contractContent
        self.templateContent = templateContent
        self.templateId = templateId
        self.contractTitle = contractTitle
        self.caType = caType
        self.stampStyle = stampStyle
        self.certExpire = certExpire
        self.businessId = businessId
        self.needStorage = needStorage
        self.needContract = needContract
        self.dept = dept
        self.pageRange = pageRange
