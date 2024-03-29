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


class PanelMetricForCreate(object):

    def __init__(self, metric, aggregator=None, downsample=None):
        """
        :param aggregator: (Optional) 聚合方式，跨资源计算方式
        :param downsample: (Optional) 采样方式，同一资源计算方式，如一分钟两个点，计算一分钟内这两个点的平均值得出一个点
        :param metric:  metric
        """

        self.aggregator = aggregator
        self.downsample = downsample
        self.metric = metric
