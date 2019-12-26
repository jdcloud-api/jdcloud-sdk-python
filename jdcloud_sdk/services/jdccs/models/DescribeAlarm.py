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


class DescribeAlarm(object):

    def __init__(self, alarmId=None, name=None, idc=None, idcName=None, resourceType=None, resourceId=None, resourceName=None, metric=None, metricName=None, period=None, statisticMethod=None, operator=None, threshold=None, times=None, noticePeriod=None, status=None, switchboard=None):
        """
        :param alarmId: (Optional) 规则实例ID
        :param name: (Optional) 规则名称
        :param idc: (Optional) 机房英文标识
        :param idcName: (Optional) 机房名称
        :param resourceType: (Optional) 资源类型 bandwidth:带宽
        :param resourceId: (Optional) 资源ID
        :param resourceName: (Optional) 资源名称
        :param metric: (Optional) 监控项英文标识
        :param metricName: (Optional) 监控项名称
        :param period: (Optional) 统计周期（单位：分钟）
        :param statisticMethod: (Optional) 统计方法：平均值=avg、最大值=max、最小值=min
        :param operator: (Optional) 计算方式 >=、>、<、<=、=、！=
        :param threshold: (Optional) 阈值
        :param times: (Optional) 连续多少次后报警
        :param noticePeriod: (Optional) 通知周期 单位：小时
        :param status: (Optional) 规则状态 disabled:禁用 enabled:启用
        :param switchboard: (Optional) 
        """

        self.alarmId = alarmId
        self.name = name
        self.idc = idc
        self.idcName = idcName
        self.resourceType = resourceType
        self.resourceId = resourceId
        self.resourceName = resourceName
        self.metric = metric
        self.metricName = metricName
        self.period = period
        self.statisticMethod = statisticMethod
        self.operator = operator
        self.threshold = threshold
        self.times = times
        self.noticePeriod = noticePeriod
        self.status = status
        self.switchboard = switchboard
