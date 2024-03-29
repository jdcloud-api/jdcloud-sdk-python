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


class BatchDescribeMetricDataRequest(JDCloudRequest):
    """
    查看某资源多个监控项数据，metric介绍：<a href="https://docs.jdcloud.com/cn/monitoring/metrics">Metrics</a>，可以使用接口<a href="https://docs.jdcloud.com/cn/monitoring/metrics">describeMetrics</a>：查询产品线可用的metric列表。
    """

    def __init__(self, parameters, header=None, version="v2"):
        super(BatchDescribeMetricDataRequest, self).__init__(
            '/regions/{regionId}/ydMetricsData', 'GET', header, version)
        self.parameters = parameters


class BatchDescribeMetricDataParameters(object):

    def __init__(self,regionId, resourceId, filters):
        """
        :param regionId: 地域 Id
        :param resourceId: 资源的uuid
        :param filters: 自定义过滤标签，查询时必须在filters中指定要查询的metric，支持多个metric。如：  name='metric',values=["metric1","metric2"]
        """

        self.regionId = regionId
        self.aggrType = None
        self.downSampleType = None
        self.startTime = None
        self.endTime = None
        self.timeInterval = None
        self.tags = None
        self.groupBy = None
        self.rate = None
        self.serviceCode = None
        self.dimension = None
        self.resourceId = resourceId
        self.multiResources = None
        self.filters = filters

    def setAggrType(self, aggrType):
        """
        :param aggrType: (Optional) 聚合方式，用于不同时间轴上的聚合。如balance产品同一个resourceId下存在port=80和port=8080等多种维度。可选值参考:sum、avg、min、max
        """
        self.aggrType = aggrType

    def setDownSampleType(self, downSampleType):
        """
        :param downSampleType: (Optional) 采样方式，用于在时间轴维度上将聚合周期内的数据聚合为一个点。可选值参考：sum(聚合周期内的数据求和)、avg(求平均)、last(最新值)、min(最小值)、max(最大值)
        """
        self.downSampleType = downSampleType

    def setStartTime(self, startTime):
        """
        :param startTime: (Optional) 查询时间范围的开始时间， UTC时间，格式：2016-12-11T00:00:00+0800（注意在url中+要转译为%2B故url中为2016-12-11T00:00:00%2B0800）
        """
        self.startTime = startTime

    def setEndTime(self, endTime):
        """
        :param endTime: (Optional) 查询时间范围的结束时间， UTC时间，格式：2016-12-11T00:00:00+0800（为空时，将由startTime与timeInterval计算得出）（注意在url中+要转译为%2B故url中为2016-12-11T00:00:00%2B0800）
        """
        self.endTime = endTime

    def setTimeInterval(self, timeInterval):
        """
        :param timeInterval: (Optional) 时间间隔：1h，6h，12h，1d，3d，7d，14d，固定时间间隔，timeInterval默认为1h，当前时间往 前1h
        """
        self.timeInterval = timeInterval

    def setTags(self, tags):
        """
        :param tags: (Optional) 监控指标数据的维度信息,根据tags来筛选指标数据不同的维度
        """
        self.tags = tags

    def setGroupBy(self, groupBy):
        """
        :param groupBy: (Optional) 是否对查询的tags分组
        """
        self.groupBy = groupBy

    def setRate(self, rate):
        """
        :param rate: (Optional) 是否求速率
        """
        self.rate = rate

    def setServiceCode(self, serviceCode):
        """
        :param serviceCode: (Optional) 资源的类型，取值vm, lb, ip, database 等,<a href="https://docs.jdcloud.com/cn/monitoring/api/describeservices?content=API&SOP=JDCloud">describeServices</a>：查询己接入云监控的产品线列表
        """
        self.serviceCode = serviceCode

    def setDimension(self, dimension):
        """
        :param dimension: (Optional) 资源的维度。查询serviceCode下可用的维度请使用describeServices接口
        """
        self.dimension = dimension

    def setMultiResources(self, multiResources):
        """
        :param multiResources: (Optional) 是否跨资源查询，默认为false。当该字段为false时，取resourceId字段进行查询；当该子弹为true时，忽略resourceId字段，从tags中取resourceId作为实际的多资源id处理。
        """
        self.multiResources = multiResources

