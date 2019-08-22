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


class RemoveDeviceRequest(JDCloudRequest):
    """
    删除设备
    """

    def __init__(self, parameters, header=None, version="v2"):
        super(RemoveDeviceRequest, self).__init__(
            '/regions/{regionId}/instances/{instanceId}/products/{productKey}/device/{deviceName}:delete', 'DELETE', header, version)
        self.parameters = parameters


class RemoveDeviceParameters(object):

    def __init__(self, deviceName, instanceId, regionId, productKey, ):
        """
        :param deviceName: 设备名称
        :param instanceId: 设备归属的实例ID
        :param regionId: 设备归属的实例所在区域
        :param productKey: 产品Key
        """

        self.deviceName = deviceName
        self.instanceId = instanceId
        self.regionId = regionId
        self.productKey = productKey

