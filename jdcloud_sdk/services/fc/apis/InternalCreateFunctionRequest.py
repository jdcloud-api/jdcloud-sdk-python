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


class InternalCreateFunctionRequest(JDCloudRequest):
    """
    内部创建函数

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(InternalCreateFunctionRequest, self).__init__(
            '/regions/{regionId}/services/{serviceName}/functions:internal', 'POST', header, version)
        self.parameters = parameters


class InternalCreateFunctionParameters(object):

    def __init__(self,regionId, serviceName, functionSpec, ):
        """
        :param regionId: Region ID
        :param serviceName: Service Name
        :param functionSpec: 函数 创建参数
        """

        self.regionId = regionId
        self.serviceName = serviceName
        self.functionSpec = functionSpec
        self.clientToken = None

    def setClientToken(self, clientToken):
        """
        :param clientToken: (Optional) 保证请求幂等性的字符串；最大长度64个ASCII字符
        """
        self.clientToken = clientToken

