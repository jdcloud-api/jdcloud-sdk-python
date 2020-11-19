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


class DBInstance(object):

    def __init__(self, instanceId=None, instanceName=None, instanceType=None, instanceStorageType=None, storageEncrypted=None, engine=None, engineVersion=None, instanceClass=None, instanceStorageGB=None, instanceCPU=None, instanceMemoryMB=None, regionId=None, azId=None, vpcId=None, subnetId=None, instanceStatus=None, publicDomainName=None, internalDomainName=None, createTime=None, backupSynchronicity=None, charge=None, tags=None, sourceInstanceId=None, instancePort=None):
        """
        :param instanceId: (Optional) 实例ID
        :param instanceName: (Optional) 实例名称，具体规则可参见帮助中心文档:[名称及密码限制](../../../documentation/Database-and-Cache-Service/RDS/Introduction/Restrictions/SQLServer-Restrictions.md)
        :param instanceType: (Optional) 实例类别，例如主实例，只读实例等，参见[枚举参数定义](../Enum-Definitions/Enum-Definitions.md)
        :param instanceStorageType: (Optional) 存储类型，参见[枚举参数定义](../Enum-Definitions/Enum-Definitions.md)<br>- 仅支持MySQL，Percona，MariaDB, SQL Server
        :param storageEncrypted: (Optional) 实例数据加密. false：不加密; true：加密
        :param engine: (Optional) 实例引擎类型，如MySQL或SQL Server等，参见[枚举参数定义](../Enum-Definitions/Enum-Definitions.md)
        :param engineVersion: (Optional) 实例引擎版本，参见[枚举参数定义](../Enum-Definitions/Enum-Definitions.md)
        :param instanceClass: (Optional) 实例规格代码
        :param instanceStorageGB: (Optional) 磁盘，单位GB
        :param instanceCPU: (Optional) CPU核数
        :param instanceMemoryMB: (Optional) 内存，单位MB
        :param regionId: (Optional) 地域ID，参见[地域及可用区对照表](../Enum-Definitions/Regions-AZ.md)
        :param azId: (Optional) 可用区ID，第一个为主实例在的可用区，参见[地域及可用区对照表](../Enum-Definitions/Regions-AZ.md)
        :param vpcId: (Optional) VPC的ID
        :param subnetId: (Optional) 子网的ID
        :param instanceStatus: (Optional) 实例状态，参见[枚举参数定义](../Enum-Definitions/Enum-Definitions.md)
        :param publicDomainName: (Optional) 实例公网域名<br>- 仅支持MySQL
        :param internalDomainName: (Optional) 实例内网域名<br>- 仅支持MySQL
        :param createTime: (Optional) 实例创建时间
        :param backupSynchronicity: (Optional) 实例跨地域备份服务开启相关信息
        :param charge: (Optional) 计费配置
        :param tags: (Optional) 标签信息
        :param sourceInstanceId: (Optional) MySQL、PostgreSQL只读实例对应的主实例ID
        :param instancePort: (Optional) 应用访问端口<br>- 仅支持MySQL
        """

        self.instanceId = instanceId
        self.instanceName = instanceName
        self.instanceType = instanceType
        self.instanceStorageType = instanceStorageType
        self.storageEncrypted = storageEncrypted
        self.engine = engine
        self.engineVersion = engineVersion
        self.instanceClass = instanceClass
        self.instanceStorageGB = instanceStorageGB
        self.instanceCPU = instanceCPU
        self.instanceMemoryMB = instanceMemoryMB
        self.regionId = regionId
        self.azId = azId
        self.vpcId = vpcId
        self.subnetId = subnetId
        self.instanceStatus = instanceStatus
        self.publicDomainName = publicDomainName
        self.internalDomainName = internalDomainName
        self.createTime = createTime
        self.backupSynchronicity = backupSynchronicity
        self.charge = charge
        self.tags = tags
        self.sourceInstanceId = sourceInstanceId
        self.instancePort = instancePort
