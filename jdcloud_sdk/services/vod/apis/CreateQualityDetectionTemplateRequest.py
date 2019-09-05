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


class CreateQualityDetectionTemplateRequest(JDCloudRequest):
    """
    创建质检模板
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(CreateQualityDetectionTemplateRequest, self).__init__(
            '/qualityDetectionTemplates', 'POST', header, version)
        self.parameters = parameters


class CreateQualityDetectionTemplateParameters(object):

    def __init__(self, name, templateType, detections):
        """
        :param name: 模板名称。长度不超过128个字符。UTF-8编码。

        :param templateType: 模板类型，区分该模板的检测内容。目前只支持 video 。
        :param detections: 检测项列表。取值范围：
  blackScreen - 黑场
  pureColor - 纯色
  colorCast - 偏色
  frozenFrame - 静帧
  brightness - 亮度
  contrast - 对比度

        """

        self.name = name
        self.templateType = templateType
        self.detections = detections

