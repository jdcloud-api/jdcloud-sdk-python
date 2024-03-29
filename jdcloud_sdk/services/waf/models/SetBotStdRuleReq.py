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


class SetBotStdRuleReq(object):

    def __init__(self, domain, botType, action=None, disable=None):
        """
        :param domain:  域名
        :param botType:  要设置的bot类型，list列表中的值
        :param action: (Optional) 动作配置
        :param disable: (Optional) 0-启用 1-禁用
        """

        self.domain = domain
        self.botType = botType
        self.action = action
        self.disable = disable
