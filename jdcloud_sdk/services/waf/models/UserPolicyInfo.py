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


class UserPolicyInfo(object):

    def __init__(self, id=None, name=None, count=None, domainCnt=None, autoAdd=None, importLevel=None, ruleIds=None, updateTime=None, wafDomains=None):
        """
        :param id: (Optional) 规则组id
        :param name: (Optional) 规则组名字
        :param count: (Optional) 规则组里的规则个数
        :param domainCnt: (Optional) 规则组应用的域名个数
        :param autoAdd: (Optional) 规则是否自动更新, 0/1
        :param importLevel: (Optional) 导入规则集的等级，0/1/2/-1
        :param ruleIds: (Optional) 规则id
        :param updateTime: (Optional) 更新时间
        :param wafDomains: (Optional) 自定义规则集应用的域名信息
        """

        self.id = id
        self.name = name
        self.count = count
        self.domainCnt = domainCnt
        self.autoAdd = autoAdd
        self.importLevel = importLevel
        self.ruleIds = ruleIds
        self.updateTime = updateTime
        self.wafDomains = wafDomains
