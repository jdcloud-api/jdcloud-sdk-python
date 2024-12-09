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


class LogDetailPublicSearchParam(object):

    def __init__(self, searchId=None, logType=None, ip=None, podName=None, namespace=None, cluster=None, containerName=None, filePath=None, startTime=None, endTime=None, direction=None, limit=None, step=None, streamFilter=None, lineFilter=None, fmtFilter=None):
        """
        :param searchId: (Optional) UUID，同一批次保持一致，必填
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
        """

        self.searchId = searchId
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