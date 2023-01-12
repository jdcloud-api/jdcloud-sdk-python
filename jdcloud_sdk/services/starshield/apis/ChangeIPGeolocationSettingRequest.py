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


class ChangeIPGeolocationSettingRequest(JDCloudRequest):
    """
    启用IP地理定位，让星盾对您网站的访问者进行地理定位，并将国家代码传递给您。
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(ChangeIPGeolocationSettingRequest, self).__init__(
            '/zones/{zone_identifier}/settings$$ip_geolocation', 'PATCH', header, version)
        self.parameters = parameters


class ChangeIPGeolocationSettingParameters(object):

    def __init__(self,zone_identifier, ):
        """
        :param zone_identifier: 
        """

        self.zone_identifier = zone_identifier
        self.value = None

    def setValue(self, value):
        """
        :param value: (Optional) on - 开启；off - 关闭
        """
        self.value = value

