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


class ModifyParam(object):

    def __init__(self, name=None, value=None, nodeType=None):
        """
        :param name: (Optional) 参数名称
        :param value: (Optional) 参数修改值
        :param nodeType: (Optional) 参数的节点类型，包括TiKV,TiDB,PD,TiFlash
        """

        self.name = name
        self.value = value
        self.nodeType = nodeType
