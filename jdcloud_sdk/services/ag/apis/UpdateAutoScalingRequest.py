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


class UpdateAutoScalingRequest(JDCloudRequest):
    """
    更新弹性伸缩组
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(UpdateAutoScalingRequest, self).__init__(
            '/regions/{regionId}/autoScaling/{agId}:updateAutoScaling', 'POST', header, version)
        self.parameters = parameters


class UpdateAutoScalingParameters(object):

    def __init__(self,regionId, agId, autoscalingSpec):
        """
        :param regionId: 地域
        :param agId: 高可用组 ID
        :param autoscalingSpec: 伸缩组详细信息
        """

        self.regionId = regionId
        self.agId = agId
        self.autoscalingSpec = autoscalingSpec

