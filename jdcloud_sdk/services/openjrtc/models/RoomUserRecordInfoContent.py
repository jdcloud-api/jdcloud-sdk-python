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


class RoomUserRecordInfoContent(object):

    def __init__(self, appId=None, userRoomId=None, roomName=None, userId=None, nickName=None, deviceId=None, deviceName=None, deviceType=None, deviceModel=None, sdkVersion=None, internalIp=None, networkType=None, extranetIp=None, isp=None, city=None, province=None, country=None, status=None, joinTime=None, leaveTime=None):
        """
        :param appId: (Optional) 应用ID
        :param userRoomId: (Optional) 业务接入方定义的且在JRTC系统内注册过的用户房间号
        :param roomName: (Optional) 房间名称
        :param userId: (Optional) 业务接入方定义的且在JRTC系统内注册过的用户ID
        :param nickName: (Optional) 昵称
        :param deviceId: (Optional) 设备ID
        :param deviceName: (Optional) 设备名称
        :param deviceType: (Optional) 设备类型
        :param deviceModel: (Optional) 设备型号
        :param sdkVersion: (Optional) sdk版本
        :param internalIp: (Optional) 接入服务器ip
        :param networkType: (Optional) 接入网络类型
        :param extranetIp: (Optional) 接入网络ip
        :param isp: (Optional) 网络服务提供商
        :param city: (Optional) 网络接入城市
        :param province: (Optional) 网络接入省份
        :param country: (Optional) 网络接入国家
        :param status: (Optional) 状态 1-在线 2-离线
        :param joinTime: (Optional) 加入时间
        :param leaveTime: (Optional) 离开时间
        """

        self.appId = appId
        self.userRoomId = userRoomId
        self.roomName = roomName
        self.userId = userId
        self.nickName = nickName
        self.deviceId = deviceId
        self.deviceName = deviceName
        self.deviceType = deviceType
        self.deviceModel = deviceModel
        self.sdkVersion = sdkVersion
        self.internalIp = internalIp
        self.networkType = networkType
        self.extranetIp = extranetIp
        self.isp = isp
        self.city = city
        self.province = province
        self.country = country
        self.status = status
        self.joinTime = joinTime
        self.leaveTime = leaveTime
