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


class InstanceTemplate(object):

    def __init__(self, id=None, name=None, description=None, instanceTemplateData=None, ags=None, createdTime=None):
        """
        :param id: (Optional) 实例模板ID
        :param name: (Optional) 实例模板名称。
        :param description: (Optional) 实例模板描述。
        :param instanceTemplateData: (Optional) 实例模板详细配置。
        :param ags: (Optional) 关联的高可用组(ag)信息。
        :param createdTime: (Optional) 实例模板创建时间。
        """

        self.id = id
        self.name = name
        self.description = description
        self.instanceTemplateData = instanceTemplateData
        self.ags = ags
        self.createdTime = createdTime
