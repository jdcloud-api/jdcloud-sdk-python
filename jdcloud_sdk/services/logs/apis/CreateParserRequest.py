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


class CreateParserRequest(JDCloudRequest):
    """
    创建日志的解析配置。
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(CreateParserRequest, self).__init__(
            '/regions/{regionId}/logtopics/{logtopicUID}/createParser', 'POST', header, version)
        self.parameters = parameters


class CreateParserParameters(object):

    def __init__(self, regionId,logtopicUID,parserFields, parserMode, ):
        """
        :param regionId: 地域 Id
        :param logtopicUID: 日志主题 UID
        :param parserFields: 
        :param parserMode: 解析类型。oneline - 单行，split - 分割， json - json， regexp - regexp
        """

        self.regionId = regionId
        self.logtopicUID = logtopicUID
        self.parserFields = parserFields
        self.parserMode = parserMode
        self.parserPattern = None
        self.parserSample = None
        self.pipelines = None

    def setParserPattern(self, parserPattern):
        """
        :param parserPattern: (Optional) 解析语法
        """
        self.parserPattern = parserPattern

    def setParserSample(self, parserSample):
        """
        :param parserSample: (Optional) 日志样例
        """
        self.parserSample = parserSample

    def setPipelines(self, pipelines):
        """
        :param pipelines: (Optional) 预处理任务列表。按照数组的顺序执行。
        """
        self.pipelines = pipelines

