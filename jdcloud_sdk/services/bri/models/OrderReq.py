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


class OrderReq(object):

    def __init__(self, region, buyType, timeSpan, timeUnit, startTime, packageType, returnURL, qpsLimit, needSpiderIp=None, version=None):
        """
        :param region:  地域信息
        :param buyType:  购买类型, 1:创建 2:续费 3:升配
        :param timeSpan:  购买时长
        :param timeUnit:  时间单位，month, year
        :param startTime:  创建时间
        :param packageType:  套餐类型 1.phone 2.IP 3.addr 4.eid 5.signup 6.login 7.marketing 8.pin 9.card
        :param returnURL:  下单成功后返回的url, eg:http://abc.com
        :param qpsLimit:  QPS上限(1-7) 1-100 2-300 3-500 4-1000 5-3000 6-5000 7-10000
        :param needSpiderIp: (Optional) 是否需要爬虫IP识别,当packageType为ip时必填  false-不购买  true-购买
        :param version: (Optional) 注册，登录，营销场景的版本号，当packageTpe为signup,login,marketing时必填   1-标准版  2-定制版
        """

        self.region = region
        self.buyType = buyType
        self.timeSpan = timeSpan
        self.timeUnit = timeUnit
        self.startTime = startTime
        self.packageType = packageType
        self.returnURL = returnURL
        self.qpsLimit = qpsLimit
        self.needSpiderIp = needSpiderIp
        self.version = version
