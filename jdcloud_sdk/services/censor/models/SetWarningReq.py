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


class SetWarningReq(object):

    def __init__(self, logTypes, riskLevels, notifyTime, enable=None, realTimeNotify=None, contactWays=None, contactorPersons=None, contactorGroups=None):
        """
        :param enable: (Optional) 是否开启开关
        :param realTimeNotify: (Optional) 是否开启实时消息提醒
        :param logTypes:  
        :param riskLevels:  
        :param notifyTime:  通知时间，eg:"10:00:00"
        :param contactWays: (Optional) 通知方式
        :param contactorPersons: (Optional) 告警通知人
        :param contactorGroups: (Optional) 告警通知群组
        """

        self.enable = enable
        self.realTimeNotify = realTimeNotify
        self.logTypes = logTypes
        self.riskLevels = riskLevels
        self.notifyTime = notifyTime
        self.contactWays = contactWays
        self.contactorPersons = contactorPersons
        self.contactorGroups = contactorGroups