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


class AutoscalingSpec(object):

    def __init__(self, minSize, maxSize, desiredCapacity=None, healthCheck=None, coolDownSeconds=None, scalingPolicy=None, removalPolicy=None):
        """
        :param minSize:  伸缩组最小实例数，取值范围为0-300。若高可用组分散策略为host或、switch，组内最小实例数不能大于组quota限制
        :param maxSize:  伸缩组最大实例数，取值范围为0-300。若高可用组分散策略为host或、switch，组内最大实例数不能大于组quota限制
        :param desiredCapacity: (Optional) 伸缩组期望实例数，取值范围为：[最小实例数，最大实例数]
        :param healthCheck: (Optional) 伸缩组内实例是否需要健康检查，默认是开启
        :param coolDownSeconds: (Optional) 冷却时间，默认值为300（单位为秒）,范围为0-86400（24小时）
        :param scalingPolicy: (Optional) 默认值为均衡分布，Balance，当前仅支持这个值
        :param removalPolicy: (Optional) 实例移出策略，默认值为最早创建的实例,支持：OldestResource（最早创建实例）,NewestResource（最新创建实例）
        """

        self.minSize = minSize
        self.maxSize = maxSize
        self.desiredCapacity = desiredCapacity
        self.healthCheck = healthCheck
        self.coolDownSeconds = coolDownSeconds
        self.scalingPolicy = scalingPolicy
        self.removalPolicy = removalPolicy
