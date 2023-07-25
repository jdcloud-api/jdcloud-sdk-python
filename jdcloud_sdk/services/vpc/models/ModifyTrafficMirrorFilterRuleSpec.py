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


class ModifyTrafficMirrorFilterRuleSpec(object):

    def __init__(self, mirrorFilterRuleId, direction=None, protocol=None, action=None, priority=None, sourceCidr=None, destinationCidr=None, sourcePortStart=None, sourcePortEnd=None, destinationPortStart=None, destinationPortEnd=None):
        """
        :param mirrorFilterRuleId:  过滤器规则的ID
        :param direction: (Optional) 规则方向ingress为入站、egress为出站
        :param protocol: (Optional) 协议：ICMP，ICMPv6，TCP，UDP，ALL：表示选择所有协议和所有端口；TCP和UDP时需要输入Port
        :param action: (Optional) 访问控制策略：accept:接受，drop：拒绝
        :param priority: (Optional) 规则优先级1~32768（值越小优先级越高），相同direction内的优先级不能相同
        :param sourceCidr: (Optional) 规则作用的源IP的CIDR，输入格式为x.x.x.x/x，合法的IPv4、IPv6地址段
        :param destinationCidr: (Optional) 规则作用的目的IP的CIDR，输入格式为x.x.x.x/x，合法的IPv4、IPv6地址段
        :param sourcePortStart: (Optional) 若protocal是UDP、TCP，必须，范围1-65535，start必须小于等于end
        :param sourcePortEnd: (Optional) 若protocal是UDP、TCP，必须，范围1-65535，start必须小于等于end
        :param destinationPortStart: (Optional) 若protocal是UDP、TCP，必须，范围1-65535，start必须小于等于end
        :param destinationPortEnd: (Optional) 若protocal是UDP、TCP，必须，范围1-65535，start必须小于等于end.
        """

        self.mirrorFilterRuleId = mirrorFilterRuleId
        self.direction = direction
        self.protocol = protocol
        self.action = action
        self.priority = priority
        self.sourceCidr = sourceCidr
        self.destinationCidr = destinationCidr
        self.sourcePortStart = sourcePortStart
        self.sourcePortEnd = sourcePortEnd
        self.destinationPortStart = destinationPortStart
        self.destinationPortEnd = destinationPortEnd
