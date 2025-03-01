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


class LogCountOrAggregateSearchParam(object):

    def __init__(self, pin, product, instance=None, logType=None, ip=None, podName=None, namespace=None, cluster=None, containerName=None, filePath=None, startTime=None, endTime=None, direction=None, limit=None, step=None, streamFilter=None, lineFilter=None, fmtFilter=None, metric=None, queryType=None, duration=None, groupBy=None):
        """
        :param pin:  租户，必填
        :param product:  产品，必填
        :param instance: (Optional) 实例
        :param logType: (Optional) 日志类型
        :param ip: (Optional) ip
        :param podName: (Optional) pod name
        :param namespace: (Optional) 命名空间
        :param cluster: (Optional) 集群
        :param containerName: (Optional) 容器名
        :param filePath: (Optional) 文件路径
        :param startTime: (Optional) 开始时间纳秒数字，默认一小时前
        :param endTime: (Optional) 结束时间纳秒数字，默认现在
        :param direction: (Optional) 正序：FORWARD、倒序：BACKWARD，默认BACKWARD
        :param limit: (Optional) 查询数量数字，默认100
        :param step: (Optional) 步长时间（单位：秒），10、0.5
        :param streamFilter: (Optional) label过滤
        :param lineFilter: (Optional) 行过滤
        :param fmtFilter: (Optional) 格式化过滤条件
        :param metric: (Optional) 指标函数及参数
        :param queryType: (Optional) 检索类型枚举：range
        :param duration: (Optional) 时间区间1s、1m、1h
        :param groupBy: (Optional) 分组字段，逗号分隔
        """

        self.pin = pin
        self.product = product
        self.instance = instance
        self.logType = logType
        self.ip = ip
        self.podName = podName
        self.namespace = namespace
        self.cluster = cluster
        self.containerName = containerName
        self.filePath = filePath
        self.startTime = startTime
        self.endTime = endTime
        self.direction = direction
        self.limit = limit
        self.step = step
        self.streamFilter = streamFilter
        self.lineFilter = lineFilter
        self.fmtFilter = fmtFilter
        self.metric = metric
        self.queryType = queryType
        self.duration = duration
        self.groupBy = groupBy
