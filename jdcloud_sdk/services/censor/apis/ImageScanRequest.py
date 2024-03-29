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


class ImageScanRequest(JDCloudRequest):
    """
    图片同步检测
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(ImageScanRequest, self).__init__(
            '/image:scan', 'POST', header, version)
        self.parameters = parameters


class ImageScanParameters(object):

    def __init__(self, ):
        """
        """

        self.bizType = None
        self.scenes = None
        self.tasks = None

    def setBizType(self, bizType):
        """
        :param bizType: (Optional) 机审策略，eg: default
        """
        self.bizType = bizType

    def setScenes(self, scenes):
        """
        :param scenes: (Optional) 指定检测场景
        """
        self.scenes = scenes

    def setTasks(self, tasks):
        """
        :param tasks: (Optional) 检测任务列表，包含一个或多个元素。每个元素是个结构体，最多可添加10个元素，即最多对10段文本进行检测。每个元素的具体结构描述见ImageTask。
        """
        self.tasks = tasks

