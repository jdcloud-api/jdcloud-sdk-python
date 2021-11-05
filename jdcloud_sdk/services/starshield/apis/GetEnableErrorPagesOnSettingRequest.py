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


class GetEnableErrorPagesOnSettingRequest(JDCloudRequest):
    """
    星盾将代源服务器上任何 502、504 错误的客户错误页面，而不是显示默认的星盾错误页面。这不适用于 522 错误，并且仅限于企业级域。

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(GetEnableErrorPagesOnSettingRequest, self).__init__(
            '/zones/{zone_identifier}/settings$$origin_error_page_pass_thru', 'GET', header, version)
        self.parameters = parameters


class GetEnableErrorPagesOnSettingParameters(object):

    def __init__(self, zone_identifier, ):
        """
        :param zone_identifier: 
        """

        self.zone_identifier = zone_identifier

