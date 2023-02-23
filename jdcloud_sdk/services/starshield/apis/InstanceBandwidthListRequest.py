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


class InstanceBandwidthListRequest(JDCloudRequest):
    """
    域名带宽列表，按带宽降序排列。查询范围最近6个月、查询最大跨度1个月。
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(InstanceBandwidthListRequest, self).__init__(
            '/instances/{instanceId}/instanceBandwidthList', 'POST', header, version)
        self.parameters = parameters


class InstanceBandwidthListParameters(object):

    def __init__(self,instanceId, queryMode, since, until, pageNumber, ):
        """
        :param instanceId: 实例标识
        :param queryMode: all - 所有
normal - 业务
mitigation - 缓解
cache - 缓存
origin - 回源

        :param since: 查询开始时间
        :param until: 查询结束时间
        :param pageNumber: 页码。当页码为-1时，返回所有记录
        """

        self.instanceId = instanceId
        self.queryMode = queryMode
        self.since = since
        self.until = until
        self.pageNumber = pageNumber
        self.pageSize = None

    def setPageSize(self, pageSize):
        """
        :param pageSize: (Optional) 每页显示记录数。当pageNumber的值大于0时，该字段必须赋值
        """
        self.pageSize = pageSize

