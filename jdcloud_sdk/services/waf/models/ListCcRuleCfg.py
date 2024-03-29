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


class ListCcRuleCfg(object):

    def __init__(self, wafInstanceId=None, domain=None, ruleName=None, uri=None, matchType=None, detectPeriod=None, singleIpLimit=None, blockType=None, blockTime=None, updateTime=None, disable=None, redirection=None, dimension=None, dmvalue=None):
        """
        :param wafInstanceId: (Optional) WAF实例id
        :param domain: (Optional) 域名
        :param ruleName: (Optional) 规则名称
        :param uri: (Optional) uri以/开头
        :param matchType: (Optional) 匹配uri 类型 0 精确匹配，1 前缀匹配（目前就支持精确匹配）
        :param detectPeriod: (Optional) 检测周期，单位是秒，[30~600]
        :param singleIpLimit: (Optional) ip访问次数，[1~9999999]
        :param blockType: (Optional) 阻断类型 3:封禁，2:人机交互
        :param blockTime: (Optional) block 持续时间，单位为分钟[1~24*60]
        :param updateTime: (Optional) 更新时间，s
        :param disable: (Optional) 0-使用中 1-禁用
        :param redirection: (Optional) 跳转地址，blockType为1时必须为当前实例下的域名的url，为2时为自定义页面名称
        :param dimension: (Optional) cc 统计维度，ip或cookie
        :param dmvalue: (Optional) cookiename, 只有当 dimension 为 cookie 时才有效
        """

        self.wafInstanceId = wafInstanceId
        self.domain = domain
        self.ruleName = ruleName
        self.uri = uri
        self.matchType = matchType
        self.detectPeriod = detectPeriod
        self.singleIpLimit = singleIpLimit
        self.blockType = blockType
        self.blockTime = blockTime
        self.updateTime = updateTime
        self.disable = disable
        self.redirection = redirection
        self.dimension = dimension
        self.dmvalue = dmvalue
