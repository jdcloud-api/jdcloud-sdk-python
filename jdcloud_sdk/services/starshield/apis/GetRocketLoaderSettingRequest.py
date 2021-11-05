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


class GetRocketLoaderSettingRequest(JDCloudRequest):
    """
    Rocket Loader是一个通用的异步JavaScript优化，它优先渲染你的内容同时异步加载你的网站的Javascript。
开启Rocket Loader将立即改善网页的渲染时间，有时以首次绘制时间（TTFP）以及window.onload时间（假设页面上有JavaScript）来衡量，这对你的搜索排名会产生积极影响。
当打开时，Rocket Loader将自动推迟加载你的HTML中引用的所有Javascript，而不需要配置。

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(GetRocketLoaderSettingRequest, self).__init__(
            '/zones/{zone_identifier}/settings$$rocket_loader', 'GET', header, version)
        self.parameters = parameters


class GetRocketLoaderSettingParameters(object):

    def __init__(self, zone_identifier, ):
        """
        :param zone_identifier: 
        """

        self.zone_identifier = zone_identifier

