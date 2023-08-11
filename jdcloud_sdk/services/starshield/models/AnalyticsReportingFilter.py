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


class AnalyticsReportingFilter(object):

    def __init__(self, name=None, operator=None, values=None):
        """
        :param name: (Optional) 过滤条件的名称。有效值：
HttpHost/URI/ResponseStatusCode/ClientDeviceType/
ServedBy/CacheStatus/ClientHttpMethod/ResponseContentType/
ASN/IP/ClientHttpProtocol/FirewallSource/UserAgent/RuleId

        :param operator: (Optional) 过滤条件的操作符
        :param values: (Optional) 过滤条件的值
        """

        self.name = name
        self.operator = operator
        self.values = values
