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


class CreateTargetAsRuleSpec(object):

    def __init__(self, metricName, targetValue, scaleOutHitCount=None, scaleInHitCount=None):
        """
        :param metricName:  目标跟踪的监控项，云主机监控指标说明：https://docs.jdcloud.com/cn/monitoring/vm
目前支持的指标项如下:
- `cpu_util`: `CPU使用率`
- `memory.usage`: `内存使用率`
- `vm.disk.bytes.read`: `磁盘读吞吐量(host)`
- `vm.disk.bytes.write`: `磁盘写吞吐量(host)`
- `vm.network.bytes.incoming`: `网络进速率(host)`
- `vm.network.bytes.outgoing`: `网络出速率(host)`

        :param targetValue:  目标跟踪的目标值，必须大于0
        :param scaleOutHitCount: (Optional) 扩容报警触发的阈值次数，默认为`3`，必须大于0
        :param scaleInHitCount: (Optional) 缩容报警触发的阈值次数，默认为`15`，必须大于0
        """

        self.metricName = metricName
        self.targetValue = targetValue
        self.scaleOutHitCount = scaleOutHitCount
        self.scaleInHitCount = scaleInHitCount
