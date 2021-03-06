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


class RiskEventVarsCfg(object):

    def __init__(self, wafInstanceId=None, domain=None, name=None, event=None, vars=None, policys=None):
        """
        :param wafInstanceId: (Optional) WAF实例id
        :param domain: (Optional) 域名
        :param name: (Optional) 名称
        :param event: (Optional) 事件信息
        :param vars: (Optional) 变量信息
        :param policys: (Optional) 策略信息
        """

        self.wafInstanceId = wafInstanceId
        self.domain = domain
        self.name = name
        self.event = event
        self.vars = vars
        self.policys = policys
