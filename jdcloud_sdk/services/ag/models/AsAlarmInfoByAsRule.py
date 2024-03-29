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


class AsAlarmInfoByAsRule(object):

    def __init__(self, asAlarmId=None, name=None, description=None, metricType=None, metricName=None, namespace=None, period=None, statistic=None, threshold=None, comparison=None, hitCount=None, createTime=None, updateTime=None, state=None):
        """
        :param asAlarmId: (Optional) 告警任务ID
        :param name: (Optional) 告警任务名称
        :param description: (Optional) 告警任务描述
        :param metricType: (Optional) 监控项类型，取值范围：[`System`,`Custom`]
        :param metricName: (Optional) 监控项，云主机监控指标说明：https://docs.jdcloud.com/cn/monitoring/vm
目前支持的指标项如下:
- `cpu_util`: `CPU使用率`
- `memory.usage`: `内存使用率`
- `vm.disk.bytes.read`: `磁盘读吞吐量(host)`
- `vm.disk.bytes.write`: `磁盘写吞吐量(host)`
- `vm.network.bytes.incoming`: `网络进速率(host)`
- `vm.network.bytes.outgoing`: `网络出速率(host)`

        :param namespace: (Optional) 命名空间，仅当`metricType`为`Custom`时返回
        :param period: (Optional) 监控项数据统计周期，单位分钟，取值范围：[`1`,`2`,`5`,`10`,`15`,`30`,`60`]
        :param statistic: (Optional) 统计监控项数据的方法
- 系统监控取值范围：[`avg`,`max`,`min`]
- 自定义监控取值范围：[`avg`]

        :param threshold: (Optional) 监控指标的阈值，必须大于0，阈值单位与监控项单位一致
        :param comparison: (Optional) 对监控项阈值的判断方式，取值范围：[`gte`:`大于等于`,`lte`:`小于等于`,`gt`:`大于`,`lt`:`小于`]
        :param hitCount: (Optional) 触发告警需要满足阈值表达式的次数，默认为`3`，取值范围：[`1`,`2`,`3`,`5`,`10`,`15`,`30`,`60`]
        :param createTime: (Optional) 创建时间
        :param updateTime: (Optional) 更新时间
        :param state: (Optional) 告警任务状态，取值范围如下：
- `Disabled`：已禁用
- `Normal`：正常
- `DataMissing`：监控数据不足
- `Alarm`：告警中

        """

        self.asAlarmId = asAlarmId
        self.name = name
        self.description = description
        self.metricType = metricType
        self.metricName = metricName
        self.namespace = namespace
        self.period = period
        self.statistic = statistic
        self.threshold = threshold
        self.comparison = comparison
        self.hitCount = hitCount
        self.createTime = createTime
        self.updateTime = updateTime
        self.state = state
