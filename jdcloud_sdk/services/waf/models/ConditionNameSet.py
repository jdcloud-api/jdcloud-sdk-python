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


class ConditionNameSet(object):

    def __init__(self, conditionId=None, conditionName=None, conditionType=None, opposite=None, nand=None):
        """
        :param conditionId: (Optional) 条件id
        :param conditionName: (Optional) 条件名称
        :param conditionType: (Optional) 条件类型
        :param opposite: (Optional) 对条件结果的取反操作，does不取反，doesnot取反
        :param nand: (Optional) 与或逻辑
        """

        self.conditionId = conditionId
        self.conditionName = conditionName
        self.conditionType = conditionType
        self.opposite = opposite
        self.nand = nand
