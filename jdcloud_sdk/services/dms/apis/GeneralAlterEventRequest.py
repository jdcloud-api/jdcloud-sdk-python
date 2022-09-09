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


class GeneralAlterEventRequest(JDCloudRequest):
    """
    生成修改事件sql语句，支持Mysql
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(GeneralAlterEventRequest, self).__init__(
            '/regions/{regionId}/event:generalAlter', 'POST', header, version)
        self.parameters = parameters


class GeneralAlterEventParameters(object):

    def __init__(self,regionId, ):
        """
        :param regionId: 地域代码，取值范围参见[《各地域及可用区对照表》](../Enum-Definitions/Regions-AZ.md)
        """

        self.regionId = regionId
        self.dataSourceId = None
        self.dbName = None
        self.originEventName = None
        self.eventName = None
        self.eventComment = None
        self.eventStatus = None
        self.isPreserve = None
        self.eventDefinition = None
        self.eventType = None
        self.executeAt = None
        self.intervalValue = None
        self.intervalField = None
        self.starts = None
        self.ends = None

    def setDataSourceId(self, dataSourceId):
        """
        :param dataSourceId: (Optional) 数据源id。
        """
        self.dataSourceId = dataSourceId

    def setDbName(self, dbName):
        """
        :param dbName: (Optional) 数据库名称。
        """
        self.dbName = dbName

    def setOriginEventName(self, originEventName):
        """
        :param originEventName: (Optional) 原始事件名称。
        """
        self.originEventName = originEventName

    def setEventName(self, eventName):
        """
        :param eventName: (Optional) 新事件名称。
        """
        self.eventName = eventName

    def setEventComment(self, eventComment):
        """
        :param eventComment: (Optional) 注释。
        """
        self.eventComment = eventComment

    def setEventStatus(self, eventStatus):
        """
        :param eventStatus: (Optional) 状态，ENABLED,DISABLED, SLAVESIDE_DISABLED。
        """
        self.eventStatus = eventStatus

    def setIsPreserve(self, isPreserve):
        """
        :param isPreserve: (Optional) 完成后是否保存。
        """
        self.isPreserve = isPreserve

    def setEventDefinition(self, eventDefinition):
        """
        :param eventDefinition: (Optional) 事件定义。
        """
        self.eventDefinition = eventDefinition

    def setEventType(self, eventType):
        """
        :param eventType: (Optional) 调度方式，ONE_TIME,RECURRING。
        """
        self.eventType = eventType

    def setExecuteAt(self, executeAt):
        """
        :param executeAt: (Optional) 执行一次的时间。
        """
        self.executeAt = executeAt

    def setIntervalValue(self, intervalValue):
        """
        :param intervalValue: (Optional) 循环执行时间隔时间的值。
        """
        self.intervalValue = intervalValue

    def setIntervalField(self, intervalField):
        """
        :param intervalField: (Optional) 循环执行时间隔时间的单位，YEAR,QUARTER,MONTH,WEEK,DAY,HOUR,MINUTE,SECOND,YEAR_MONTH,DAY_HOUR,DAY_MINUTE,DAY_SECOND,HOUR_MINUTE,HOUR_SECOND,MINUTE_SECOND。
        """
        self.intervalField = intervalField

    def setStarts(self, starts):
        """
        :param starts: (Optional) 循环执行开始时间。
        """
        self.starts = starts

    def setEnds(self, ends):
        """
        :param ends: (Optional) 循环执行结束时间。
        """
        self.ends = ends

