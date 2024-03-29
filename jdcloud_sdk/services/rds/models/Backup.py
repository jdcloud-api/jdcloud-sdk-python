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


class Backup(object):

    def __init__(self, backupId=None, backupName=None, instanceId=None, instanceName=None, backupStatus=None, backupStartTime=None, backupEndTime=None, backupType=None, backupMode=None, backupMethod=None, backupUnit=None, backupFiles=None, backupSizeByte=None, descriptionkey=None, availabilityZone=None, engine=None, ifSupportDownload=None, serverId=None):
        """
        :param backupId: (Optional) 备份ID
        :param backupName: (Optional) 备份名称，最长支持64个英文字符或等长的中文字符
        :param instanceId: (Optional) 备份所属实例ID
        :param instanceName: (Optional) 备份所属实例名称
        :param backupStatus: (Optional) 备份状态，请查看[枚举参数定义](../Enum-Definitions/Enum-Definitions.md)
        :param backupStartTime: (Optional) 备份开始时间，格式为：YYYY-MM-DD HH:mm:ss
        :param backupEndTime: (Optional) 备份结束时间，格式为：YYYY-MM-DD HH:mm:ss<br>- **SQL Server、MySQL支持**<br>
        :param backupType: (Optional) 备份类型，全量备份或增量备份，请查看[枚举参数定义](../Enum-Definitions/Enum-Definitions.md)<br>- **SQL Server支持**<br>- **MySQL不支持**
        :param backupMode: (Optional) 备份模式，系统自动备份或手动备份，请查看[枚举参数定义](../Enum-Definitions/Enum-Definitions.md)
        :param backupMethod: (Optional) 备份方法，支持物理备份和快照备份，请查看[枚举参数定义](../Enum-Definitions/Enum-Definitions.md)<br>- **仅支持 MySQL、MariaDB、Percona**
        :param backupUnit: (Optional) 备份粒度，实例备份或者多库备份，请查看[枚举参数定义](../Enum-Definitions/Enum-Definitions.md)<br>- **SQL Server支持**<br>- **MySQL不支持**
        :param backupFiles: (Optional) 备份文件列表<br>- **SQL Server支持**,备份可以有多个文件，文件名的命名规则为:<br>（1）全备：数据库名+.bak<br>（2）增量：数据库名+.diff<br>- **MySQL不支持**
        :param backupSizeByte: (Optional) 整个备份集大小，单位：Byte
        :param descriptionkey: (Optional) 加密秘钥
        :param availabilityZone: (Optional) 备份上传的可用区
        :param engine: (Optional) 实例引擎类型，如MySQL等，参见[枚举参数定义](../Enum-Definitions/Enum-Definitions.md)
        :param ifSupportDownload: (Optional) 备份是否支持下载，0为不支持，1为支持<br>- **仅PostgreSQL支持**
        :param serverId: (Optional) serverId
        """

        self.backupId = backupId
        self.backupName = backupName
        self.instanceId = instanceId
        self.instanceName = instanceName
        self.backupStatus = backupStatus
        self.backupStartTime = backupStartTime
        self.backupEndTime = backupEndTime
        self.backupType = backupType
        self.backupMode = backupMode
        self.backupMethod = backupMethod
        self.backupUnit = backupUnit
        self.backupFiles = backupFiles
        self.backupSizeByte = backupSizeByte
        self.descriptionkey = descriptionkey
        self.availabilityZone = availabilityZone
        self.engine = engine
        self.ifSupportDownload = ifSupportDownload
        self.serverId = serverId
