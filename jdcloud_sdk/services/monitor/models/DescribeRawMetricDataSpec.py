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


class DescribeRawMetricDataSpec(object):

    def __init__(self, aggregator, downsample, end, filters, metric, start, ):
        """
        :param aggregator:  多维度聚合方式，即多条时序数据聚合为一条时序数据的方式，支持zimsum，avg，max，min，参考opentsdb协议http://opentsdb.net/docs/build/html/user_guide/query/aggregators.html
        :param downsample:  采样方式即时间维度的聚合, 比如5m-sum-zero。若要将时间范围内的数据聚合为一个值，用0all-sum。注意：采样周期不得低于5分钟。参考opentsdb协议http://opentsdb.net/docs/build/html/user_guide/query/downsampling.html
        :param end:  查询结束时间, 秒级时间戳, 查询时间段不得超过31天
        :param filters:  监控指标数据的维度信息,根据filters来筛选指标数据不同的维度,至少需要包含一个
        :param metric:  metric
        :param start:  查询开始时间, 秒级时间戳, 查询时间段不得超过31天, 最早开始时间不得早于45天前
        """

        self.aggregator = aggregator
        self.downsample = downsample
        self.end = end
        self.filters = filters
        self.metric = metric
        self.start = start
