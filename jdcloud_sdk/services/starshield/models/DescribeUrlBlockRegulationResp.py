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


class DescribeUrlBlockRegulationResp(object):

    def __init__(self, id=None, userPin=None, regulationName=None, blockUrl=None, zoneId=None, filterId=None, firewallRuleId=None, opType=None, enableRegulation=None, createTime=None, createUser=None, updateTime=None, updateUser=None):
        """
        :param id: (Optional) 封禁URL规则id
        :param userPin: (Optional) url对应的用户pin
        :param regulationName: (Optional) 封禁URL规则名称
        :param blockUrl: (Optional) 封禁的url
        :param zoneId: (Optional) zone id
        :param filterId: (Optional) filter id
        :param firewallRuleId: (Optional) firewall rule id
        :param opType: (Optional) 操作类型(0->阻断)
        :param enableRegulation: (Optional) 规则开启状态(0->关闭  1->开启)
        :param createTime: (Optional) 规则创建时间
        :param createUser: (Optional) 规则创建者
        :param updateTime: (Optional) 规则更新时间
        :param updateUser: (Optional) 规则更新者
        """

        self.id = id
        self.userPin = userPin
        self.regulationName = regulationName
        self.blockUrl = blockUrl
        self.zoneId = zoneId
        self.filterId = filterId
        self.firewallRuleId = firewallRuleId
        self.opType = opType
        self.enableRegulation = enableRegulation
        self.createTime = createTime
        self.createUser = createUser
        self.updateTime = updateTime
        self.updateUser = updateUser
