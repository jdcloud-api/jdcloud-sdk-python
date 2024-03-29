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


class DeleteLiveStreamDomainTranslateRequest(JDCloudRequest):
    """
    删除域名的翻译模板配置
- 删除域名级别翻译模板配置,重新推流后生效

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DeleteLiveStreamDomainTranslateRequest, self).__init__(
            '/translateDomains/{publishDomain}/templates/{template}:config', 'DELETE', header, version)
        self.parameters = parameters


class DeleteLiveStreamDomainTranslateParameters(object):

    def __init__(self, publishDomain, template, ):
        """
        :param publishDomain: 推流域名
        :param template: 翻译模板
        """

        self.publishDomain = publishDomain
        self.template = template

