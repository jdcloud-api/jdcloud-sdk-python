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


class DeleteDiskRequest(JDCloudRequest):
    """
    -   删除一块按配置计费的云硬盘，云盘类型包括高效云盘、SSD云盘、通用型SSD、性能型SSD和容量型HDD。
-   删除云盘时，云盘的状态必须为 待挂载（Available）。
-   云盘被删除后，云硬盘快照可以被保留。

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DeleteDiskRequest, self).__init__(
            '/regions/{regionId}/disks/{diskId}', 'DELETE', header, version)
        self.parameters = parameters


class DeleteDiskParameters(object):

    def __init__(self,regionId, diskId, ):
        """
        :param regionId: 地域ID
        :param diskId: 云硬盘ID
        """

        self.regionId = regionId
        self.diskId = diskId
        self.putInRecycleBin = None

    def setPutInRecycleBin(self, putInRecycleBin):
        """
        :param putInRecycleBin: (Optional) true 加入回收站 false 或者不传直接删除
        """
        self.putInRecycleBin = putInRecycleBin

