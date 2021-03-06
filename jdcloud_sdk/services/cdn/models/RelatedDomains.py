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


class RelatedDomains(object):

    def __init__(self, domainName=None, domainType=None, rtmpUrls=None, flvUrls=None, hlsUrls=None):
        """
        :param domainName: (Optional) 域名
        :param domainType: (Optional) （关联域名类型）publish或play
        :param rtmpUrls: (Optional) 该相关域名的rtmp格式
        :param flvUrls: (Optional) 该相关域名的flv格式
        :param hlsUrls: (Optional) 该相关域名的hls格式
        """

        self.domainName = domainName
        self.domainType = domainType
        self.rtmpUrls = rtmpUrls
        self.flvUrls = flvUrls
        self.hlsUrls = hlsUrls
