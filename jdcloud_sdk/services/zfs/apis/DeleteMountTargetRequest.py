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


class DeleteMountTargetRequest(JDCloudRequest):
    """
    -   删除挂载目标的同时会删除相关的网络接口。

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DeleteMountTargetRequest, self).__init__(
            '/regions/{regionId}/mountTargets/{mountTargetId}', 'DELETE', header, version)
        self.parameters = parameters


class DeleteMountTargetParameters(object):

    def __init__(self,regionId, mountTargetId):
        """
        :param regionId: 地域ID
        :param mountTargetId: 挂载目标ID
        """

        self.regionId = regionId
        self.mountTargetId = mountTargetId

