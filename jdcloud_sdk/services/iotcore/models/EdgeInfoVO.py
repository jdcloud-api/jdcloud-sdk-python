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


class EdgeInfoVO(object):

    def __init__(self, uuid=None, edgeId=None, edgeName=None, edgeStatus=None, edgeDesc=None, edgeVersion=None, createTime=None, lastOnlineTime=None, lastTurnOnTime=None, iothubInstanceId=None, iothubInstanceName=None):
        """
        :param uuid: (Optional) 系统流水号
        :param edgeId: (Optional) Edge的唯一编号
        :param edgeName: (Optional) Edge的名称
        :param edgeStatus: (Optional) 是否在线【0-离线，1-在线】
        :param edgeDesc: (Optional) 边缘计算说明
        :param edgeVersion: (Optional) Edge版本
        :param createTime: (Optional) Edge创建时间
        :param lastOnlineTime: (Optional) 最后在线时间
        :param lastTurnOnTime: (Optional) 最后开机时间
        :param iothubInstanceId: (Optional) IoT Hub实例编号
        :param iothubInstanceName: (Optional) IoT Hub实例名称
        """

        self.uuid = uuid
        self.edgeId = edgeId
        self.edgeName = edgeName
        self.edgeStatus = edgeStatus
        self.edgeDesc = edgeDesc
        self.edgeVersion = edgeVersion
        self.createTime = createTime
        self.lastOnlineTime = lastOnlineTime
        self.lastTurnOnTime = lastTurnOnTime
        self.iothubInstanceId = iothubInstanceId
        self.iothubInstanceName = iothubInstanceName
