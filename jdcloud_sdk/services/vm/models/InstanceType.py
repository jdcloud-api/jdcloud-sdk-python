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


class InstanceType(object):

    def __init__(self, family=None, instanceType=None, cpu=None, architecture=None, memoryMB=None, nicLimit=None, cloudDiskCountLimit=None, desc=None, state=None, gpu=None, localDisks=None, generation=None, burstInfo=None, cloudDiskTypes=None):
        """
        :param family: (Optional) 实例规格族。
        :param instanceType: (Optional) 实例规格。
        :param cpu: (Optional) cpu个数。
        :param architecture: (Optional) 镜像架构。取值范围：`x86_64、arm64`。
        :param memoryMB: (Optional) 内存大小。
        :param nicLimit: (Optional) 支持绑定的弹性网卡数量，包括主网卡。
        :param cloudDiskCountLimit: (Optional) 支持挂载的云硬盘数量，包括云盘系统盘。
        :param desc: (Optional) 实例规格描述。
        :param state: (Optional) 实例规格售卖状态。已售罄的实例规格无法使用。
        :param gpu: (Optional) GPU配置，针对GPU类型的实例规格有效。
        :param localDisks: (Optional) 本地数据盘配置（缓存盘），针对GPU类型、或本地存储型的实例规格有效。
        :param generation: (Optional) 实例规格代数。
        :param burstInfo: (Optional) 突发型规格信息
        :param cloudDiskTypes: (Optional) 支持的云盘类型
        """

        self.family = family
        self.instanceType = instanceType
        self.cpu = cpu
        self.architecture = architecture
        self.memoryMB = memoryMB
        self.nicLimit = nicLimit
        self.cloudDiskCountLimit = cloudDiskCountLimit
        self.desc = desc
        self.state = state
        self.gpu = gpu
        self.localDisks = localDisks
        self.generation = generation
        self.burstInfo = burstInfo
        self.cloudDiskTypes = cloudDiskTypes
