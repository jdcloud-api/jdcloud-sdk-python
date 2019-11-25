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


class FuntionApi(object):

    def __init__(self, apiId=None, apiGroupId=None, groupName=None, revision=None, apiName=None, action=None, path=None, description=None, deploymentStatus=None):
        """
        :param apiId: (Optional) 接口ID
        :param apiGroupId: (Optional) 分组ID
        :param groupName: (Optional) 分组名称
        :param revision: (Optional) 修订版本号
        :param apiName: (Optional) API名称
        :param action: (Optional) 请求方式
        :param path: (Optional) 请求路径，同时发布多个环境后会有多个路径
        :param description: (Optional) API描述
        :param deploymentStatus: (Optional) 部署状态(1:已部署)
        """

        self.apiId = apiId
        self.apiGroupId = apiGroupId
        self.groupName = groupName
        self.revision = revision
        self.apiName = apiName
        self.action = action
        self.path = path
        self.description = description
        self.deploymentStatus = deploymentStatus
