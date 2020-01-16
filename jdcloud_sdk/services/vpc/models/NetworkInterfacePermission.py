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


class NetworkInterfacePermission(object):

    def __init__(self, networkInterfacePermissionId=None, networkInterfaceOwner=None, trustUser=None, networkInterfaceId=None, policy=None, createdTime=None):
        """
        :param networkInterfacePermissionId: (Optional) 弹性网卡授权ID
        :param networkInterfaceOwner: (Optional) 弹性网卡所属用户
        :param trustUser: (Optional) 授信用户
        :param networkInterfaceId: (Optional) 弹性网卡ID
        :param policy: (Optional) 授权策略, 授权后，该弹性网卡可以关联的服务端账号的资源类型，取值范围，instance-attach：可以关联服务端账号的实例资源，eip-associate：可以关联服务端账号的弹性公网IP资源
        :param createdTime: (Optional) 弹性网卡授权创建时间
        """

        self.networkInterfacePermissionId = networkInterfacePermissionId
        self.networkInterfaceOwner = networkInterfaceOwner
        self.trustUser = trustUser
        self.networkInterfaceId = networkInterfaceId
        self.policy = policy
        self.createdTime = createdTime