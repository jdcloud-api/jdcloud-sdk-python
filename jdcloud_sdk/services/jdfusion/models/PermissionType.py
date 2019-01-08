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


class PermissionType(object):

    def __init__(self, cloudID=None, ipProtocol=None, portRange=None, description=None, sourceCidrIp=None, sourceGroupId=None, sourceGroupOwnerAccount=None, destCidrIp=None, destGroupId=None, destGroupOwnerAccount=None, policy=None, nicType=None, priority=None, direction=None):
        """
        :param cloudID: (Optional) 云注册信息ID
        :param ipProtocol: (Optional) IP协议
        :param portRange: (Optional) 端口范围
        :param description: (Optional) 描述信息
        :param sourceCidrIp: (Optional) 源IP地址段，用于入方向授权
        :param sourceGroupId: (Optional) 源安全组，用于入方向授权
        :param sourceGroupOwnerAccount: (Optional) 源安全组所属阿里云账户Id
        :param destCidrIp: (Optional) 目标IP地址段，用于出方向授权
        :param destGroupId: (Optional) 目标安全组，用于出方向授权
        :param destGroupOwnerAccount: (Optional) 目标安全组所属阿里云账户Id
        :param policy: (Optional) 授权策略
        :param nicType: (Optional) 网络类型
        :param priority: (Optional) 规则优先级
        :param direction: (Optional) 授权方向
        """

        self.cloudID = cloudID
        self.ipProtocol = ipProtocol
        self.portRange = portRange
        self.description = description
        self.sourceCidrIp = sourceCidrIp
        self.sourceGroupId = sourceGroupId
        self.sourceGroupOwnerAccount = sourceGroupOwnerAccount
        self.destCidrIp = destCidrIp
        self.destGroupId = destGroupId
        self.destGroupOwnerAccount = destGroupOwnerAccount
        self.policy = policy
        self.nicType = nicType
        self.priority = priority
        self.direction = direction