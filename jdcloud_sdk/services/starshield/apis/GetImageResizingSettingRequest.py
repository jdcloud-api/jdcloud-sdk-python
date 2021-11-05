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


class GetImageResizingSettingRequest(JDCloudRequest):
    """
    图像调整为通过星盾的网络提供的图像提供按需调整、转换和优化。
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(GetImageResizingSettingRequest, self).__init__(
            '/zones/{zone_identifier}/settings$$image_resizing', 'GET', header, version)
        self.parameters = parameters


class GetImageResizingSettingParameters(object):

    def __init__(self, zone_identifier, ):
        """
        :param zone_identifier: 
        """

        self.zone_identifier = zone_identifier

