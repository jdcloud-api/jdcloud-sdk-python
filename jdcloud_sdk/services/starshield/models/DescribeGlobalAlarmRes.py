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


class DescribeGlobalAlarmRes(object):

    def __init__(self, id=None, alarmType=None, statCycle=None, statCycleUnit=None, statThreshold=None, alarmTimesLimit=None, smsEnable=None, emailEnable=None, webMsEnable=None, enable=None, contactUsers=None, contactGroups=None):
        """
        :param id: (Optional) 告警规则ID
        :param alarmType: (Optional) 告警类型 WEB_ATTACK->网站攻击 CC_ATTACK->CC攻击 DDOS_ATTACK->DDOS攻击 STATUS_CODE_ERROR->状态码错误
        :param statCycle: (Optional) 统计周期
        :param statCycleUnit: (Optional) 统计周期单位
        :param statThreshold: (Optional) 统计阈值
        :param alarmTimesLimit: (Optional) 告警次数限制
        :param smsEnable: (Optional) 发送短信开关
        :param emailEnable: (Optional) 发送邮件开关
        :param webMsEnable: (Optional) 发送站内信开关
        :param enable: (Optional) 规则开关
        :param contactUsers: (Optional) 告警联系人
        :param contactGroups: (Optional) 告警联系组
        """

        self.id = id
        self.alarmType = alarmType
        self.statCycle = statCycle
        self.statCycleUnit = statCycleUnit
        self.statThreshold = statThreshold
        self.alarmTimesLimit = alarmTimesLimit
        self.smsEnable = smsEnable
        self.emailEnable = emailEnable
        self.webMsEnable = webMsEnable
        self.enable = enable
        self.contactUsers = contactUsers
        self.contactGroups = contactGroups
