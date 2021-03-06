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

from jdcloud_sdk.core.jdcloudrequest import JDCloudRequest


class ModyfyAgentLimitsRequest(JDCloudRequest):
    """
    修改agent资源限额,支持多个agentId,英文逗号分隔
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(ModyfyAgentLimitsRequest, self).__init__(
            '/regions/{regionId}/agents/{agentId}', 'PATCH', header, version)
        self.parameters = parameters


class ModyfyAgentLimitsParameters(object):

    def __init__(self, regionId, agentId, ):
        """
        :param regionId: 地域 Id
        :param agentId: agentId
        """

        self.regionId = regionId
        self.agentId = agentId
        self.limitStatus = None
        self.cpuLimit = None
        self.memLimit = None

    def setLimitStatus(self, limitStatus):
        """
        :param limitStatus: (Optional) 是否限制 0 不限制 1 限制(cpuLimit/memLimit必填)
        """
        self.limitStatus = limitStatus

    def setCpuLimit(self, cpuLimit):
        """
        :param cpuLimit: (Optional) cpu使用限制（1%-50%）
        """
        self.cpuLimit = cpuLimit

    def setMemLimit(self, memLimit):
        """
        :param memLimit: (Optional) 内存占用限额（1%-50%）
        """
        self.memLimit = memLimit

