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


class UpdateUserRoomRequest(JDCloudRequest):
    """
    修改房间

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(UpdateUserRoomRequest, self).__init__(
            '/updateUserRoom/{appId}', 'PUT', header, version)
        self.parameters = parameters


class UpdateUserRoomParameters(object):

    def __init__(self,appId, ):
        """
        :param appId: 应用ID
        """

        self.appId = appId
        self.userRoomId = None
        self.roomName = None
        self.roomType = None

    def setUserRoomId(self, userRoomId):
        """
        :param userRoomId: (Optional) 用户房间号
        """
        self.userRoomId = userRoomId

    def setRoomName(self, roomName):
        """
        :param roomName: (Optional) 房间名称
        """
        self.roomName = roomName

    def setRoomType(self, roomType):
        """
        :param roomType: (Optional) 房间类型 1-小房间；2-大房间
        """
        self.roomType = roomType

