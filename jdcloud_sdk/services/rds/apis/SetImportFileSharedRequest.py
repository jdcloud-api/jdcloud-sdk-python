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


class SetImportFileSharedRequest(JDCloudRequest):
    """
    设置或取消上传文件是否共享给同一账号下的其他实例。缺省情况下，文件仅在上传的实例上可见并可导入，其他实例不可见不可导入。如果需要该文件在其他实例上也可导入，可将此文件设置为共享<br>- 仅支持SQL Server
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(SetImportFileSharedRequest, self).__init__(
            '/regions/{regionId}/instances/{instanceId}/importFiles/{fileName}:setShared', 'POST', header, version)
        self.parameters = parameters


class SetImportFileSharedParameters(object):

    def __init__(self,regionId, instanceId, fileName, shared):
        """
        :param regionId: 地域代码，取值范围参见[《各地域及可用区对照表》](../Enum-Definitions/Regions-AZ.md)
        :param instanceId: RDS 实例ID，唯一标识一个RDS实例
        :param fileName: 单库上云文件名
        :param shared: 文件是否共享<br>true:共享<br>false:不共享
        """

        self.regionId = regionId
        self.instanceId = instanceId
        self.fileName = fileName
        self.shared = shared

