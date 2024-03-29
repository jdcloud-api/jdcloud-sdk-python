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


class ModifyFlowLogRequest(JDCloudRequest):
    """
    本接口用于修改流日志资源，包括流日志的名称、描述、采集时间间隔
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(ModifyFlowLogRequest, self).__init__(
            '/regions/{regionId}/flowLogs/{flowLogId}', 'PATCH', header, version)
        self.parameters = parameters


class ModifyFlowLogParameters(object):

    def __init__(self,regionId, flowLogId, ):
        """
        :param regionId: 地域 ID
        :param flowLogId: 流日志ID
        """

        self.regionId = regionId
        self.flowLogId = flowLogId
        self.flowLogName = None
        self.description = None
        self.collectInterval = None

    def setFlowLogName(self, flowLogName):
        """
        :param flowLogName: (Optional) 流日志名称，只允许输入中文、数字、大小写字母、英文下划线“_”及中划线“-”，不允许为空且不超过32字符
        """
        self.flowLogName = flowLogName

    def setDescription(self, description):
        """
        :param description: (Optional) 描述,允许输入UTF-8编码下的全部字符，不超过256字符
        """
        self.description = description

    def setCollectInterval(self, collectInterval):
        """
        :param collectInterval: (Optional) 流日志采集时间间隔。单位：分钟。取值：1、5、10
        """
        self.collectInterval = collectInterval

