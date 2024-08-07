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


class UserGroupListVo(object):

    def __init__(self, name=None, code=None, operator=None, createBy=None, createTime=None, updateTime=None, status=None, state=None):
        """
        :param name: (Optional) 名称
        :param code: (Optional) 编码
        :param operator: (Optional) 操作人
        :param createBy: (Optional) 创建人
        :param createTime: (Optional) 创建时间
        :param updateTime: (Optional) 修改时间
        :param status: (Optional) 状态
        :param state: (Optional) 枚举编码
        """

        self.name = name
        self.code = code
        self.operator = operator
        self.createBy = createBy
        self.createTime = createTime
        self.updateTime = updateTime
        self.status = status
        self.state = state
