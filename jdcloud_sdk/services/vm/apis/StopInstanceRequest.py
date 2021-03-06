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


class StopInstanceRequest(JDCloudRequest):
    """
    停止单个云主机，只能停止<b>running</b>状态的云主机，云主机没有正在进行中的任务才可停止

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(StopInstanceRequest, self).__init__(
            '/regions/{regionId}/instances/{instanceId}:stopInstance', 'POST', header, version)
        self.parameters = parameters


class StopInstanceParameters(object):

    def __init__(self, regionId, instanceId, ):
        """
        :param regionId: 地域ID
        :param instanceId: 云主机ID
        """

        self.regionId = regionId
        self.instanceId = instanceId
        self.chargeOnStopped = None

    def setChargeOnStopped(self, chargeOnStopped):
        """
        :param chargeOnStopped: (Optional) 关机模式，只支持云盘做系统盘的按配置计费云主机keepCharging：关机后继续计费；stopCharging：关机后停止计费。
        """
        self.chargeOnStopped = chargeOnStopped

