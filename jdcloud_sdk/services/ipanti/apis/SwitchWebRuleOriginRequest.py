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


class SwitchWebRuleOriginRequest(JDCloudRequest):
    """
    网站类规则切换成回源状态。支持批量操作, 批量操作时 webRuleId 传多个, 以 ',' 分隔, 返回 result.code 为 1 表示操作成功, 为 0 时可能全部失败, 也可能部分失败
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(SwitchWebRuleOriginRequest, self).__init__(
            '/regions/{regionId}/instances/{instanceId}/webRules/{webRuleId}:origin', 'POST', header, version)
        self.parameters = parameters


class SwitchWebRuleOriginParameters(object):

    def __init__(self, regionId,instanceId,webRuleId,):
        """
        :param regionId: 区域 ID, 高防不区分区域, 传 cn-north-1 即可
        :param instanceId: 高防实例 Id
        :param webRuleId: 网站规则 Id
        """

        self.regionId = regionId
        self.instanceId = instanceId
        self.webRuleId = webRuleId

