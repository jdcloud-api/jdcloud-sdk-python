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


class AssociateNetworkAclRequest(JDCloudRequest):
    """
    给子网绑定networkAcl接口
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(AssociateNetworkAclRequest, self).__init__(
            '/regions/{regionId}/networkAcls/{networkAclId}:associateNetworkAcl', 'POST', header, version)
        self.parameters = parameters


class AssociateNetworkAclParameters(object):

    def __init__(self,regionId, networkAclId, subnetIds):
        """
        :param regionId: Region ID
        :param networkAclId: networkAclId ID
        :param subnetIds: networkAcl要绑定的子网ID列表, subnet已被其他networkAcl绑定时，自动解绑
        """

        self.regionId = regionId
        self.networkAclId = networkAclId
        self.subnetIds = subnetIds

