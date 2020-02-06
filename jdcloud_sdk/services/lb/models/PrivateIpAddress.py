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


class PrivateIpAddress(object):

    def __init__(self, privateIpAddress=None, elasticIpId=None, elasticIpAddress=None):
        """
        :param privateIpAddress: (Optional) LoadBalancer的VIP(IPv4地址)
        :param elasticIpId: (Optional) 弹性公网IP ID
        :param elasticIpAddress: (Optional) 弹性公网IP地址
        """

        self.privateIpAddress = privateIpAddress
        self.elasticIpId = elasticIpId
        self.elasticIpAddress = elasticIpAddress
