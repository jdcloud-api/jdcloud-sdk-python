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


class UpdateSecurityPolicyRequest(JDCloudRequest):
    """
    修改一个安全策略的信息
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(UpdateSecurityPolicyRequest, self).__init__(
            '/regions/{regionId}/securityPolicies/{securityPolicyId}', 'PATCH', header, version)
        self.parameters = parameters


class UpdateSecurityPolicyParameters(object):

    def __init__(self,regionId, securityPolicyId, ):
        """
        :param regionId: Region ID
        :param securityPolicyId: Security Policy Id
        """

        self.regionId = regionId
        self.securityPolicyId = securityPolicyId
        self.securityPolicyName = None
        self.description = None
        self.protocols = None
        self.ciphers = None

    def setSecurityPolicyName(self, securityPolicyName):
        """
        :param securityPolicyName: (Optional) 安全策略名称,只允许输入中文、数字、大小写字母、英文下划线“_”及中划线“-”，不允许为空且不超过32字符
        """
        self.securityPolicyName = securityPolicyName

    def setDescription(self, description):
        """
        :param description: (Optional) 安全策略描述,允许输入UTF-8编码下的全部字符，不超过256字符
        """
        self.description = description

    def setProtocols(self, protocols):
        """
        :param protocols: (Optional) TLS协议版本列表，目前支持TLSv1、TLSv1.1、TLSv1.2和TLSv1.3，传入的每个protocol至少需要传入一个支持的cipher
        """
        self.protocols = protocols

    def setCiphers(self, ciphers):
        """
        :param ciphers: (Optional) TLS加密套件列表，传入的每个cipher至少需要传入一个能够支持的protocol
TLSv1和TLSv1.1支持的加密套件：
AES128-SHA
AES256-SHA
CAMELLIA128-SHA
CAMELLIA256-SHA
DES-CBC3-SHA
ECDHE-RSA-AES128-SHA
ECDHE-RSA-AES256-SHA
ECDHE-RSA-DES-CBC3-SHA
IDEA-CBC-SHA
SEED-SHA
ECDHE-ECDSA-AES256-SHA
ECDHE-ECDSA-AES128-SHA
ECDHE-ECDSA-DES-CBC3-SHA
TLSv1.2支持的加密套件：
AES128-CCM
AES128-CCM8
AES128-GCM-SHA256
AES128-SHA
AES128-SHA256
AES256-CCM
AES256-CCM8
AES256-GCM-SHA384
AES256-SHA
AES256-SHA256
ARIA128-GCM-SHA256
ARIA256-GCM-SHA384
CAMELLIA128-SHA
CAMELLIA128-SHA256
CAMELLIA256-SHA
CAMELLIA256-SHA256
DES-CBC3-SHA
ECDHE-ARIA128-GCM-SHA256
ECDHE-ARIA256-GCM-SHA384
ECDHE-RSA-AES128-GCM-SHA256
ECDHE-RSA-AES128-SHA
ECDHE-RSA-AES128-SHA256
ECDHE-RSA-AES256-GCM-SHA384
ECDHE-RSA-AES256-SHA
ECDHE-RSA-AES256-SHA384
ECDHE-RSA-CAMELLIA128-SHA256
ECDHE-RSA-CAMELLIA256-SHA384
ECDHE-RSA-CHACHA20-POLY1305
ECDHE-RSA-DES-CBC3-SHA
SEED-SHA
ECDHE-ECDSA-AES256-GCM-SHA384
ECDHE-ECDSA-CHACHA20-POLY1305
ECDHE-ECDSA-AES256-CCM8
ECDHE-ECDSA-AES256-CCM
ECDHE-ECDSA-ARIA256-GCM-SHA384
ECDHE-ECDSA-AES128-GCM-SHA256
ECDHE-ECDSA-AES128-CCM8
ECDHE-ECDSA-AES128-CCM
ECDHE-ECDSA-ARIA128-GCM-SHA256
ECDHE-ECDSA-AES256-SHA384
ECDHE-ECDSA-CAMELLIA256-SHA384
ECDHE-ECDSA-AES128-SHA256
ECDHE-ECDSA-CAMELLIA128-SHA256
ECDHE-ECDSA-AES256-SHA
ECDHE-ECDSA-AES128-SHA
ECDHE-ECDSA-DES-CBC3-SHA
TLSv1.3支持的加密套件：
TLS_AES_256_GCM_SHA384
TLS_CHACHA20_POLY1305_SHA256
TLS_AES_128_GCM_SHA256
        """
        self.ciphers = ciphers

