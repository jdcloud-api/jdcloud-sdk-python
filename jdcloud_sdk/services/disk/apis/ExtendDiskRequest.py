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


class ExtendDiskRequest(JDCloudRequest):
    """
    -   扩容云硬盘到指定大小，云硬盘状态必须为 available。
-   当云硬盘正在创建快照时，不允许扩容。

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(ExtendDiskRequest, self).__init__(
            '/regions/{regionId}/disks/{diskId}:extend', 'POST', header, version)
        self.parameters = parameters


class ExtendDiskParameters(object):

    def __init__(self, regionId, diskId, diskSizeGB):
        """
        :param regionId: 地域ID
        :param diskId: 云硬盘ID
        :param diskSizeGB: 扩容后的云硬盘大小，单位为GiB
        """

        self.regionId = regionId
        self.diskId = diskId
        self.diskSizeGB = diskSizeGB

