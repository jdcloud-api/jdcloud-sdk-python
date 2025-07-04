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


class FetchDataRequest(JDCloudRequest):
    """
    获取待爬取链接
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(FetchDataRequest, self).__init__(
            '/fetchData', 'GET', header, version)
        self.parameters = parameters


class FetchDataParameters(object):

    def __init__(self,):
        """
        """

        self.crawlerId = None
        self.count = None

    def setCrawlerId(self, crawlerId):
        """
        :param crawlerId: (Optional) 自定义客户端名称
        """
        self.crawlerId = crawlerId

    def setCount(self, count):
        """
        :param count: (Optional) 获取链接数量， 默认为10
        """
        self.count = count

