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


class RuleMetricDetail(object):

    def __init__(self, calculateUnit=None, dimension=None, metric=None, metricName=None, product=None, serviceCode=None):
        """
        :param calculateUnit: (Optional) 指标的计算单位，比如bit/s、%、k等
        :param dimension: (Optional) 维度标识
        :param metric: (Optional) 监控项唯一标识，可根据DescribeMetricsForCreateAlarm接口查询各产品线可用的监控项（创建规则时使用Metric字段）。格式：metric:downsample
        :param metricName: (Optional) 监控项名称
        :param product: (Optional) 产品标识
        :param serviceCode: (Optional) 产品线标识
        """

        self.calculateUnit = calculateUnit
        self.dimension = dimension
        self.metric = metric
        self.metricName = metricName
        self.product = product
        self.serviceCode = serviceCode
