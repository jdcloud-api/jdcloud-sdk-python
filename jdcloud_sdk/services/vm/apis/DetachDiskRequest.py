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


class DetachDiskRequest(JDCloudRequest):
    """
    
为一台云主机缷载云硬盘

详细操作说明请参考帮助文档：[缷载云硬盘](https://docs.jdcloud.com/cn/virtual-machines/detach-cloud-disk)

## 接口说明
- 云主机和云硬盘都没有正在进行中的的任务时才可以操作。
- 云主机状态必须是 `running` 或 `stopped` 状态。操作系统盘时必须先停止实例。

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DetachDiskRequest, self).__init__(
            '/regions/{regionId}/instances/{instanceId}:detachDisk', 'POST', header, version)
        self.parameters = parameters


class DetachDiskParameters(object):

    def __init__(self,regionId, instanceId, diskId, ):
        """
        :param regionId: 地域ID。
        :param instanceId: 云主机ID。
        :param diskId: 云硬盘ID。
        """

        self.regionId = regionId
        self.instanceId = instanceId
        self.diskId = diskId
        self.force = None

    def setForce(self, force):
        """
        :param force: (Optional) 是否强制缷载，默认False。
如果此参数传值为True，数据盘的IO会被强制断掉。

        """
        self.force = force

