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


class RuleDetail(object):

    def __init__(self, ruleId=None, ruleName=None, ruleType=None, riskLevel=None, ruleContent=None, ruleDesc=None, editable=None):
        """
        :param ruleId: (Optional) 规则Id
        :param ruleName: (Optional) 规则名称
        :param ruleType: (Optional) 规则类型: 1->自定义,0->内置
        :param riskLevel: (Optional) 风险级别: 0->无风险，1->低风险，2->中风险，3->高风险
        :param ruleContent: (Optional) 规则定义正则表达式
        :param ruleDesc: (Optional) 规则描述
        :param editable: (Optional) 是否可被编辑(内置规则禁止编辑)
        """

        self.ruleId = ruleId
        self.ruleName = ruleName
        self.ruleType = ruleType
        self.riskLevel = riskLevel
        self.ruleContent = ruleContent
        self.ruleDesc = ruleDesc
        self.editable = editable
