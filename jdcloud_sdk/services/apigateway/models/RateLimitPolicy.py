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


class RateLimitPolicy(object):

    def __init__(self, policyId=None, policyName=None, timeUnit=None, apiLimitCount=None, userLimitCount=None, appLimitCount=None, userId=None, pin=None, description=None, bindGroups=None):
        """
        :param policyId: (Optional) 策略id
        :param policyName: (Optional) 策略名称
        :param timeUnit: (Optional) 时间单位
        :param apiLimitCount: (Optional) api流量限制次数
        :param userLimitCount: (Optional) 用户流量限制次数
        :param appLimitCount: (Optional) 应用流量限制次数
        :param userId: (Optional) 用户ID
        :param pin: (Optional) 用户名
        :param description: (Optional) 描述
        :param bindGroups: (Optional) 绑定分组，以逗号隔开的分组id存储，以逗号隔开的分组name返回
        """

        self.policyId = policyId
        self.policyName = policyName
        self.timeUnit = timeUnit
        self.apiLimitCount = apiLimitCount
        self.userLimitCount = userLimitCount
        self.appLimitCount = appLimitCount
        self.userId = userId
        self.pin = pin
        self.description = description
        self.bindGroups = bindGroups
