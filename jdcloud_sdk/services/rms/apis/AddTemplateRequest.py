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


class AddTemplateRequest(JDCloudRequest):
    """
    增加富媒体短信内容接口
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(AddTemplateRequest, self).__init__(
            '/regions/{regionId}/addTemplate', 'POST', header, version)
        self.parameters = parameters


class AddTemplateParameters(object):

    def __init__(self, regionId, ):
        """
        :param regionId: Region ID
        """

        self.regionId = regionId
        self.appId = None
        self.signType = None
        self.purpose = None
        self.signCardType = None
        self.aptitudes = None
        self.title = None
        self.description = None
        self.isTuiding = None
        self.content = None

    def setAppId(self, appId):
        """
        :param appId: (Optional) appId参数
        """
        self.appId = appId

    def setSignType(self, signType):
        """
        :param signType: (Optional) signType参数
        """
        self.signType = signType

    def setPurpose(self, purpose):
        """
        :param purpose: (Optional) purpose参数
        """
        self.purpose = purpose

    def setSignCardType(self, signCardType):
        """
        :param signCardType: (Optional) signCardType参数
        """
        self.signCardType = signCardType

    def setAptitudes(self, aptitudes):
        """
        :param aptitudes: (Optional) aptitudes参数
        """
        self.aptitudes = aptitudes

    def setTitle(self, title):
        """
        :param title: (Optional) title参数
        """
        self.title = title

    def setDescription(self, description):
        """
        :param description: (Optional) description参数
        """
        self.description = description

    def setIsTuiding(self, isTuiding):
        """
        :param isTuiding: (Optional) isTuiding参数
        """
        self.isTuiding = isTuiding

    def setContent(self, content):
        """
        :param content: (Optional) content参数
        """
        self.content = content
