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


class AgentRegisterRequest(JDCloudRequest):
    """
    Agent 注册接口
    """

    def __init__(self, parameters, header=None, version="v2"):
        super(AgentRegisterRequest, self).__init__(
            '/regions/{regionId}/agent', 'POST', header, version)
        self.parameters = parameters


class AgentRegisterParameters(object):

    def __init__(self, regionId,mac, stat, ):
        """
        :param regionId: 地域代码，取值范围参见[《各地域及可用区对照表》]
        :param mac: agent的 MAC
        :param stat: agent的状态
        """

        self.regionId = regionId
        self.ip = None
        self.mac = mac
        self.hostname = None
        self.stat = stat
        self.ver = None

    def setIp(self, ip):
        """
        :param ip: (Optional) agent的IP
        """
        self.ip = ip

    def setHostname(self, hostname):
        """
        :param hostname: (Optional) agent的hostname
        """
        self.hostname = hostname

    def setVer(self, ver):
        """
        :param ver: (Optional) agent的版本号
        """
        self.ver = ver

