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


class AzIpSpec(object):

    def __init__(self, az, bandwidthMbps, provider=None, ipCharge=None):
        """
        :param provider: (Optional) IP线路类型，仅支持bgp，默认值bgp
        :param az:  公网IP可用区属性
        :param bandwidthMbps:  NAT网关公网IP的限速（单位：Mbps）。计费类型为按配置时，取值范围为[1-1000]；计费类型为按流量时，取值范围为[1-200]
        :param ipCharge: (Optional) 计费配置,支持按配置、按用量，默认按配置
        """

        self.provider = provider
        self.az = az
        self.bandwidthMbps = bandwidthMbps
        self.ipCharge = ipCharge
