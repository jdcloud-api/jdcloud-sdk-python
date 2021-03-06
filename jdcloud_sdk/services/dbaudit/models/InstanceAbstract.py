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


class InstanceAbstract(object):

    def __init__(self, pin=None, insId=None, insName=None, insDesc=None, vpcId=None, subnetId=None, ipAddr=None, ipv6Addr=None, insType=None, state=None, expireTime=None, billingType=None, insZone=None, insRegion=None, insDomain=None, dbLimit=None):
        """
        :param pin: (Optional) PIN
        :param insId: (Optional) 实例ID
        :param insName: (Optional) 实例名称,长度限制32字节,允许英文字母,数字,下划线,中划线和中文
        :param insDesc: (Optional) 实例描述,长度限制128字节
        :param vpcId: (Optional) VPC-ID
        :param subnetId: (Optional) Subnet-ID
        :param ipAddr: (Optional) VPC内地址
        :param ipv6Addr: (Optional) VPC内ipv6地址
        :param insType: (Optional) 实例规格: basic:标准版 professional:企业版 enterprise:增强版 ultimate:旗舰版
        :param state: (Optional) 实例状态: 1->创建中, 2->运行中, 3->已停止, 4->已欠费停服, 5->已删除, 6->异常
        :param expireTime: (Optional) 计费到期时间
        :param billingType: (Optional) 计费类型 1:按配置 2: 按用量 3:包年包月 4:一次性
        :param insZone: (Optional) 可用区
        :param insRegion: (Optional) 地域
        :param insDomain: (Optional) 域名
        :param dbLimit: (Optional) 数据库限额
        """

        self.pin = pin
        self.insId = insId
        self.insName = insName
        self.insDesc = insDesc
        self.vpcId = vpcId
        self.subnetId = subnetId
        self.ipAddr = ipAddr
        self.ipv6Addr = ipv6Addr
        self.insType = insType
        self.state = state
        self.expireTime = expireTime
        self.billingType = billingType
        self.insZone = insZone
        self.insRegion = insRegion
        self.insDomain = insDomain
        self.dbLimit = dbLimit
