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


class IotDataStatsVO(object):

    def __init__(self, totalThingTypes=None, directConnectThingTypes=None, connectAgentThingTypes=None, indirectConnectAgentThingTypes=None, totalDevices=None, directConnectDevices=None, connectAgentDevices=None, totalOnlineDevices=None, onlineDirectConnectDevices=None, onlineConnectAgentDevices=None, onlineIndirectConnectDevices=None):
        """
        :param totalThingTypes: (Optional) 物类型总数
        :param directConnectThingTypes: (Optional) 直连终端物类型总数
        :param connectAgentThingTypes: (Optional) 直连终端物类型总数
        :param indirectConnectAgentThingTypes: (Optional) 非直连在线终端总数
        :param totalDevices: (Optional) 总设备数
        :param directConnectDevices: (Optional) 直连总设备数
        :param connectAgentDevices: (Optional) 连接终端设备数
        :param totalOnlineDevices: (Optional) 总在线设备数
        :param onlineDirectConnectDevices: (Optional) 在线直接设备数
        :param onlineConnectAgentDevices: (Optional) 在线终端数
        :param onlineIndirectConnectDevices: (Optional) 在线非直连设备数
        """

        self.totalThingTypes = totalThingTypes
        self.directConnectThingTypes = directConnectThingTypes
        self.connectAgentThingTypes = connectAgentThingTypes
        self.indirectConnectAgentThingTypes = indirectConnectAgentThingTypes
        self.totalDevices = totalDevices
        self.directConnectDevices = directConnectDevices
        self.connectAgentDevices = connectAgentDevices
        self.totalOnlineDevices = totalOnlineDevices
        self.onlineDirectConnectDevices = onlineDirectConnectDevices
        self.onlineConnectAgentDevices = onlineConnectAgentDevices
        self.onlineIndirectConnectDevices = onlineIndirectConnectDevices
