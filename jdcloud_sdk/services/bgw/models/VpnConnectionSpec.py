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


class VpnConnectionSpec(object):

    def __init__(self, vpnConnectionName, bgwId, cgwId, description=None, bgpEnabled=None, localAsn=None, providers=None, chargeSpec=None):
        """
        :param vpnConnectionName:  VPN连接的名称,只允许输入中文、数字、大小写字母、英文下划线“_”及中划线“-”，不允许为空且不超过32字符。
        :param description: (Optional) VPN连接的描述，允许输入UTF-8编码下的全部字符，不超过256字符。
        :param bgwId:  边界网关的Id
        :param cgwId:  客户网关的Id
        :param bgpEnabled: (Optional) “是否使用BGP路由，取值范围为：false（不使能）、true（使能），默认为：true”
        :param localAsn: (Optional) 本地的BGP ASN号，支持16位的私有ASN，取值范围为：64512~65534，默认从BGW继承65000
        :param providers: (Optional) VPN连接的2个公网IP线路信息。当BGW为标准BGW时，忽略此参数。当BGW为边缘BGW时，可配置2个公网IP线路，其值可通过调用describeEdgeIpProviders获取不同边缘节点的边缘公网IP线路信息，不指定provider时，系统会自动选择describeEdgeIpProviders获取的此边缘节点第1顺序的线路作为第1个provider，边缘节点第2顺序的线路作为第2个provider，特殊情况：当获取的线路只有1个时，provider2=provider1
        :param chargeSpec: (Optional) 计费配置，仅支持按用量，默认按用量
        """

        self.vpnConnectionName = vpnConnectionName
        self.description = description
        self.bgwId = bgwId
        self.cgwId = cgwId
        self.bgpEnabled = bgpEnabled
        self.localAsn = localAsn
        self.providers = providers
        self.chargeSpec = chargeSpec
