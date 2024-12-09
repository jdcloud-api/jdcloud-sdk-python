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


class LogsetEnd(object):

    def __init__(self, uID=None, createTime=None, description=None, hasTopic=None, lifeCycle=None, name=None, region=None, resourceGroupUID=None, tags=None):
        """
        :param uID: (Optional) UID
        :param createTime: (Optional) 创建时间
        :param description: (Optional) 描述信息
        :param hasTopic: (Optional) 是否存在日志主题
        :param lifeCycle: (Optional) 保存周期
        :param name: (Optional) 日志集名称
        :param region: (Optional) 地域信息
        :param resourceGroupUID: (Optional) 资源组
        :param tags: (Optional) 标签列表
        """

        self.uID = uID
        self.createTime = createTime
        self.description = description
        self.hasTopic = hasTopic
        self.lifeCycle = lifeCycle
        self.name = name
        self.region = region
        self.resourceGroupUID = resourceGroupUID
        self.tags = tags
