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

    def __init__(self, personStamps=None, companyStamps=None, contractContent=None, templateContent=None, templateId=None, contractTitle=None, caType=None, stampStyle=None, dept=None, pageRange=None):
        """
        :param personStamps: (Optional) 个人用户盖章信息
        :param companyStamps: (Optional) 企业用户盖章信息
        :param contractContent: (Optional) 合同文件（base64）
        :param templateContent: (Optional) 合同模板文件（base64）
        :param templateId: (Optional) 合同模板文件ID
        :param contractTitle: (Optional) 合同标题或名称
        :param caType: (Optional) 证书类型
        :param stampStyle: (Optional) 自定义签章类型（如需增加时间戳，此字段传time）
        :param dept: (Optional) 部门信息
        :param pageRange: (Optional) 盖章范围
        """

        self.personStamps = personStamps
        self.companyStamps = companyStamps
        self.contractContent = contractContent
        self.templateContent = templateContent
        self.templateId = templateId
        self.contractTitle = contractTitle
        self.caType = caType
        self.stampStyle = stampStyle
        self.dept = dept
        self.pageRange = pageRange
