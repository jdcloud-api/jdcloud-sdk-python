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


class DescribeOpenDevicesDataRequest(JDCloudRequest):
    """
    查询开放设备数据信息接口
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeOpenDevicesDataRequest, self).__init__(
            '/openDevicesData', 'GET', header, version)
        self.parameters = parameters


class DescribeOpenDevicesDataParameters(object):

    def __init__(self,deviceType):
        """
        :param deviceType: 设备类型
        """

        self.deviceCodes = None
        self.deviceType = deviceType

    def setDeviceCodes(self, deviceCodes):
        """
        :param deviceCodes: (Optional) 设备编码,支持多个deviceCode批量查询，每个id用英文竖线分隔
        """
        self.deviceCodes = deviceCodes

