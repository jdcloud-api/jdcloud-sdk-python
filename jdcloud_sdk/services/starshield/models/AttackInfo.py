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


class AttackInfo(object):

    def __init__(self, date=None, id=None, group=None, desc=None, attackSum=None):
        """
        :param date: (Optional) 时间
        :param id: (Optional) 规则id
        :param group: (Optional) 分组
        :param desc: (Optional) 描述
        :param attackSum: (Optional) 攻击次数
        """

        self.date = date
        self.id = id
        self.group = group
        self.desc = desc
        self.attackSum = attackSum
