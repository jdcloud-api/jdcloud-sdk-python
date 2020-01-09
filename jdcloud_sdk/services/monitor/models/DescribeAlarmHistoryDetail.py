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


class DescribeAlarmHistoryDetail(object):

    def __init__(self, alarmId=None, dimension=None, durationTimes=None, namespace=None, namespaceName=None, noticeDurationTime=None, noticeLevelTriggered=None, noticeTime=None, receivers=None, region=None, rule=None, status=None, value=None):
        """
        :param alarmId: (Optional) 报警规则ID
        :param dimension: (Optional) 资源维度
        :param durationTimes: (Optional) 告警持续次数
        :param namespace: (Optional) 命名空间
        :param namespaceName: (Optional) 命名空间名称
        :param noticeDurationTime: (Optional) 告警持续时间，单位分钟
        :param noticeLevelTriggered: (Optional) 触发的告警级别。从低到高分别为‘common’, ‘critical’, ‘fatal’
        :param noticeTime: (Optional) 告警时间
        :param receivers: (Optional) 告警通知人
        :param region: (Optional) 规则绑定资源所在地域
        :param rule: (Optional) 
        :param status: (Optional) 告警类型  1-告警恢复  2-告警 4-数据不足
        :param value: (Optional) 告警值
        """

        self.alarmId = alarmId
        self.dimension = dimension
        self.durationTimes = durationTimes
        self.namespace = namespace
        self.namespaceName = namespaceName
        self.noticeDurationTime = noticeDurationTime
        self.noticeLevelTriggered = noticeLevelTriggered
        self.noticeTime = noticeTime
        self.receivers = receivers
        self.region = region
        self.rule = rule
        self.status = status
        self.value = value
