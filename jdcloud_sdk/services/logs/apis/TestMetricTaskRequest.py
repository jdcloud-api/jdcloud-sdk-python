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


class TestMetricTaskRequest(JDCloudRequest):
    """
    日志测试，根据用户输入的日志筛选条件以及监控指标设置进行模拟监控统计
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(TestMetricTaskRequest, self).__init__(
            '/regions/{regionId}/logsets/{logsetUID}/logtopics/{logtopicUID}/metrictaskTest', 'POST', header, version)
        self.parameters = parameters


class TestMetricTaskParameters(object):

    def __init__(self, regionId, logsetUID, logtopicUID, aggregate, content, dataField, filterOpen, filterType):
        """
        :param regionId: 地域 Id
        :param logsetUID: 日志集 UID
        :param logtopicUID: 日志主题 UID
        :param aggregate: 聚合函数,支持 count sum max min avg
        :param content: 测试内容
        :param dataField: 查询字段,支持 英文字母 数字 下划线 中划线 点（中文日志原文和各产品线的key）
        :param filterOpen: 是否打开过滤
        :param filterType: 过滤类型，只能是fulltext和 advance
        """

        self.regionId = regionId
        self.logsetUID = logsetUID
        self.logtopicUID = logtopicUID
        self.aggregate = aggregate
        self.content = content
        self.dataField = dataField
        self.filterContent = None
        self.filterOpen = filterOpen
        self.filterType = filterType

    def setFilterContent(self, filterContent):
        """
        :param filterContent: (Optional) 过滤语法，可以为空
        """
        self.filterContent = filterContent

