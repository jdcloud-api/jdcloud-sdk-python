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


class CreateAsAlarmRequest(JDCloudRequest):
    """
    创建告警任务
- 所有参数取值为字符串类型的都严格区分大小写
- 伸缩功能关闭的情况下，不支持调用此接口
- 创建告警可以不选择简单伸缩规则，但是最终一个告警只允许关联一个简单规则和一个步进规则，步进规则优先级高于简单规则

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(CreateAsAlarmRequest, self).__init__(
            '/regions/{regionId}/asAlarms', 'POST', header, version)
        self.parameters = parameters


class CreateAsAlarmParameters(object):

    def __init__(self,regionId, agId, name, metricType, metricName, period, statistic, threshold, comparison, ):
        """
        :param regionId: 地域ID
        :param agId: 高可用组ID
        :param name: 名称，长度为1~32个字符，只允许中文、数字、大小写字母、英文下划线（_）、连字符（-）
        :param metricType: 监控项类型，取值范围：[`System`,`Custom`]
- `System`：系统监控项
- `Custom`：自定义监控项

        :param metricName: 监控项，云主机监控指标说明：https://docs.jdcloud.com/cn/monitoring/vm
目前支持的指标项如下:
- `cpu_util`: `CPU使用率`
- `memory.usage`: `内存使用率`
- `vm.disk.bytes.read`: `磁盘读吞吐量(host)`
- `vm.disk.bytes.write`: `磁盘写吞吐量(host)`
- `vm.network.bytes.incoming`: `网络进速率(host)`
- `vm.network.bytes.outgoing`: `网络出速率(host)`

        :param period: 监控项数据统计周期，单位分钟，取值范围：[`1`,`2`,`5`,`10`,`15`,`30`,`60`]
        :param statistic: 统计监控项数据的方法
- 系统监控取值范围：[`avg`,`max`,`min`]
- 自定义监控取值范围：[`avg`]

        :param threshold: 监控指标的阈值，必须大于0，阈值单位与监控项单位一致
        :param comparison: 对监控项阈值的判断方式，取值范围：[`gte`:`大于等于`,`lte`:`小于等于`,`gt`:`大于`,`lt`:`小于`]
        """

        self.regionId = regionId
        self.agId = agId
        self.name = name
        self.description = None
        self.metricType = metricType
        self.metricName = metricName
        self.namespace = None
        self.period = period
        self.statistic = statistic
        self.threshold = threshold
        self.comparison = comparison
        self.hitCount = None
        self.asRuleId = None

    def setDescription(self, description):
        """
        :param description: (Optional) 描述，最大长度为256个字符
        """
        self.description = description

    def setNamespace(self, namespace):
        """
        :param namespace: (Optional) 命名空间，当`metricType`为`Custom`，此参数必填
        """
        self.namespace = namespace

    def setHitCount(self, hitCount):
        """
        :param hitCount: (Optional) 触发告警需要满足阈值表达式的次数，默认为`3`，取值范围：[`1`,`2`,`3`,`5`,`10`,`15`,`30`,`60`]
        """
        self.hitCount = hitCount

    def setAsRuleId(self, asRuleId):
        """
        :param asRuleId: (Optional) 伸缩规则ID，可以为告警任务绑定伸缩规则，目前只支持 `asRuleType` 为 `Simple` 的伸缩规则
        """
        self.asRuleId = asRuleId

