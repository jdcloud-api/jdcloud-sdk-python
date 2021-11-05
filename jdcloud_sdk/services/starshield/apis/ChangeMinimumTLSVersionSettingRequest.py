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


class ChangeMinimumTLSVersionSettingRequest(JDCloudRequest):
    """
    设置HTTPS请求使用的TLS协议的最低版本。例如，如果选择TLS 1.1，那么TLS 1.0连接将被拒绝，而1.1、1.2和1.3（如果启用）将被允许。
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(ChangeMinimumTLSVersionSettingRequest, self).__init__(
            '/zones/{zone_identifier}/settings$$min_tls_version', 'PATCH', header, version)
        self.parameters = parameters


class ChangeMinimumTLSVersionSettingParameters(object):

    def __init__(self, zone_identifier, ):
        """
        :param zone_identifier: 
        """

        self.zone_identifier = zone_identifier
        self.value = None

    def setValue(self, value):
        """
        :param value: (Optional) TLS协议版本
        """
        self.value = value

