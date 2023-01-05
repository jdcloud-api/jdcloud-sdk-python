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


class AddNetworkSecurityGroupRulesRequest(JDCloudRequest):
    """
    添加安全组规则
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(AddNetworkSecurityGroupRulesRequest, self).__init__(
            '/regions/{regionId}/networkSecurityGroups/{networkSecurityGroupId}:addNetworkSecurityGroupRules', 'POST', header, version)
        self.parameters = parameters


class AddNetworkSecurityGroupRulesParameters(object):

    def __init__(self,regionId, networkSecurityGroupId, networkSecurityGroupRuleSpecs):
        """
        :param regionId: Region ID
        :param networkSecurityGroupId: NetworkSecurityGroup ID
        :param networkSecurityGroupRuleSpecs: 安全组规则信息
        """

        self.regionId = regionId
        self.networkSecurityGroupId = networkSecurityGroupId
        self.networkSecurityGroupRuleSpecs = networkSecurityGroupRuleSpecs

