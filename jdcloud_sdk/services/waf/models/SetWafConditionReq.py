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


class SetWafConditionReq(object):

    def __init__(self, wafInstanceId, domain, conditionType, filters, id=None, conditionName=None):
        """
        :param id: (Optional) 0:新增，大于0:更新
        :param wafInstanceId:  WAF实例id
        :param domain:  域名
        :param conditionName: (Optional) 条件名称，新增时必须
        :param conditionType:  匹配类型，"str"/"regex"/"geo"/"size"/"ip"/"SQLi"/"XSS"
        :param filters:  过滤器配置
        """

        self.id = id
        self.wafInstanceId = wafInstanceId
        self.domain = domain
        self.conditionName = conditionName
        self.conditionType = conditionType
        self.filters = filters
