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


class WarningCfg(object):

    def __init__(self, id=None, userPin=None, wafInstanceId=None, domains=None, ruleType=None, ruleName=None, warnType=None, enable=None, detectSpan=None, detectThreshold=None, unit=None, detectUnit=None, contactWays=None, contactorPersons=None, contactorGroups=None, detectItems=None, mode=None, userPinScdn=None):
        """
        :param id: (Optional) 规则id
        :param userPin: (Optional) 用户名
        :param wafInstanceId: (Optional) WAF实例id
        :param domains: (Optional) 域名集
        :param ruleType: (Optional) 全局告警globle 自定义告警userdefine
        :param ruleName: (Optional) 规则名称
        :param warnType: (Optional) 告警类型
        :param enable: (Optional) 是否生效，0-不生效，1-生效
        :param detectSpan: (Optional) 检测周期
        :param detectThreshold: (Optional) 告警阈值
        :param unit: (Optional) 阈值单位，""-个数，"percent"-百分比，缺省为个数
        :param detectUnit: (Optional) 检测时长单位，hour/minute
        :param contactWays: (Optional) 告警方式
        :param contactorPersons: (Optional) 告警通知人
        :param contactorGroups: (Optional) 告警通知群组
        :param detectItems: (Optional) warnType为statusCode时为要检测的状态码
        :param mode: (Optional) 产品类型, 0waf, 1scdn
        :param userPinScdn: (Optional) scdn用户名
        """

        self.id = id
        self.userPin = userPin
        self.wafInstanceId = wafInstanceId
        self.domains = domains
        self.ruleType = ruleType
        self.ruleName = ruleName
        self.warnType = warnType
        self.enable = enable
        self.detectSpan = detectSpan
        self.detectThreshold = detectThreshold
        self.unit = unit
        self.detectUnit = detectUnit
        self.contactWays = contactWays
        self.contactorPersons = contactorPersons
        self.contactorGroups = contactorGroups
        self.detectItems = detectItems
        self.mode = mode
        self.userPinScdn = userPinScdn
