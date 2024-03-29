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


class DisableRulesReq(object):

    def __init__(self, wafInstanceId, domain, ruleType, disable=None, ids=None):
        """
        :param wafInstanceId:  实例id，代表要设置的WAF实例
        :param domain:  域名
        :param disable: (Optional) 0:使用规则，1：禁用规则
        :param ids: (Optional) 操作的规则id, ruleType非"waf"时必填
        :param ruleType:  操作的规则类型，"waf":waf总体防护开关，"cc":cc规则，"ratelimit"：限速，"usrdefCookie":cookie类型的黑白名单，"usrdefGeo":geo类型的黑白名单，"usrdefOwner":owner类型的黑白名单,"usrdefHeaders":header类型的黑白名单，"usrdefIP":ip类型的黑白名单，"usrdefURI":uri类型的黑白名单，"filterReqresp":请求头类型的流量管理，"filterSenseinfo":敏感信息防泄漏，"usrdefWaf":waf自定义规则,"rewriteRule":重写规则（目前是uri重写规则）,"listRule":黑白名单规则（目前指method黑白名单）,"proxycache":url缓存，"botUsr":自定义类型BOT规则,"risk":风险防护规则,"riskEvent":风险控制事件,"riskUsrList":风险控制用户自定义名单
        """

        self.wafInstanceId = wafInstanceId
        self.domain = domain
        self.disable = disable
        self.ids = ids
        self.ruleType = ruleType
