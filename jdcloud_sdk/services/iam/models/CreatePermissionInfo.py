# coding=utf8

# Copyright 2018-2025 JDCLOUD.COM
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http:#www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# NOTE: This class is auto generated by the jdcloud code generator program.


class CreatePermissionInfo(object):

    def __init__(self, name, content, description=None):
        """
        :param name:  权限名称，1~32位数字、字母、中文、下划线、下划线、中划线
        :param description: (Optional) 描述，0~256个字符
        :param content:  权限详细信息
        """

        self.name = name
        self.description = description
        self.content = content
