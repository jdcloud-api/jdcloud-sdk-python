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


class ZoneBandwidthMultiDateHistogramRequest(JDCloudRequest):
    """
    多指标的带宽图。查询范围最近6个月、查询最大跨度1个月。
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(ZoneBandwidthMultiDateHistogramRequest, self).__init__(
            '/zones/{zone_identifier}/zoneBandwidthMultiDateHistogram', 'POST', header, version)
        self.parameters = parameters


class ZoneBandwidthMultiDateHistogramParameters(object):

    def __init__(self,zone_identifier, queryModes, zoneName, since, until):
        """
        :param zone_identifier: 域名标识
        :param queryModes: all - 所有
normal - 业务
mitigation - 缓解
cache - 缓存
origin - 回源
all/normal/mitigation/cache/origin的任意组合

        :param zoneName: 域名
        :param since: 开始时间
        :param until: 结束时间
        """

        self.zone_identifier = zone_identifier
        self.queryModes = queryModes
        self.zoneName = zoneName
        self.since = since
        self.until = until

