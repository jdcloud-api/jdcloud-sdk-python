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


class ModifySmsAppUsingPOSTRequest(JDCloudRequest):
    """
    编辑短信应用
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(ModifySmsAppUsingPOSTRequest, self).__init__(
            '/smsApps/{appId}', 'POST', header, version)
        self.parameters = parameters


class ModifySmsAppUsingPOSTParameters(object):

    def __init__(self, appId, ):
        """
        :param appId: appId
        """

        self.appId = appId
        self.appDesc = None
        self.appName = None

    def setAppDesc(self, appDesc):
        """
        :param appDesc: (Optional) 应用描述
        """
        self.appDesc = appDesc

    def setAppName(self, appName):
        """
        :param appName: (Optional) 应用名称
        """
        self.appName = appName

