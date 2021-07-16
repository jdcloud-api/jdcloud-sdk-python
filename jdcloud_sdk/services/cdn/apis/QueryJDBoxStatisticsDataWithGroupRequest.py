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


class QueryJDBoxStatisticsDataWithGroupRequest(JDCloudRequest):
    """
    无线宝按group查询的统计接口
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(QueryJDBoxStatisticsDataWithGroupRequest, self).__init__(
            '/jdBoxStatisticsWithGroup', 'POST', header, version)
        self.parameters = parameters


class QueryJDBoxStatisticsDataWithGroupParameters(object):

    def __init__(self, ):
        """
        """

        self.startTime = None
        self.endTime = None
        self.groupBy = None
        self.fields = None
        self.area = None
        self.isp = None
        self.period = None
        self.category = None
        self.macAddr = None
        self.pluginPin = None

    def setStartTime(self, startTime):
        """
        :param startTime: (Optional) 查询起始时间,时间戳
        """
        self.startTime = startTime

    def setEndTime(self, endTime):
        """
        :param endTime: (Optional) 查询截止时间,时间戳
        """
        self.endTime = endTime

    def setGroupBy(self, groupBy):
        """
        :param groupBy: (Optional) 取值范围：area，isp，pin ,mac_addr，category，多个用,隔开,多个维度的查询，必须要限制较短的时间间隔
        """
        self.groupBy = groupBy

    def setFields(self, fields):
        """
        :param fields: (Optional) 查询的字段，取值范围(avgbandwidth,pv,flow)。多个用逗号分隔。默认为空，表示查询带宽流量
        """
        self.fields = fields

    def setArea(self, area):
        """
        :param area: (Optional) 区域
        """
        self.area = area

    def setIsp(self, isp):
        """
        :param isp: (Optional) 运营商
        """
        self.isp = isp

    def setPeriod(self, period):
        """
        :param period: (Optional) 查询周期，当前取值范围：“oneMin,fiveMin”，分别表示1min，5min。默认为空，表示fiveMin
        """
        self.period = period

    def setCategory(self, category):
        """
        :param category: (Optional) 业务类型
        """
        self.category = category

    def setMacAddr(self, macAddr):
        """
        :param macAddr: (Optional) 设备id
        """
        self.macAddr = macAddr

    def setPluginPin(self, pluginPin):
        """
        :param pluginPin: (Optional) 插件pin
        """
        self.pluginPin = pluginPin
