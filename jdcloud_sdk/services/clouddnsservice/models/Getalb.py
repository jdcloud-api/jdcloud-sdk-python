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


class Getalb(object):

    def __init__(self, balance=None, record=None, type=None, viewName=None, viewValue=None, items=None):
        """
        :param balance: (Optional) 负载均衡的解析记录的列表中解析记录是否是相同的权重 
true: 均等负载 
false: 按权重分配负载

        :param record: (Optional) 主机记录
        :param type: (Optional) 解析的类型
        :param viewName: (Optional) 解析线路的名称
        :param viewValue: (Optional) 解析线路的ID
        :param items: (Optional) 负载均衡的解析记录的列表
        """

        self.balance = balance
        self.record = record
        self.type = type
        self.viewName = viewName
        self.viewValue = viewValue
        self.items = items
