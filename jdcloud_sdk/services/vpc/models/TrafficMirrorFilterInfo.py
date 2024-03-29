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


class TrafficMirrorFilterInfo(object):

    def __init__(self, mirrorFilterId=None, mirrorFilterName=None, description=None, createdTime=None, egressRules=None, ingressRules=None, trafficMirrorSessions=None):
        """
        :param mirrorFilterId: (Optional) 镜像过滤器ID
        :param mirrorFilterName: (Optional) 镜像过滤器名称，只允许输入中文、数字、大小写字母、英文下划线“_”及中划线“-”，不允许为空且不超过32字符
        :param description: (Optional) 描述,允许输入UTF-8编码下的全部字符，不超过256字符
        :param createdTime: (Optional) Filter创建时间
        :param egressRules: (Optional) 出方向规则详情列表。
        :param ingressRules: (Optional) 入方向规则详情列表。
        :param trafficMirrorSessions: (Optional) 所关联的流量镜像会话
        """

        self.mirrorFilterId = mirrorFilterId
        self.mirrorFilterName = mirrorFilterName
        self.description = description
        self.createdTime = createdTime
        self.egressRules = egressRules
        self.ingressRules = ingressRules
        self.trafficMirrorSessions = trafficMirrorSessions
