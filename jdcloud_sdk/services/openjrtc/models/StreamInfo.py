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


class StreamInfo(object):

    def __init__(self, appId=None, userRoomId=None, roomName=None, userId=None, userName=None, nickName=None, streamId=None, streamName=None, kind=None, status=None, deviceType=None, publishCount=None, publishTime=None, createTime=None):
        """
        :param appId: (Optional) appId
        :param userRoomId: (Optional) 业务接入方定义的且在JRTC系统内注册过的房间号
        :param roomName: (Optional) 用户注册时使用的房间名称
        :param userId: (Optional) 业务接入方用户体系定义的且在JRTC系统内注册过的userId
        :param userName: (Optional) 用户注册时使用的用户名称
        :param nickName: (Optional) 用户加入房间时使用的昵称
        :param streamId: (Optional) 流ID
        :param streamName: (Optional) 流名称
        :param kind: (Optional) 流类型 1-音频流; 2-视频流; 100-数据流
        :param status: (Optional) 流状态 1-在线; 2-离线
        :param deviceType: (Optional) 标识推流设备类型 1-FrontCamera; 2-BackCamera; 3-ScreenCapturer; 4-FileVideo
        :param publishCount: (Optional) 推流次数
        :param publishTime: (Optional) 推流时间
        :param createTime: (Optional) 流创建时间(第一次推流时间)
        """

        self.appId = appId
        self.userRoomId = userRoomId
        self.roomName = roomName
        self.userId = userId
        self.userName = userName
        self.nickName = nickName
        self.streamId = streamId
        self.streamName = streamName
        self.kind = kind
        self.status = status
        self.deviceType = deviceType
        self.publishCount = publishCount
        self.publishTime = publishTime
        self.createTime = createTime
