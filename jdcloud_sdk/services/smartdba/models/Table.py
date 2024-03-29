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


class Table(object):

    def __init__(self, typeId=None, title=None, message=None, note=None, formHeader=None, count=None):
        """
        :param typeId: (Optional) 诊断类型id
        :param title: (Optional) 诊断名称
        :param message: (Optional) 问题与建议
        :param note: (Optional) 其他信息提示，如："mysql 5.5 5.6 mariadb不支持"
        :param formHeader: (Optional) 受影响表 表头
        :param count: (Optional) 问题数量
        """

        self.typeId = typeId
        self.title = title
        self.message = message
        self.note = note
        self.formHeader = formHeader
        self.count = count
