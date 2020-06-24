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


class DispatchRule(object):

    def __init__(self, id=None, name=None, cname=None, serviceIp=None, innerIps=None, dispatchThresholdMbps=None, dispatchThresholdPps=None, status=None):
        """
        :param id: (Optional) 规则 Id
        :param name: (Optional) 规则名称
        :param cname: (Optional) 规则的 CNAME
        :param serviceIp: (Optional) 高防 IP
        :param innerIps: (Optional) 云内IP
        :param dispatchThresholdMbps: (Optional) 触发调度的流量阈值, 单位 Mbps
        :param dispatchThresholdPps: (Optional) 触发调度的报文阈值, 单位 pps
        :param status: (Optional) 0: 防御状态, 1: 回源状态
        """

        self.id = id
        self.name = name
        self.cname = cname
        self.serviceIp = serviceIp
        self.innerIps = innerIps
        self.dispatchThresholdMbps = dispatchThresholdMbps
        self.dispatchThresholdPps = dispatchThresholdPps
        self.status = status