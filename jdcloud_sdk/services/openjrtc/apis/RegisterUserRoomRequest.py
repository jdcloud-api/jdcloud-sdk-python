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


class RegisterUserRoomRequest(JDCloudRequest):
    """
    注册用户房间号-将业务接入方定义的userRoomId注册为jrtc系统内可识别和流转的房间号

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(RegisterUserRoomRequest, self).__init__(
            '/registerUserRoom', 'POST', header, version)
        self.parameters = parameters


class RegisterUserRoomParameters(object):

    def __init__(self,):
        """
        """

        self.userRoomId = None
        self.roomName = None
        self.appId = None
        self.roomType = None

    def setUserRoomId(self, userRoomId):
        """
        :param userRoomId: (Optional) 业务接入方定义的房间号
        """
        self.userRoomId = userRoomId

    def setRoomName(self, roomName):
        """
        :param roomName: (Optional) 房间名称
        """
        self.roomName = roomName

    def setAppId(self, appId):
        """
        :param appId: (Optional) 应用ID
        """
        self.appId = appId

    def setRoomType(self, roomType):
        """
        :param roomType: (Optional) 房间类型 1-小房间(音频单流订阅) 2-大房间(音频固定订阅),默认取控制台APP对应的房间类型
        """
        self.roomType = roomType

