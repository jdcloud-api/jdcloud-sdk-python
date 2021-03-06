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


class BatchDevice(object):

    def __init__(self, deviceName=None, identifier=None, deviceState=None, endTime=None, currentVersion=None, updatedState=None, progress=None, retriedTimes=None, retryTimes=None, erroCode=None, errorMsg=None, beginedTime=None):
        """
        :param deviceName: (Optional) 设备名称
        :param identifier: (Optional) 设备标识
        :param deviceState: (Optional) 设备状态：
online:在线
offline:离线 

        :param endTime: (Optional) 升级完成时间，时间为东八区（UTC/GMT+08:00）
        :param currentVersion: (Optional) 当前固件版本
        :param updatedState: (Optional) 升级状态：
sending:待推送
sended:已推送
waiting:待升级
processing:进行中
retrying:待重试
success:成功
failure:失败 

        :param progress: (Optional) 进度，[1,100]
        :param retriedTimes: (Optional) 已经重试的次数，[0,5]
        :param retryTimes: (Optional) 总次数，[0,5]
        :param erroCode: (Optional) 备注/失败原因码：
-1:推送超时失败
0:未知原因
1:下载固件失败
2:固件校验失败
3:固件烧录失败
4:固件升级超时
5:任务终止

        :param errorMsg: (Optional) 失败原因信息
        :param beginedTime: (Optional) 开始时间，时间为东八区（UTC/GMT+08:00）
        """

        self.deviceName = deviceName
        self.identifier = identifier
        self.deviceState = deviceState
        self.endTime = endTime
        self.currentVersion = currentVersion
        self.updatedState = updatedState
        self.progress = progress
        self.retriedTimes = retriedTimes
        self.retryTimes = retryTimes
        self.erroCode = erroCode
        self.errorMsg = errorMsg
        self.beginedTime = beginedTime
