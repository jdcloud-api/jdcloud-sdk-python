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


class DescribeConsumeTraceRequest(JDCloudRequest):
    """
    查询消息消费轨迹（消费组列表）
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeConsumeTraceRequest, self).__init__(
            '/regions/{regionId}/instances/{instanceId}/topics/{topic}/consumeTrace/{messageId}', 'GET', header, version)
        self.parameters = parameters


class DescribeConsumeTraceParameters(object):

    def __init__(self,regionId, instanceId, topic, messageId, pageSize, pageNumber):
        """
        :param regionId: 区域ID
        :param instanceId: 实例id
        :param topic: topic 名称
        :param messageId: message Id
        :param pageSize: 分页大小
        :param pageNumber: 页码
        """

        self.regionId = regionId
        self.instanceId = instanceId
        self.topic = topic
        self.messageId = messageId
        self.traceTopic = None
        self.pageSize = pageSize
        self.pageNumber = pageNumber

    def setTraceTopic(self, traceTopic):
        """
        :param traceTopic: (Optional) 取决于客户端使用，如果未指定traceTopic,则不填
        """
        self.traceTopic = traceTopic

