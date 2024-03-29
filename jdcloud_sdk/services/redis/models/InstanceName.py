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


class InstanceName(object):

    def __init__(self, resourceId, resourceName, serviceCode, resourceStatus=None):
        """
        :param resourceId:  资源id（即实例id）
        :param resourceName:  资源名称（即实例名称）
        :param resourceStatus: (Optional) 资源状态：creating表示创建中，running表示运行中，error表示错误，changing表示变更规格中，deleting表示删除中，configuring表示修改参数中，restoring表示备份恢复中
        :param serviceCode:  service code（redis）
        """

        self.resourceId = resourceId
        self.resourceName = resourceName
        self.resourceStatus = resourceStatus
        self.serviceCode = serviceCode
