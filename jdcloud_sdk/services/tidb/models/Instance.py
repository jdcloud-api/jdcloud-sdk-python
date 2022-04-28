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


class Instance(object):

    def __init__(self, instanceId=None, instanceName=None, engineVersion=None, minorVersion=None, totalNodeNum=None, totalCPU=None, totalMemoryGB=None, totalStorageGB=None, regionId=None, azId=None, vpcId=None, subnetId=None, instanceStatus=None, createTime=None, charge=None, tags=None):
        """
        :param instanceId: (Optional) 实例ID
        :param instanceName: (Optional) 实例名称
        :param engineVersion: (Optional) 实例引擎版本
        :param minorVersion: (Optional) 实例引擎版本的详细版本号
        :param totalNodeNum: (Optional) 集群中节点的总数
        :param totalCPU: (Optional) 整个集群总的CPU核数
        :param totalMemoryGB: (Optional) 整个集群总的内存大小，单位GB
        :param totalStorageGB: (Optional) 整个集群总的存储空间大小，单位GB
        :param regionId: (Optional) 地域ID
        :param azId: (Optional) 可用区ID，目前仅支持单可用区
        :param vpcId: (Optional) VPC的ID
        :param subnetId: (Optional) 子网的ID
        :param instanceStatus: (Optional) 实例状态，参见[枚举参数定义](../Enum-Definitions/Enum-Definitions.md)
        :param createTime: (Optional) 实例创建时间, UTC 时间格式
        :param charge: (Optional) 计费配置
        :param tags: (Optional) 标签信息
        """

        self.instanceId = instanceId
        self.instanceName = instanceName
        self.engineVersion = engineVersion
        self.minorVersion = minorVersion
        self.totalNodeNum = totalNodeNum
        self.totalCPU = totalCPU
        self.totalMemoryGB = totalMemoryGB
        self.totalStorageGB = totalStorageGB
        self.regionId = regionId
        self.azId = azId
        self.vpcId = vpcId
        self.subnetId = subnetId
        self.instanceStatus = instanceStatus
        self.createTime = createTime
        self.charge = charge
        self.tags = tags
