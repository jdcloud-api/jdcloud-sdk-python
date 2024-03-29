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


class Container(object):

    def __init__(self, containerId=None, status=None, instanceType=None, az=None, name=None, hostAliases=None, hostname=None, ag=None, command=None, args=None, envs=None, image=None, secret=None, tty=None, workingDir=None, rootVolume=None, dataVolumes=None, vpcId=None, subnetId=None, privateIpAddress=None, elasticIpId=None, elasticIpAddress=None, primaryNetworkInterface=None, secondaryNetworkInterfaces=None, logConfiguration=None, tags=None, charge=None, launchTime=None, reason=None, description=None, resourceGroupId=None):
        """
        :param containerId: (Optional) 容器ID
        :param status: (Optional) 容器状态
        :param instanceType: (Optional) 实例类型
        :param az: (Optional) 可用区
        :param name: (Optional) 容器名称
        :param hostAliases: (Optional) 域名和IP映射的信息
        :param hostname: (Optional) 主机名
        :param ag: (Optional) 高可用组
        :param command: (Optional) 容器执行命令
        :param args: (Optional) 容器执行命令的参数
        :param envs: (Optional) 动态指定的容器执行的环境变量
        :param image: (Optional) 镜像名称
        :param secret: (Optional) 镜像仓库认证信息名称
        :param tty: (Optional) 容器是否分配tty
        :param workingDir: (Optional) 容器的工作目录
        :param rootVolume: (Optional) 根Volume信息
        :param dataVolumes: (Optional) 挂载的数据Volume信息
        :param vpcId: (Optional) 主网卡所属VPC的ID
        :param subnetId: (Optional) 主网卡所属子网的ID
        :param privateIpAddress: (Optional) 主网卡主IP地址
        :param elasticIpId: (Optional) 主网卡主IP绑定弹性IP的ID
        :param elasticIpAddress: (Optional) 主网卡主IP绑定弹性IP的地址
        :param primaryNetworkInterface: (Optional) 主网卡配置信息
        :param secondaryNetworkInterfaces: (Optional) 辅助网卡配置信息
        :param logConfiguration: (Optional) 容器日志配置信息
        :param tags: (Optional) 
        :param charge: (Optional) 计费配置信息
        :param launchTime: (Optional) 创建时间
        :param reason: (Optional) 容器终止原因
        :param description: (Optional) 容器描述
        :param resourceGroupId: (Optional) 资源组ID
        """

        self.containerId = containerId
        self.status = status
        self.instanceType = instanceType
        self.az = az
        self.name = name
        self.hostAliases = hostAliases
        self.hostname = hostname
        self.ag = ag
        self.command = command
        self.args = args
        self.envs = envs
        self.image = image
        self.secret = secret
        self.tty = tty
        self.workingDir = workingDir
        self.rootVolume = rootVolume
        self.dataVolumes = dataVolumes
        self.vpcId = vpcId
        self.subnetId = subnetId
        self.privateIpAddress = privateIpAddress
        self.elasticIpId = elasticIpId
        self.elasticIpAddress = elasticIpAddress
        self.primaryNetworkInterface = primaryNetworkInterface
        self.secondaryNetworkInterfaces = secondaryNetworkInterfaces
        self.logConfiguration = logConfiguration
        self.tags = tags
        self.charge = charge
        self.launchTime = launchTime
        self.reason = reason
        self.description = description
        self.resourceGroupId = resourceGroupId
