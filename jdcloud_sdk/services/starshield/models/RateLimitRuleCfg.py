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


class RateLimitRuleCfg(object):

    def __init__(self, name, id=None, host=None, url=None, ip=None, rate=None, burst=None, matchAction=None, redirection=None):
        """
        :param id: (Optional) 序号id,更新时需要
        :param name:  规则名称
        :param host: (Optional) 限速host配置
        :param url: (Optional) 限速url配置
        :param ip: (Optional) ip配置
        :param rate: (Optional) 限速大小
        :param burst: (Optional) 限速burst大小
        :param matchAction: (Optional) 匹配动作, 拦截:forbidden,redirect 人机识别:verify@jscookie,verify@captcha,verify@rdtcookie 观察:notice
        :param redirection: (Optional) 跳转地址，matchAction为redirect时必须为当前实例下的域名的url，forbidden时为自定义页面名称
        """

        self.id = id
        self.name = name
        self.host = host
        self.url = url
        self.ip = ip
        self.rate = rate
        self.burst = burst
        self.matchAction = matchAction
        self.redirection = redirection
