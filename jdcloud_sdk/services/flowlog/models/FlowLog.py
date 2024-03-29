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


class FlowLog(object):

    def __init__(self, flowLogId=None, flowLogName=None, description=None, flowLogType=None, flowLogStatus=None, collectResources=None, collectTrafficType=None, collectInterval=None, storageRegionId=None, storageType=None, storageId=None, createdTime=None):
        """
        :param flowLogId: (Optional) 流日志ID
        :param flowLogName: (Optional) 流日志名称，只允许输入中文、数字、大小写字母、英文下划线“_”及中划线“-”，不允许为空且不超过32字符
        :param description: (Optional) 描述，允许输入UTF-8编码下的全部字符，不超过256字符
        :param flowLogType: (Optional) 流日志类型
PORT：采集资源包括云主机、弹性网卡

        :param flowLogStatus: (Optional) 流日志的状态
RUNNING：采集中
STOPPED：已停止采集

        :param collectResources: (Optional) 采集资源列表
        :param collectTrafficType: (Optional) 采集流量类型
ALL：记录指定资源的全部流量。
ACCEPT：记录指定资源被安全组、网络ACL均接受的流量。
REJECT：记录指定资源被安全组或网络ACL拒绝的流量。

        :param collectInterval: (Optional) 流日志采集时间间隔。单位：分钟。取值：1、5、10
        :param storageRegionId: (Optional) 流日志的存储服务所在地域
        :param storageType: (Optional) 流日志的存储服务类型
LOG：日志服务

        :param storageId: (Optional) 流日志数据存储服务ID
        :param createdTime: (Optional) 流日志创建时间
        """

        self.flowLogId = flowLogId
        self.flowLogName = flowLogName
        self.description = description
        self.flowLogType = flowLogType
        self.flowLogStatus = flowLogStatus
        self.collectResources = collectResources
        self.collectTrafficType = collectTrafficType
        self.collectInterval = collectInterval
        self.storageRegionId = storageRegionId
        self.storageType = storageType
        self.storageId = storageId
        self.createdTime = createdTime
