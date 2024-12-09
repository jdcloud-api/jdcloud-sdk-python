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


class DescribePlansCanUpgradeRequest(JDCloudRequest):
    """
    查询当前实例可升级套餐列表。

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribePlansCanUpgradeRequest, self).__init__(
            '/regions/{regionId}/instances/{instanceId}:describePlansCanUpgrade', 'GET', header, version)
        self.parameters = parameters


class DescribePlansCanUpgradeParameters(object):

    def __init__(self,instanceId, regionId):
        """
        :param instanceId: 轻量应用云主机的实例ID

        :param regionId: regionId

        """

        self.instanceId = instanceId
        self.regionId = regionId
