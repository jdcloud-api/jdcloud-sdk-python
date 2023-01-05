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


class InstanceTemplateData(object):

    def __init__(self, instanceType=None, vpcId=None, imageId=None, includePassword=None, systemDisk=None, dataDisks=None, primaryNetworkInterface=None, elasticIp=None, keyNames=None, chargeOnStopped=None, autoImagePolicyId=None, passwordAuth=None, imageInherit=None, burstInfo=None, instanceTags=None):
        """
        :param instanceType: (Optional) 实例规格。
        :param vpcId: (Optional) 主网卡所属VPC的ID。
        :param imageId: (Optional) 云主机使用的镜像ID。
        :param includePassword: (Optional) 实例模板中是否包含自定义密码。`true`：包含自定义密码，`false`：不包含自定义密码。
        :param systemDisk: (Optional) 系统盘配置。
        :param dataDisks: (Optional) 数据盘配置列表。
        :param primaryNetworkInterface: (Optional) 主网卡配置。
        :param elasticIp: (Optional) 主网卡主IP关联的弹性公网IP配置。
        :param keyNames: (Optional) 云主机使用的密钥对名称。
        :param chargeOnStopped: (Optional) 停机不计费模式。该参数仅对按配置计费且系统盘为云硬盘的实例生效，并且不是专有宿主机中的实例。
`keepCharging`：关机后继续计费。
`stopCharging`：关机后停止计费。

        :param autoImagePolicyId: (Optional) 自动任务策略ID。
        :param passwordAuth: (Optional) 允许SSH密码登录。
`yes`：允许SSH密码登录。
`no`：禁止SSH密码登录。
仅在指定密钥时此参数有效，指定此参数后密码即使输入也将被忽略，同时会在系统内禁用SSH密码登录。

        :param imageInherit: (Optional) 使用镜像中的登录凭证，无须再指定密码或密钥（指定无效）。
`yes`：使用镜像登录凭证。
`no`：不使用镜像登录凭证。
仅使用私有或共享镜像时此参数有效。

        :param burstInfo: (Optional) 突发型实例参数信息
        :param instanceTags: (Optional) 自定义实例标签。
        """

        self.instanceType = instanceType
        self.vpcId = vpcId
        self.imageId = imageId
        self.includePassword = includePassword
        self.systemDisk = systemDisk
        self.dataDisks = dataDisks
        self.primaryNetworkInterface = primaryNetworkInterface
        self.elasticIp = elasticIp
        self.keyNames = keyNames
        self.chargeOnStopped = chargeOnStopped
        self.autoImagePolicyId = autoImagePolicyId
        self.passwordAuth = passwordAuth
        self.imageInherit = imageInherit
        self.burstInfo = burstInfo
        self.instanceTags = instanceTags
