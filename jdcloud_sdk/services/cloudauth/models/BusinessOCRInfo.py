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


class BusinessOCRInfo(object):

    def __init__(self, status=None, code=None, number=None, name=None, companyType=None, address=None, legalPersonal=None, registeredCapital=None, date=None, scope=None, registrationDate=None, chargeFlag=None):
        """
        :param status: (Optional) 识别状态
        :param code: (Optional) 状态码
        :param number: (Optional) 统一社会信用代码
        :param name: (Optional) 名称
        :param companyType: (Optional) 类型
        :param address: (Optional) 住所
        :param legalPersonal: (Optional) 法定代表人
        :param registeredCapital: (Optional) 注册资本
        :param date: (Optional) 成立日期
        :param scope: (Optional) 经营范围
        :param registrationDate: (Optional) 登记日期
        :param chargeFlag: (Optional) 1收费，0不收费
        """

        self.status = status
        self.code = code
        self.number = number
        self.name = name
        self.companyType = companyType
        self.address = address
        self.legalPersonal = legalPersonal
        self.registeredCapital = registeredCapital
        self.date = date
        self.scope = scope
        self.registrationDate = registrationDate
        self.chargeFlag = chargeFlag
