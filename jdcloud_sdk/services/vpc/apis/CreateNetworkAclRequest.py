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


class CreateNetworkAclRequest(JDCloudRequest):
    """
    创建networkAcl接口
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(CreateNetworkAclRequest, self).__init__(
            '/regions/{regionId}/networkAcls/', 'POST', header, version)
        self.parameters = parameters


class CreateNetworkAclParameters(object):

    def __init__(self,regionId, vpcId, networkAclName, ):
        """
        :param regionId: Region ID
        :param vpcId: 私有网络id
        :param networkAclName: networkAcl名称
        """

        self.regionId = regionId
        self.vpcId = vpcId
        self.networkAclName = networkAclName
        self.description = None

    def setDescription(self, description):
        """
        :param description: (Optional) 描述,允许输入UTF-8编码下的全部字符，不超过256字符
        """
        self.description = description

