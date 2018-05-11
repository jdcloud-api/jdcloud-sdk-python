# coding=utf8

# Copyright 2018-2025 JDCLOUD.COM
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http:#www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# NOTE: This class is auto generated by the jdcloud code generator program.

from jdcloud_sdk.core.jdcloudrequest import JDCloudRequest


class CreateTableRequest(JDCloudRequest):
    """
    创建数据表
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(CreateTableRequest, self).__init__(
            '/regions/{regionId}/dwTable', 'POST', header, version)
        self.parameters = parameters


class CreateTableParameters(object):

    def __init__(self, regionId, instanceName, dbModelDBTable):
        """
        :param regionId: 地域ID
        :param instanceName: 实例名称
        :param dbModelDBTable: 数据表描述
        """

        self.regionId = regionId
        self.instanceName = instanceName
        self.dbModelDBTable = dbModelDBTable

