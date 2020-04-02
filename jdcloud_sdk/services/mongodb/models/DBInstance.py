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

    def __init__(self, instanceId=None, instanceName=None, instanceType=None, engine=None, engineVersion=None, instanceStorageType=None, storageEncrypted=None, instanceClass=None, instanceStorageGB=None, instanceCPU=None, instanceMemoryGB=None, azId=None, vpcId=None, subnetId=None, replicaSetName=None, instanceDomain=None, dBName=None, accountName=None, instancePort=None, instanceStatus=None, backupRetentionPeriod=None, createTime=None, preferredBackupWindow=None, preferredmaintenanceWindow=None, charge=None, isSetSecurityIps=None, tags=None, mongos=None, configserver=None, shard=None):
        """
        :param instanceId: (Optional) 实例ID
        :param instanceName: (Optional) 实例名称
        :param instanceType: (Optional) 实例类型，副本集：Replication；分片集群：Sharding；
        :param engine: (Optional) 数据库类型
        :param engineVersion: (Optional) 数据库版本
        :param instanceStorageType: (Optional) 存储类型。LOCAL_SSD -本地盘SSD、LOCAL_NVMe -本地盘NVMe、EBS_SSD-SSD云盘。
        :param storageEncrypted: (Optional) 实例数据加密（存储类型为云硬盘才支持数据加密）。 false：不加密；true：加密。缺省为false。
        :param instanceClass: (Optional) 副本集实例规格代码
        :param instanceStorageGB: (Optional) 副本集存储空间
        :param instanceCPU: (Optional) 副本集CPU核数
        :param instanceMemoryGB: (Optional) 副本集内存，单位GB
        :param azId: (Optional) 副本集可用区区ID，依次为主、从、隐藏节点所在可用区
        :param vpcId: (Optional) VPCID
        :param subnetId: (Optional) 子网ID
        :param replicaSetName: (Optional) 副本集名称
        :param instanceDomain: (Optional) 副本集域名
        :param dBName: (Optional) 默认库名
        :param accountName: (Optional) 默认用户名
        :param instancePort: (Optional) 副本集访问端口
        :param instanceStatus: (Optional) 实例状态.RUNNING：运行, ERROR：错误 ,BUILDING：创建中, DELETING：删除中, RESTORING：恢复中, RESIZING：变配中
        :param backupRetentionPeriod: (Optional) 自动备份保留时间
        :param createTime: (Optional) 创建时间
        :param preferredBackupWindow: (Optional) 自动备份时间，如：00:00-02:00，表示0点到2点进行数据库自动备份
        :param preferredmaintenanceWindow: (Optional) 系统维护时间，如：00:00-02:00，表示0点到2点进行系统维护
        :param charge: (Optional) 计费信息
        :param isSetSecurityIps: (Optional) 是否设置白名单，true：已设置，false：未设置
        :param tags: (Optional) 标签
        :param mongos: (Optional) mongos信息
        :param configserver: (Optional) configserver信息
        :param shard: (Optional) shard信息
        """

        self.instanceId = instanceId
        self.instanceName = instanceName
        self.instanceType = instanceType
        self.engine = engine
        self.engineVersion = engineVersion
        self.instanceStorageType = instanceStorageType
        self.storageEncrypted = storageEncrypted
        self.instanceClass = instanceClass
        self.instanceStorageGB = instanceStorageGB
        self.instanceCPU = instanceCPU
        self.instanceMemoryGB = instanceMemoryGB
        self.azId = azId
        self.vpcId = vpcId
        self.subnetId = subnetId
        self.replicaSetName = replicaSetName
        self.instanceDomain = instanceDomain
        self.dBName = dBName
        self.accountName = accountName
        self.instancePort = instancePort
        self.instanceStatus = instanceStatus
        self.backupRetentionPeriod = backupRetentionPeriod
        self.createTime = createTime
        self.preferredBackupWindow = preferredBackupWindow
        self.preferredmaintenanceWindow = preferredmaintenanceWindow
        self.charge = charge
        self.isSetSecurityIps = isSetSecurityIps
        self.tags = tags
        self.mongos = mongos
        self.configserver = configserver
        self.shard = shard
