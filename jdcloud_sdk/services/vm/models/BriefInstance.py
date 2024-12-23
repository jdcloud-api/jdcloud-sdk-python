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


class BriefInstance(object):

    def __init__(self, instanceId=None, instanceName=None, instanceType=None, vpcId=None, subnetId=None, privateIpAddress=None, status=None, description=None, imageId=None, systemDisk=None, dataDisks=None, primaryNetworkInterface=None, secondaryNetworkInterfaces=None, launchTime=None, az=None, pAz=None, keyNames=None, faultDomain=None, chargeOnStopped=None, dedicatedPoolId=None, dedicatedHostId=None, cpuTopology=None, bootMode=None, autoReleaseTime=None):
        """
        :param instanceId: (Optional) 云主机ID。
        :param instanceName: (Optional) 云主机名称。
        :param instanceType: (Optional) 实例规格。
        :param vpcId: (Optional) 主网卡所属VPC的ID。
        :param subnetId: (Optional) 主网卡所属子网的ID。
        :param privateIpAddress: (Optional) 主网卡主内网IP地址。
        :param status: (Optional) 云主机状态，参考 [云主机状态](https://docs.jdcloud.com/virtual-machines/api/vm_status)。
        :param description: (Optional) 云主机描述。
        :param imageId: (Optional) 云主机使用的镜像ID。
        :param systemDisk: (Optional) 系统盘配置。
        :param dataDisks: (Optional) 数据盘配置列表。
        :param primaryNetworkInterface: (Optional) 主网卡配置。
        :param secondaryNetworkInterfaces: (Optional) 辅助网卡配置列表。
        :param launchTime: (Optional) 云主机实例的创建时间。
        :param az: (Optional) 云主机所在可用区。
        :param pAz: (Optional) 云主机所在逻辑可用区。
        :param keyNames: (Optional) 云主机使用的密钥对名称。
        :param faultDomain: (Optional) 高可用组中的错误域。
        :param chargeOnStopped: (Optional) 关机模式，只支持云盘做系统盘的按配置计费云主机。
`keepCharging`：关机后继续计费。
`stopCharging`：关机后停止计费。

        :param dedicatedPoolId: (Optional) 云主机所属的专有宿主机池。
        :param dedicatedHostId: (Optional) 云主机所属的专有宿主机ID。
        :param cpuTopology: (Optional) 虚机CPU拓扑
        :param bootMode: (Optional) 启动模式支持，取值范围[bios uefi]。
        :param autoReleaseTime: (Optional) 定时删除时间，例如:"2025-01-01 00:00:00"。
        """

        self.instanceId = instanceId
        self.instanceName = instanceName
        self.instanceType = instanceType
        self.vpcId = vpcId
        self.subnetId = subnetId
        self.privateIpAddress = privateIpAddress
        self.status = status
        self.description = description
        self.imageId = imageId
        self.systemDisk = systemDisk
        self.dataDisks = dataDisks
        self.primaryNetworkInterface = primaryNetworkInterface
        self.secondaryNetworkInterfaces = secondaryNetworkInterfaces
        self.launchTime = launchTime
        self.az = az
        self.pAz = pAz
        self.keyNames = keyNames
        self.faultDomain = faultDomain
        self.chargeOnStopped = chargeOnStopped
        self.dedicatedPoolId = dedicatedPoolId
        self.dedicatedHostId = dedicatedHostId
        self.cpuTopology = cpuTopology
        self.bootMode = bootMode
        self.autoReleaseTime = autoReleaseTime
