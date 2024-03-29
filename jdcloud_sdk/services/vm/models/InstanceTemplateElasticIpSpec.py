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


class InstanceTemplateElasticIpSpec(object):

    def __init__(self, bandwidthMbps, chargeMode, provider=None):
        """
        :param bandwidthMbps:  弹性公网IP的带宽上限，单位：Mbps。
取值范围为：`[1-200]`。

        :param provider: (Optional) 弹性公网IP线路。中心可用区目前仅提供`BGP`类型IP。

        :param chargeMode:  弹性公网IP计费模式。可选值：
`bandwith`：按带宽计费。
`flow`：按流量计费。
若指定`chargeSpec=bandwith`则弹性公网IP计费类型同实例（包年包月或按配置）。边缘可用区目前仅支持`flow`计费模式。
        """

        self.bandwidthMbps = bandwidthMbps
        self.provider = provider
        self.chargeMode = chargeMode
