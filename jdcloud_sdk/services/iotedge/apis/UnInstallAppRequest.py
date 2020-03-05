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


class UnInstallAppRequest(JDCloudRequest):
    """
    卸载安装的APP
    """

    def __init__(self, parameters, header=None, version="v2"):
        super(UnInstallAppRequest, self).__init__(
            '/regions/{regionId}/instances/{instanceId}/hardwareId/{hardwareId}/os/{osId}/edgeApp:unInstallApp', 'POST', header, version)
        self.parameters = parameters


class UnInstallAppParameters(object):

    def __init__(self, instanceId, regionId, hardwareId, osId, edgeName, appName, deployAppId):
        """
        :param instanceId: 设备归属的实例ID
        :param regionId: 设备归属的实例所在区域
        :param hardwareId: 硬件版本
        :param osId: OSID
        :param edgeName: Edge名称
        :param appName: APP名称
        :param deployAppId: 部署ID
        """

        self.instanceId = instanceId
        self.regionId = regionId
        self.hardwareId = hardwareId
        self.osId = osId
        self.edgeName = edgeName
        self.appName = appName
        self.deployAppId = deployAppId

