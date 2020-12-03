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


class MonitorLabelDetail(object):

    def __init__(self, label=None, serviceCode=None, resourceId=None, filters=None, nodes=None):
        """
        :param label: (Optional) 监控显示名称
        :param serviceCode: (Optional) 监控项目代码
        :param resourceId: (Optional) 监控项目资源代码
        :param filters: (Optional) 过滤条件的值
        :param nodes: (Optional) 监控项目子节点信息
        """

        self.label = label
        self.serviceCode = serviceCode
        self.resourceId = resourceId
        self.filters = filters
        self.nodes = nodes
