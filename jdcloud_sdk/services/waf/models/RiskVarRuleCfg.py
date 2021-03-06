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


class RiskVarRuleCfg(object):

    def __init__(self, left=None, operator=None, right=None, resultOpt=None, resultRight=None):
        """
        :param left: (Optional) 左表达式
        :param operator: (Optional) 操作符
        :param right: (Optional) 右表达式
        :param resultOpt: (Optional) 结果比较运算符
        :param resultRight: (Optional) 结果右表达式
        """

        self.left = left
        self.operator = operator
        self.right = right
        self.resultOpt = resultOpt
        self.resultRight = resultRight
