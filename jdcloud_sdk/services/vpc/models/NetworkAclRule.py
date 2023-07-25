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


class NetworkAclRule(object):

    def __init__(self, ruleId=None, protocol=None, fromPort=None, toPort=None, direction=None, addressPrefix=None, ruleAction=None, priority=None, description=None, createdTime=None, ruleType=None):
        """
        :param ruleId: (Optional) networkAcl规则ID
        :param protocol: (Optional) 规则限定协议。取值范围：All,TCP,UDP,ICMP
        :param fromPort: (Optional) 规则限定起始传输层端口, 取值范围:1-65535, 若protocol为传输层协议，默认值为1，若protocol不是传输层协议，设置无效，恒为0。如果规则只限定一个端口号，fromPort和toPort填写同一个值
        :param toPort: (Optional) 规则限定终止传输层端口, 取值范围:1-65535, 若protocol为传输层协议，默认值为65535，若protocol不是传输层协议，设置无效，恒为0。如果规则只限定一个端口号，fromPort和toPort填写同一个值
        :param direction: (Optional) networkAcl规则方向。ingress：入规则; egress：出规则
        :param addressPrefix: (Optional) 匹配地址前缀
        :param ruleAction: (Optional) 访问控制策略：allow:允许，deny：拒绝
        :param priority: (Optional) 规则匹配优先级，取值范围为[1,32768]，优先级数字越小优先级越高
        :param description: (Optional) 描述,允许输入UTF-8编码下的全部字符，不超过256字符
        :param createdTime: (Optional) networkAclRule创建时间
        :param ruleType: (Optional) 规则类型，default：默认规则，custom：自定义规则，service：服务创建规则
        """

        self.ruleId = ruleId
        self.protocol = protocol
        self.fromPort = fromPort
        self.toPort = toPort
        self.direction = direction
        self.addressPrefix = addressPrefix
        self.ruleAction = ruleAction
        self.priority = priority
        self.description = description
        self.createdTime = createdTime
        self.ruleType = ruleType
