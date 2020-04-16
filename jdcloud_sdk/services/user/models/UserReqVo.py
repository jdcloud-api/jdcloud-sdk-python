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


class UserReqVo(object):

    def __init__(self, pin=None, cscPhone=None, cscEmail=None, name=None, userType=None, companyName=None, createTimeStart=None, createTimeEnd=None, arrearageStatus=None, groups=None, group=None, billingWhite=None, tag=None, pageSize=None, currentPage=None):
        """
        :param pin: (Optional) 用户pin
        :param cscPhone: (Optional) 用户手机号
        :param cscEmail: (Optional) 用户邮箱
        :param name: (Optional) 用户名
        :param userType: (Optional) 用户类型
        :param companyName: (Optional) 公司名
        :param createTimeStart: (Optional) 起始时间
        :param createTimeEnd: (Optional) 结束时间
        :param arrearageStatus: (Optional) 欠费状态：
        :param groups: (Optional) 用户分组，多个逗号分隔:1-自然流量，2-内部测试，3-内部重点，4-渠道用户
        :param group: (Optional) 用户分组:1-自然流量，2-内部测试，3-内部重点，4-渠道用户
        :param billingWhite: (Optional) 计费白名单：1、在白名单  2、不在白名单
        :param tag: (Optional) 渠道等级;1普通用户2测试用户4VIP用户8其他VIP用户16boss迁移账户
        :param pageSize: (Optional) 页大小(必传)
        :param currentPage: (Optional) 当前页(必传)
        """

        self.pin = pin
        self.cscPhone = cscPhone
        self.cscEmail = cscEmail
        self.name = name
        self.userType = userType
        self.companyName = companyName
        self.createTimeStart = createTimeStart
        self.createTimeEnd = createTimeEnd
        self.arrearageStatus = arrearageStatus
        self.groups = groups
        self.group = group
        self.billingWhite = billingWhite
        self.tag = tag
        self.pageSize = pageSize
        self.currentPage = currentPage
