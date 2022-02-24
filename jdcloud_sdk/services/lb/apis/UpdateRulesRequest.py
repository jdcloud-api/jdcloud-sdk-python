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


class UpdateRulesRequest(JDCloudRequest):
    """
    修改转发规则
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(UpdateRulesRequest, self).__init__(
            '/regions/{regionId}/urlMaps/{urlMapId}:updateRules', 'PATCH', header, version)
        self.parameters = parameters


class UpdateRulesParameters(object):

    def __init__(self, regionId,urlMapId,ruleUpdateSpecs):
        """
        :param regionId: Region ID
        :param urlMapId: 转发规则组Id
        :param ruleUpdateSpecs: 更新转发规则rules信息
        """

        self.regionId = regionId
        self.urlMapId = urlMapId
        self.ruleUpdateSpecs = ruleUpdateSpecs

