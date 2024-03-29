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


class UpdateLiveForwardTaskRequest(JDCloudRequest):
    """
    更新直播拉流转推任务

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(UpdateLiveForwardTaskRequest, self).__init__(
            '/LiveForwardTask:update', 'POST', header, version)
        self.parameters = parameters


class UpdateLiveForwardTaskParameters(object):

    def __init__(self, taskId, ):
        """
        :param taskId: 任务ID

        """

        self.taskId = taskId
        self.sourceUrl = None
        self.pushUrl = None
        self.startTime = None
        self.endTime = None
        self.callbackEvents = None
        self.callbackUrl = None
        self.name = None

    def setSourceUrl(self, sourceUrl):
        """
        :param sourceUrl: (Optional) 拉流地址
- 支持rtmp

        """
        self.sourceUrl = sourceUrl

    def setPushUrl(self, pushUrl):
        """
        :param pushUrl: (Optional) 转推地址
- 支持rtmp

        """
        self.pushUrl = pushUrl

    def setStartTime(self, startTime):
        """
        :param startTime: (Optional) 开始时间
- UTC时间， ISO8601示例：2021-07-26T08:08:08Z
- 不填表示立即开始

        """
        self.startTime = startTime

    def setEndTime(self, endTime):
        """
        :param endTime: (Optional) 结束时间
- UTC时间， ISO8601示例：2021-07-26T08:08:08Z
- 最大支持365天，与开始时间间隔不超过7天。
- 不填拉不到流10分钟自动结束

        """
        self.endTime = endTime

    def setCallbackEvents(self, callbackEvents):
        """
        :param callbackEvents: (Optional) 回调类型
- 不填发送全部回调
- TaskStart 任务开始
- TaskExit 任务结束
- callbackUrl非空的情况下，callbackEvents有效

        """
        self.callbackEvents = callbackEvents

    def setCallbackUrl(self, callbackUrl):
        """
        :param callbackUrl: (Optional) 事件回调地址

        """
        self.callbackUrl = callbackUrl

    def setName(self, name):
        """
        :param name: (Optional) 任务名称
- 最大255字符

        """
        self.name = name

