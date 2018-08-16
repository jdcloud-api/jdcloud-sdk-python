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


class DescribeDatabasesRequest(JDCloudRequest):
    """
    查看数据库列表</br>- SQL Server：支持</br>- MySQL：支持
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeDatabasesRequest, self).__init__(
            '/regions/{regionId}/instances/{instanceId}/databases', 'GET', header, version)
        self.parameters = parameters


class DescribeDatabasesParameters(object):

    def __init__(self, regionId, instanceId, ):
        """
        :param regionId: 区域代码
        :param instanceId: 实例ID
        """

        self.regionId = regionId
        self.instanceId = instanceId
        self.dbName = None

    def setDbName(self, dbName):
        """
        :param dbName: (Optional) 数据库名称</br>- SQL Server：支持</br>- MySQL：暂不支持
        """
        self.dbName = dbName

