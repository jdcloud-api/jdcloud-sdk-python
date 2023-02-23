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


class InstanceBandwidthDateHistogramRequest(JDCloudRequest):
    """
    带宽图。查询范围最近6个月、查询最大跨度1个月。
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(InstanceBandwidthDateHistogramRequest, self).__init__(
            '/instances/{instanceId}/instanceBandwidthDateHistogram', 'POST', header, version)
        self.parameters = parameters


class InstanceBandwidthDateHistogramParameters(object):

    def __init__(self,instanceId, queryMode, since, until):
        """
        :param instanceId: 实例标识
        :param queryMode: all - 所有
normal - 业务
mitigation - 缓解
cache - 缓存
origin - 回源

        :param since: 查询开始时间
        :param until: 查询结束时间
        """

        self.instanceId = instanceId
        self.queryMode = queryMode
        self.since = since
        self.until = until

