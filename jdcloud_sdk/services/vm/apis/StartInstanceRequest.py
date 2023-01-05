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


class StartInstanceRequest(JDCloudRequest):
    """
    
启动云主机实例。

详细操作说明请参考帮助文档：[启动实例](https://docs.jdcloud.com/cn/virtual-machines/start-instance)

## 接口说明
- 实例状态必须为停止 `stopped` 状态，同时实例没有正在进行中的任务时才可以启动。
- 如果实例为停机不计费模式，启动时有可能因为库存资源不足而导致无法启动。
- 如果云主机实例已欠费或已到期，则无法启动。
- 如果实例系统盘是云硬盘，启动之前请确保系统盘处于正常挂载状态。

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(StartInstanceRequest, self).__init__(
            '/regions/{regionId}/instances/{instanceId}:startInstance', 'POST', header, version)
        self.parameters = parameters


class StartInstanceParameters(object):

    def __init__(self,regionId, instanceId):
        """
        :param regionId: 地域ID。
        :param instanceId: 云主机ID。
        """

        self.regionId = regionId
        self.instanceId = instanceId

