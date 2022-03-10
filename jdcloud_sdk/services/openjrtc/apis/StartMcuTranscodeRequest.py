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


class StartMcuTranscodeRequest(JDCloudRequest):
    """
    下发混流任务

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(StartMcuTranscodeRequest, self).__init__(
            '/startMcuTranscode', 'POST', header, version)
        self.parameters = parameters


class StartMcuTranscodeParameters(object):

    def __init__(self, ):
        """
        """

        self.appId = None
        self.userRoomId = None
        self.layoutTemplate = None
        self.mainUserId = None
        self.outputType = None
        self.outputName = None
        self.mcuUserInfos = None
        self.outputEncode = None

    def setAppId(self, appId):
        """
        :param appId: (Optional) 应用ID
        """
        self.appId = appId

    def setUserRoomId(self, userRoomId):
        """
        :param userRoomId: (Optional) 业务接入方定义的且在JRTC系统内注册过的房间号
        """
        self.userRoomId = userRoomId

    def setLayoutTemplate(self, layoutTemplate):
        """
        :param layoutTemplate: (Optional) 布局模板-支持参数1
        """
        self.layoutTemplate = layoutTemplate

    def setMainUserId(self, mainUserId):
        """
        :param mainUserId: (Optional) 主人员userId
        """
        self.mainUserId = mainUserId

    def setOutputType(self, outputType):
        """
        :param outputType: (Optional) 输出类型 1：录制 2：旁路转推
        """
        self.outputType = outputType

    def setOutputName(self, outputName):
        """
        :param outputName: (Optional) 输出名称
        """
        self.outputName = outputName

    def setMcuUserInfos(self, mcuUserInfos):
        """
        :param mcuUserInfos: (Optional) 参与混流人员参数
        """
        self.mcuUserInfos = mcuUserInfos

    def setOutputEncode(self, outputEncode):
        """
        :param outputEncode: (Optional) 输出格式
        """
        self.outputEncode = outputEncode

