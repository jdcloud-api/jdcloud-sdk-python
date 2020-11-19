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


class CertificateTemplateStateRequest(JDCloudRequest):
    """
    查询域名信息模板实名认证状态
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(CertificateTemplateStateRequest, self).__init__(
            '/regions/{regionId}/template/{templateId}/certificate', 'GET', header, version)
        self.parameters = parameters


class CertificateTemplateStateParameters(object):

    def __init__(self, regionId, templateId, ):
        """
        :param regionId: 实例所属的地域ID
        :param templateId: 模板ID
        """

        self.regionId = regionId
        self.templateId = templateId

