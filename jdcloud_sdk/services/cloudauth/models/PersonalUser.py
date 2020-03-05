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


class PersonalUser(object):

    def __init__(self, name, idCard, bankcard, mobile, imgBase64, ):
        """
        :param name:  姓名
        :param idCard:  身份证号码
        :param bankcard:  银行卡号
        :param mobile:  手机号
        :param imgBase64:  人像图片
        """

        self.name = name
        self.idCard = idCard
        self.bankcard = bankcard
        self.mobile = mobile
        self.imgBase64 = imgBase64
