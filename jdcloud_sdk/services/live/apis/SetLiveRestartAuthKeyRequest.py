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


class SetLiveRestartAuthKeyRequest(JDCloudRequest):
    """
    设置直播回看播放鉴权KEY
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(SetLiveRestartAuthKeyRequest, self).__init__(
            '/liveRestartAuthKey', 'POST', header, version)
        self.parameters = parameters


class SetLiveRestartAuthKeyParameters(object):

    def __init__(self, restartDomain, ):
        """
        :param restartDomain: 直播回看播放域名
        """

        self.restartDomain = restartDomain
        self.authStatus = None
        self.authKey = None

    def setAuthStatus(self, authStatus):
        """
        :param authStatus: (Optional) 直播回看播放鉴权状态
  on: 开启
  off: 关闭
- 当回看播放鉴权状态on(开启)时,authKey不能为空

        """
        self.authStatus = authStatus

    def setAuthKey(self, authKey):
        """
        :param authKey: (Optional) 直播回看播放鉴权key
- 取值: 支持大小写字母和数字 长度6-32位

        """
        self.authKey = authKey
