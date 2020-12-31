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


class Ipv6AddressSpec(object):

    def __init__(self, bandwidth, ipv6Addresses, charge, ):
        """
        :param bandwidth:  带宽, 范围[1,200] 单位Mbps
        :param ipv6Addresses:  IPv6地址
        :param charge:  计费配置
        """

        self.bandwidth = bandwidth
        self.ipv6Addresses = ipv6Addresses
        self.charge = charge
