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


class CreateCustomPageRequest(JDCloudRequest):
    """
    添加自定义页面
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(CreateCustomPageRequest, self).__init__(
            '/regions/{regionId}/instances/{instanceId}/customPages', 'POST', header, version)
        self.parameters = parameters


class CreateCustomPageParameters(object):

    def __init__(self, regionId,instanceId,customPageSpec):
        """
        :param regionId: 区域 ID, 高防不区分区域, 传 cn-north-1 即可
        :param instanceId: 实例 ID
        :param customPageSpec: 添加自定义页面请求参数
        """

        self.regionId = regionId
        self.instanceId = instanceId
        self.customPageSpec = customPageSpec

