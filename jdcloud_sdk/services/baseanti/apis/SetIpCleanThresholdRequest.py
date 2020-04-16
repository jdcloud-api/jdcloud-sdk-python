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


class SetIpCleanThresholdRequest(JDCloudRequest):
    """
    设置基础防护已防护公网 IP 的清洗阈值, 支持 ipv4 和 ipv6
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(SetIpCleanThresholdRequest, self).__init__(
            '/regions/{regionId}/setIpCleanThreshold', 'POST', header, version)
        self.parameters = parameters


class SetIpCleanThresholdParameters(object):

    def __init__(self, regionId, ipCleanThresholdSpec):
        """
        :param regionId: 地域编码. 基础防护已支持华北-北京, 华东-宿迁, 华东-上海, 华南-广州
        :param ipCleanThresholdSpec: 请求参数
        """

        self.regionId = regionId
        self.ipCleanThresholdSpec = ipCleanThresholdSpec

