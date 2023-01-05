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


class DescribeQuotaRequest(JDCloudRequest):
    """
    查询云硬盘和快照资源的配额
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeQuotaRequest, self).__init__(
            '/regions/{regionId}/quotas', 'GET', header, version)
        self.parameters = parameters


class DescribeQuotaParameters(object):

    def __init__(self,regionId, type):
        """
        :param regionId: 地域ID
        :param type: 资源类型  disk：用户能创建的云盘的配额  snapshot： 用户能创建的快照的配额 snapshot_policy： 用户能创建的快照策略的配额
        """

        self.regionId = regionId
        self.type = type

