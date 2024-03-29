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


class DescribeSlowSqlMetricRequest(JDCloudRequest):
    """
    查询慢sql次数及分布
    """

    def __init__(self, parameters, header=None, version="v2"):
        super(DescribeSlowSqlMetricRequest, self).__init__(
            '/regions/{regionId}/instance/{instanceGid}/sqlMetrics', 'GET', header, version)
        self.parameters = parameters


class DescribeSlowSqlMetricParameters(object):

    def __init__(self, regionId,instanceGid,metric, startTime, endTime):
        """
        :param regionId: 地域代码
        :param instanceGid: 实例ID
        :param metric: metric名称
        :param startTime: 查询开始时间，格式为：2021-11-11T15:04:05Z
        :param endTime: 查询截止时间，格式为：2021-11-11T15:04:05Z
        """

        self.regionId = regionId
        self.instanceGid = instanceGid
        self.metric = metric
        self.startTime = startTime
        self.endTime = endTime

