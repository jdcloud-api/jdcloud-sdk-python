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


class CreateDataMigrationRequest(JDCloudRequest):
    """
    创建一个数据迁移任务，可以将对象存储 OSS 中的数据导入到 TiDB 实例中，具体可以参考帮助文档。
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(CreateDataMigrationRequest, self).__init__(
            '/regions/{regionId}/instances/{instanceId}/migration', 'POST', header, version)
        self.parameters = parameters


class CreateDataMigrationParameters(object):

    def __init__(self,regionId, instanceId, migrationType, importTask):
        """
        :param regionId: 地域代码
        :param instanceId: 实例ID
        :param migrationType: 迁移任务类型，支持以下类型（大小写不敏感）：<br>-FULL_IMPORT:全量数据导入
        :param importTask: 使用 TiDB Lightning 进行的数据迁移任务
        """

        self.regionId = regionId
        self.instanceId = instanceId
        self.migrationType = migrationType
        self.importTask = importTask

