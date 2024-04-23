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


class InstanceTrafficPackageUsage(object):

    def __init__(self, instanceId=None, trafficUsed=None, trafficPackageTotal=None, trafficPackageRemaining=None, trafficOverflow=None):
        """
        :param instanceId: (Optional) 实例ID
        :param trafficUsed: (Optional) 流量包当月周期内已使用流量
        :param trafficPackageTotal: (Optional) 流量包当月周期内的总流量
        :param trafficPackageRemaining: (Optional) 流量包当月周期内的剩余流量
        :param trafficOverflow: (Optional) 流量包当月周期内超出流量包额度的流量
        """

        self.instanceId = instanceId
        self.trafficUsed = trafficUsed
        self.trafficPackageTotal = trafficPackageTotal
        self.trafficPackageRemaining = trafficPackageRemaining
        self.trafficOverflow = trafficOverflow
