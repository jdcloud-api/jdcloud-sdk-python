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


class UpdateAsAlarmRequest(JDCloudRequest):
    """
    修改告警任务
- 所有参数取值为字符串类型的都严格区分大小写
- 所有告警任务不允许修改高可用组
- 所有告警任务不允许修改监控类型
- 目标跟踪规则生成的告警任务不允许修改任何内容
- 监控类型为自定义监控的告警任务不允许修改命名空间
- 步进规则绑定的告警任务不允许修改报警指标相关内容
- 所有参数都为非必传，但是至少需要传入一个参数，否则报错
- 伸缩功能开启或者关闭的情况下，都支持调用此接口

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(UpdateAsAlarmRequest, self).__init__(
            '/regions/{regionId}/asAlarms/{asAlarmId}', 'POST', header, version)
        self.parameters = parameters


class UpdateAsAlarmParameters(object):

    def __init__(self,regionId, asAlarmId, ):
        """
        :param regionId: 地域ID
        :param asAlarmId: 告警任务ID
        """

        self.regionId = regionId
        self.asAlarmId = asAlarmId
        self.name = None
        self.description = None
        self.metricName = None
        self.period = None
        self.statistic = None
        self.threshold = None
        self.comparison = None
        self.hitCount = None
        self.asRuleId = None

    def setName(self, name):
        """
        :param name: (Optional) 名称，长度为1~32个字符，只允许中文、数字、大小写字母、英文下划线（_）、连字符（-）
        """
        self.name = name

    def setDescription(self, description):
        """
        :param description: (Optional) 描述，最大长度为256个字符
        """
        self.description = description

    def setMetricName(self, metricName):
        """
        :param metricName: (Optional) 监控项，云主机监控指标说明：https://docs.jdcloud.com/cn/monitoring/vm
目前支持的指标项如下:
- `cpu_util`: `CPU使用率`
- `memory.usage`: `内存使用率`
- `vm.disk.bytes.read`: `磁盘读吞吐量(host)`
- `vm.disk.bytes.write`: `磁盘写吞吐量(host)`
- `vm.network.bytes.incoming`: `网络进速率(host)`
- `vm.network.bytes.outgoing`: `网络出速率(host)`

        """
        self.metricName = metricName

    def setPeriod(self, period):
        """
        :param period: (Optional) 监控项数据统计周期，单位分钟，取值范围：[`1`,`2`,`5`,`10`,`15`,`30`,`60`]
        """
        self.period = period

    def setStatistic(self, statistic):
        """
        :param statistic: (Optional) 统计监控项数据的方法
- 系统监控取值范围：[`avg`,`max`,`min`]
- 自定义监控取值范围：[`avg`]

        """
        self.statistic = statistic

    def setThreshold(self, threshold):
        """
        :param threshold: (Optional) 监控指标的阈值，必须大于0，阈值单位与监控项单位一致
        """
        self.threshold = threshold

    def setComparison(self, comparison):
        """
        :param comparison: (Optional) 对监控项阈值的判断方式，取值范围：[`gte`:`大于等于`,`lte`:`小于等于`,`gt`:`大于`,`lt`:`小于`]
        """
        self.comparison = comparison

    def setHitCount(self, hitCount):
        """
        :param hitCount: (Optional) 触发告警需要满足阈值表达式的次数，取值范围：[`1`,`2`,`3`,`5`,`10`,`15`,`30`,`60`]
        """
        self.hitCount = hitCount

    def setAsRuleId(self, asRuleId):
        """
        :param asRuleId: (Optional) 伸缩规则ID，更新告警任务关联的伸缩规则，目前只支持 `asRuleType` 为 `Simple` 的伸缩规则
        """
        self.asRuleId = asRuleId

