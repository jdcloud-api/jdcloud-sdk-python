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


class TrafficMonitor(object):

    def __init__(self, sourceCluster=None, rdtsProxy=None, targetProxy=None, diffPercent=None, currentTime=None):
        """
        :param sourceCluster: (Optional) 源端流量监控
        :param rdtsProxy: (Optional) 迁移代理流量监控
        :param targetProxy: (Optional) 目的端流量监控
        :param diffPercent: (Optional) 迁移代理ops与源端ops百分比
        :param currentTime: (Optional) 当前时间(ISO 8601标准的UTC时间，格式为：YYYY-MM-DDTHH:mm:ssZ)
        """

        self.sourceCluster = sourceCluster
        self.rdtsProxy = rdtsProxy
        self.targetProxy = targetProxy
        self.diffPercent = diffPercent
        self.currentTime = currentTime