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


class ApplySnapshotPoliciesRequest(JDCloudRequest):
    """
    绑定/解绑快照策略与磁盘关系
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(ApplySnapshotPoliciesRequest, self).__init__(
            '/regions/{regionId}/snapshotPolicies:apply', 'POST', header, version)
        self.parameters = parameters


class ApplySnapshotPoliciesParameters(object):

    def __init__(self, regionId, ):
        """
        :param regionId: 地域ID
        """

        self.regionId = regionId
        self.relations = None

    def setRelations(self, relations):
        """
        :param relations: (Optional) 绑定/解绑操作
        """
        self.relations = relations

