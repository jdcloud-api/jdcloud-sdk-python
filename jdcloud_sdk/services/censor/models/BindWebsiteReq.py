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


class BindWebsiteReq(object):

    def __init__(self, scheme, host, hostInterval, homePage, homePageInterval, ):
        """
        :param scheme:  协议，http或https
        :param host:  域名，不含协议
        :param hostInterval:  全站检测频率，1d-1天，7d-7天
        :param homePage:  完整的首页地址，必须在host下
        :param homePageInterval:  首页检测间隔，eg:1h表示一小时，必须为整小时
        """

        self.scheme = scheme
        self.host = host
        self.hostInterval = hostInterval
        self.homePage = homePage
        self.homePageInterval = homePageInterval