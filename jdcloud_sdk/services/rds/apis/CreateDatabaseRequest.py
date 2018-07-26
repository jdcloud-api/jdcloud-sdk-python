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


class CreateDatabaseRequest(JDCloudRequest):
    """
    创建数据库</br>- SQL Server：支持</br>- MySQL：暂不支持
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(CreateDatabaseRequest, self).__init__(
            '/regions/{regionId}/instances/{instanceId}/databases', 'POST', header, version)
        self.parameters = parameters


class CreateDatabaseParameters(object):

    def __init__(self, regionId, instanceId, dbName, characterSetName):
        """
        :param regionId: 区域代码
        :param instanceId: 实例ID
        :param dbName: 数据库名称
        :param characterSetName: 字符集名称</br><strong>mysql字符集支持：</strong></br>- utf8；</br><strong>SQL Server字符集支持：</strong></br>- Chinese_PRC_CI_AS</br>- Chinese_PRC_CS_AS</br>- SQL_Latin1_General_CP1_CI_AS</br>- SQL_Latin1_General_CP1_CS_AS</br>- Chinese_PRC_BIN
        """

        self.regionId = regionId
        self.instanceId = instanceId
        self.dbName = dbName
        self.characterSetName = characterSetName

