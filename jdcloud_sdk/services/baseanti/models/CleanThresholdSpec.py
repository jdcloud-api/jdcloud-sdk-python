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


class CleanThresholdSpec(object):

    def __init__(self, cleanThresholdBps, cleanThresholdPps, ):
        """
        :param cleanThresholdBps:  触发清洗的流量速率, 单位 bps. 取值范围由 <a href='http://docs.jdcloud.com/anti-ddos-basic/api/describeipcleanthresholdrange'>describeIpCleanThresholdRange</a> 接口查询可知
        :param cleanThresholdPps:  触发清洗的报文流量速率, 单位 bps. 取值范围由 <a href='http://docs.jdcloud.com/anti-ddos-basic/api/describeipcleanthresholdrange'>describeIpCleanThresholdRange</a> 接口查询可知
        """

        self.cleanThresholdBps = cleanThresholdBps
        self.cleanThresholdPps = cleanThresholdPps
