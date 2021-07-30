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


class AsyncVideoScanRequest(JDCloudRequest):
    """
    提交视频异步检测任务
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(AsyncVideoScanRequest, self).__init__(
            '/video:asyncscan', 'POST', header, version)
        self.parameters = parameters


class AsyncVideoScanParameters(object):

    def __init__(self, ):
        """
        """

        self.bizType = None
        self.live = None
        self.scenes = None
        self.audioScenes = None
        self.tasks = None
        self.callback = None
        self.seed = None

    def setBizType(self, bizType):
        """
        :param bizType: (Optional) 机审策略，eg: default
        """
        self.bizType = bizType

    def setLive(self, live):
        """
        :param live: (Optional) 是否直播。默认为false，表示为普通视频检测；若是直播检测，该值必须传入true。
        """
        self.live = live

    def setScenes(self, scenes):
        """
        :param scenes: (Optional) 指定检测场景
        """
        self.scenes = scenes

    def setAudioScenes(self, audioScenes):
        """
        :param audioScenes: (Optional) 视频中语音的检测场景
        """
        self.audioScenes = audioScenes

    def setTasks(self, tasks):
        """
        :param tasks: (Optional) 检测任务列表，包含一个或多个元素。每个元素是个结构体，最多可添加10个元素，每个元素的具体结构描述见videoTask。
        """
        self.tasks = tasks

    def setCallback(self, callback):
        """
        :param callback: (Optional) 异步检测结果回调通知您的URL，支持HTTP/HTTPS。该字段为空时，您必须定时检索检测结果。
        """
        self.callback = callback

    def setSeed(self, seed):
        """
        :param seed: (Optional) 随机字符串，该值用于回调通知请求中的签名。当使用callback时，该字段必须提供。
        """
        self.seed = seed

