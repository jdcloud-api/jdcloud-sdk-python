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


class CreateInstanceSpec(object):

    def __init__(self, buyType, carrier, bp, ep, bw, id=None, name=None, ipType=None, ipCount=None, portCount=None, domainCount=None, timeSpan=None, timeUnit=None, returnUrl=None):
        """
        :param id: (Optional) 实例 Id, 升级时必传
        :param name: (Optional) 实例名称, 新购时必传
        :param buyType:  购买类型. <br>- 1: 新购<br>- 3: 升级
        :param carrier:  链路类型. <br>- 3: 电信、联通和移动<br>- 4: BGP 线路
        :param ipType: (Optional) 可防护 ip 类型, 目前仅电信线路支持 IPV6 线路<br>- 0: IPV4,<br>- 1: IPV4/IPV6
        :param ipCount: (Optional) IP 数量
        :param portCount: (Optional) 可配的转发端口数量
        :param domainCount: (Optional) 可配的网站规则域名数量
        :param bp:  保底带宽: 单位 Gbps
        :param ep:  弹性带宽: 单位 Gbps
        :param bw:  业务带宽: 单位 Mbps
        :param timeSpan: (Optional) 购买时长, 新购高防实例时必传<br>- timeUnit 为 3 时, 可取值 1-9<br>- timeUnit 为 4 时, 可取值 1-3
        :param timeUnit: (Optional) 购买时长类型, 新购高防实例时必传<br>- 3: 月<br>- 4: 年
        :param returnUrl: (Optional) 支付成功后跳转的页面, 控制台交互模式传该字段
        """

        self.id = id
        self.name = name
        self.buyType = buyType
        self.carrier = carrier
        self.ipType = ipType
        self.ipCount = ipCount
        self.portCount = portCount
        self.domainCount = domainCount
        self.bp = bp
        self.ep = ep
        self.bw = bw
        self.timeSpan = timeSpan
        self.timeUnit = timeUnit
        self.returnUrl = returnUrl
