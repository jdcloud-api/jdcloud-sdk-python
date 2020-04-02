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

    def __init__(self, backupId=None, backupName=None, instanceId=None, backupStatus=None, backupStartTime=None, backupEndTime=None, backupMode=None, backupMethod=None, backupSizeByte=None):
        """
        :param backupId: (Optional) 备份ID
        :param backupName: (Optional) 备份名称
        :param instanceId: (Optional) 备份所属实例ID
        :param backupStatus: (Optional) 备份状态，Waiting(等待中)、Running(备份中)、Finished(已完成)、(Failed错误)
        :param backupStartTime: (Optional) 备份开始时间
        :param backupEndTime: (Optional) 备份结束时间
        :param backupMode: (Optional) 备份模式，Automated(系统自动备份)、Manual(手动备份)
        :param backupMethod: (Optional) 备份方式，Logical - 逻辑备份、Physical - 物理备份
        :param backupSizeByte: (Optional) 整个备份集大小，单位：Byte
        """

        self.backupId = backupId
        self.backupName = backupName
        self.instanceId = instanceId
        self.backupStatus = backupStatus
        self.backupStartTime = backupStartTime
        self.backupEndTime = backupEndTime
        self.backupMode = backupMode
        self.backupMethod = backupMethod
        self.backupSizeByte = backupSizeByte
