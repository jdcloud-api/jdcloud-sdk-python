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


class BackupFileRequest(JDCloudRequest):
    """
    上传备份文件信息
    """

    def __init__(self, parameters, header=None, version="v2"):
        super(BackupFileRequest, self).__init__(
            '/regions/{regionId}/backupFile', 'POST', header, version)
        self.parameters = parameters


class BackupFileParameters(object):

    def __init__(self, regionId,planId, backupType, dataSourceId, isManual, filename, extInfo, path, size, storageType, taskId, ):
        """
        :param regionId: 地域代码，取值范围参见[《各地域及可用区对照表》]
        :param planId: 
        :param backupType: 
        :param dataSourceId: 
        :param isManual: 0代表自动备份 1代表的是手动触发备份
        :param filename: 
        :param extInfo: 
        :param path: 
        :param size: 
        :param storageType: 
        :param taskId: 
        """

        self.regionId = regionId
        self.planId = planId
        self.backupType = backupType
        self.dataSourceId = dataSourceId
        self.isManual = isManual
        self.filename = filename
        self.extInfo = extInfo
        self.path = path
        self.size = size
        self.srcSize = None
        self.storageType = storageType
        self.taskId = taskId
        self.binlogStartTime = None
        self.binlogEndTime = None
        self.binlogStartPos = None
        self.binlogEndPos = None
        self.version = None

    def setSrcSize(self, srcSize):
        """
        :param srcSize: (Optional) 
        """
        self.srcSize = srcSize

    def setBinlogStartTime(self, binlogStartTime):
        """
        :param binlogStartTime: (Optional) 
        """
        self.binlogStartTime = binlogStartTime

    def setBinlogEndTime(self, binlogEndTime):
        """
        :param binlogEndTime: (Optional) 
        """
        self.binlogEndTime = binlogEndTime

    def setBinlogStartPos(self, binlogStartPos):
        """
        :param binlogStartPos: (Optional) 
        """
        self.binlogStartPos = binlogStartPos

    def setBinlogEndPos(self, binlogEndPos):
        """
        :param binlogEndPos: (Optional) 
        """
        self.binlogEndPos = binlogEndPos

    def setVersion(self, version):
        """
        :param version: (Optional) 
        """
        self.version = version

