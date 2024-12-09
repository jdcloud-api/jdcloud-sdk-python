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


class UpdateMetricTaskRequest(JDCloudRequest):
    """
    更新监控任务，日志监控任务不许重名。
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(UpdateMetricTaskRequest, self).__init__(
            '/regions/{regionId}/logsets/{logsetUID}/logtopics/{logtopicUID}/metrictasks/{logmetrictaskUID}', 'PUT', header, version)
        self.parameters = parameters


class UpdateMetricTaskParameters(object):

    def __init__(self,regionId, logsetUID, logtopicUID, logmetrictaskUID, customUnit, name, unit):
        """
        :param regionId: 地域 Id
        :param logsetUID: 日志集 UID
        :param logtopicUID: 日志主题 UID
        :param logmetrictaskUID: 
        :param customUnit: 自定义单位
        :param name: 监控任务名称,同一日志主题下唯一，支持中文 大小写英文字母 下划线 中划线 数字，且不超过32
        :param unit: 单位
        """

        self.regionId = regionId
        self.logsetUID = logsetUID
        self.logtopicUID = logtopicUID
        self.logmetrictaskUID = logmetrictaskUID
        self.aggregate = None
        self.customUnit = customUnit
        self.dataField = None
        self.filterContent = None
        self.filterOpen = None
        self.filterType = None
        self.metric = None
        self.name = name
        self.settingType = None
        self.sqlSpec = None
        self.unit = unit

    def setAggregate(self, aggregate):
        """
        :param aggregate: (Optional) 聚合函数,支持 count sum max min avg; 配置方式(SettingType) 为 空或visual 时，必填；
        """
        self.aggregate = aggregate

    def setDataField(self, dataField):
        """
        :param dataField: (Optional) 查询字段,支持 英文字母 数字 下划线 中划线 点（中文日志原文和各产品线的key）; 配置方式(SettingType) 为 空或visual 时，必填；
        """
        self.dataField = dataField

    def setFilterContent(self, filterContent):
        """
        :param filterContent: (Optional) 过滤语法，可以为空
        """
        self.filterContent = filterContent

    def setFilterOpen(self, filterOpen):
        """
        :param filterOpen: (Optional) 是否打开过滤; 配置方式(SettingType) 为 空或visual 时，必填；
        """
        self.filterOpen = filterOpen

    def setFilterType(self, filterType):
        """
        :param filterType: (Optional) 过滤类型，只能是fulltext和 advance; 配置方式(SettingType) 为 空或visual 时，必填；
        """
        self.filterType = filterType

    def setMetric(self, metric):
        """
        :param metric: (Optional) 监控项 , 支持大小写英文字母 下划线 数字 点，且不超过255byte（不支持中划线）; 配置方式(SettingType) 为 空或visual 时，必填；
        """
        self.metric = metric

    def setSettingType(self, settingType):
        """
        :param settingType: (Optional) 配置方式: 可选参数；枚举值 visual，sql；分别代表可视化配置及sql配置方式，传空表示可视化配置；
        """
        self.settingType = settingType

    def setSqlSpec(self, sqlSpec):
        """
        :param sqlSpec: (Optional) 
        """
        self.sqlSpec = sqlSpec

