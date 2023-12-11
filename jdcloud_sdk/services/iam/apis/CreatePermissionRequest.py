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


class CreatePermissionRequest(JDCloudRequest):
    """
    创建策略 <br>
关于策略的详细介绍，可以查询<a href="https://docs.jdcloud.com/cn/iam/policy-overview">策略概览</a> <br>

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(CreatePermissionRequest, self).__init__(
            '/regions/{regionId}/permission', 'POST', header, version)
        self.parameters = parameters


class CreatePermissionParameters(object):

    def __init__(self,regionId, createPermissionInfo):
        """
        :param regionId: Region ID
        :param createPermissionInfo: 权限信息
        """

        self.regionId = regionId
        self.createPermissionInfo = createPermissionInfo

