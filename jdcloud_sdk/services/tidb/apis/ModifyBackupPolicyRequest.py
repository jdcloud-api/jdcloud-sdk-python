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

from jdcloud_sdk.core.jdcloudrequest import JDCloudRequest


class ModifyBackupPolicyRequest(JDCloudRequest):
    """
    修改TiDB实例备份策略。
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(ModifyBackupPolicyRequest, self).__init__(
            '/regions/{regionId}/instances/{instanceId}:modifyBackupPolicy', 'POST', header, version)
        self.parameters = parameters


class ModifyBackupPolicyParameters(object):

    def __init__(self, regionId,instanceId,):
        """
        :param regionId: 地域代码
        :param instanceId: 实例ID
        """

        self.regionId = regionId
        self.instanceId = instanceId
        self.startWindow = None
        self.backupPeriod = None
        self.autoIncBackup = None

    def setStartWindow(self, startWindow):
        """
        :param startWindow: (Optional) 自动备份开始时间窗口,例如：00:00-01:00，表示0点到1点开始进行数据库自动备份，备份完成时间则跟实例大小有关，不一定在这个时间范围中该参数只能是以下取值:00:00-01:0001:00-02:00......23:00-24:00
        """
        self.startWindow = startWindow

    def setBackupPeriod(self, backupPeriod):
        """
        :param backupPeriod: (Optional) 自动备份的周期，多个取值用英文逗号分隔，支持以下参数，不区分大小写:- Monday：周一 - Tuesday：周二 - Wednesday：周三 - Thursday：周四 - Friday：周五- Saturday：周六- Sunday：周日 例如定义周一和周三备份，则输入为Monday,Wednesday
        """
        self.backupPeriod = backupPeriod

    def setAutoIncBackup(self, autoIncBackup):
        """
        :param autoIncBackup: (Optional) 是否开启自动增量备份。 开启后会在没有全量备份的日期自动进行一次增量备份
        """
        self.autoIncBackup = autoIncBackup

