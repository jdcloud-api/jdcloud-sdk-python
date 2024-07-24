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


class GetAliveUrlNewRequest(JDCloudRequest):
    """
    H5活体检测获取采集页面链接新版
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(GetAliveUrlNewRequest, self).__init__(
            '/alive:getUrlNew', 'POST', header, version)
        self.parameters = parameters


class GetAliveUrlNewParameters(object):

    def __init__(self,returnUrl, ):
        """
        :param returnUrl: 采集结束后自动跳转的目标地址（须以http或https开头，长度不超过128字符）
        """

        self.name = None
        self.idcard = None
        self.returnUrl = returnUrl
        self.actions = None

    def setName(self, name):
        """
        :param name: (Optional) 姓名（需要进行身份核验时传递此参数）
        """
        self.name = name

    def setIdcard(self, idcard):
        """
        :param idcard: (Optional) 身份证号（需要进行身份核验时传递此参数）
        """
        self.idcard = idcard

    def setActions(self, actions):
        """
        :param actions: (Optional) 指定动作，逗号隔开。（LookLeft 向左，LookRight 向右，OpenMouth 张嘴，BlinkEye 眨眼，ShakeHead 摇头，NodHead 点头）
        """
        self.actions = actions

