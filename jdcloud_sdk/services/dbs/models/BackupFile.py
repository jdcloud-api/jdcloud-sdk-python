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


class BackupFile(object):

    def __init__(self, planId, backupType, dataSourceId, isManual, filename, extInfo, path, size, storageType, taskId, srcSize=None, binlogStartTime=None, binlogEndTime=None, binlogStartPos=None, binlogEndPos=None, version=None):
        """
        :param planId:  
        :param backupType:  
        :param dataSourceId:  
        :param isManual:  0代表自动备份 1代表的是手动触发备份
        :param filename:  
        :param extInfo:  
        :param path:  
        :param size:  
        :param srcSize: (Optional) 
        :param storageType:  
        :param taskId:  
        :param binlogStartTime: (Optional) 
        :param binlogEndTime: (Optional) 
        :param binlogStartPos: (Optional) 
        :param binlogEndPos: (Optional) 
        :param version: (Optional) 
        """

        self.planId = planId
        self.backupType = backupType
        self.dataSourceId = dataSourceId
        self.isManual = isManual
        self.filename = filename
        self.extInfo = extInfo
        self.path = path
        self.size = size
        self.srcSize = srcSize
        self.storageType = storageType
        self.taskId = taskId
        self.binlogStartTime = binlogStartTime
        self.binlogEndTime = binlogEndTime
        self.binlogStartPos = binlogStartPos
        self.binlogEndPos = binlogEndPos
        self.version = version
