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


class SetLiveDomainReferRequest(JDCloudRequest):
    """
    设置域名refer防盗链
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(SetLiveDomainReferRequest, self).__init__(
            '/liveDomain/{domain}/refer', 'POST', header, version)
        self.parameters = parameters


class SetLiveDomainReferParameters(object):

    def __init__(self,domain, ):
        """
        :param domain: 用户域名
        """

        self.domain = domain
        self.referType = None
        self.referList = None
        self.allowNoReferHeader = None
        self.allowNullReferHeader = None

    def setReferType(self, referType):
        """
        :param referType: (Optional) refer类型，取值：block（黑名单），allow（白名单）默认为block
        """
        self.referType = referType

    def setReferList(self, referList):
        """
        :param referList: (Optional) 逗号隔开的域名列表，如果referList传空则为删除
        """
        self.referList = referList

    def setAllowNoReferHeader(self, allowNoReferHeader):
        """
        :param allowNoReferHeader: (Optional) 是否允许空refer访问，默认为“on”
        """
        self.allowNoReferHeader = allowNoReferHeader

    def setAllowNullReferHeader(self, allowNullReferHeader):
        """
        :param allowNullReferHeader: (Optional) 是否允许无ua访问，默认为“on”
        """
        self.allowNullReferHeader = allowNullReferHeader

