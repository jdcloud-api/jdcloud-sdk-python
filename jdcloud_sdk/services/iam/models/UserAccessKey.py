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


class UserAccessKey(object):

    def __init__(self, accessKey=None, accessKeySecret=None, createTime=None, modified=None, lastVisitTime=None, lastVisitEvent=None, state=None, yn=None, remark=None):
        """
        :param accessKey: (Optional) accessKey
        :param accessKeySecret: (Optional) accessKeySecret
        :param createTime: (Optional) 创建时间
        :param modified: (Optional) 修改时间
        :param lastVisitTime: (Optional) 最近一次使用AK访问时间
        :param lastVisitEvent: (Optional) 最近一次使用AK访问事件
        :param state: (Optional) 禁用/启用状态[0-禁用,1-启用]
        :param yn: (Optional) 删除/有效状态[0-删除,1-有效]
        :param remark: (Optional) AK备注信息
        """

        self.accessKey = accessKey
        self.accessKeySecret = accessKeySecret
        self.createTime = createTime
        self.modified = modified
        self.lastVisitTime = lastVisitTime
        self.lastVisitEvent = lastVisitEvent
        self.state = state
        self.yn = yn
        self.remark = remark
