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

from jdcloud_sdk.core.jdcloudrequest import JDCloudRequest


class CheckWhetherIpBelongToJCloudRequest(JDCloudRequest):
    """
    获取所有上层节点的ip，仅支持中国境内上层节点IP地址查询
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(CheckWhetherIpBelongToJCloudRequest, self).__init__(
            '/ip:whetherBelongToJCloud', 'POST', header, version)
        self.parameters = parameters


class CheckWhetherIpBelongToJCloudParameters(object):

    def __init__(self, ):
        """
        """

        self.ips = None

    def setIps(self, ips):
        """
        :param ips: (Optional) 
        """
        self.ips = ips

