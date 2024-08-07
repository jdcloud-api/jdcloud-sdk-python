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


class GetPriceReq(object):

    def __init__(self, region, buyType, timeSpan, timeUnit, packageType, appCode=None, serviceCode=None):
        """
        :param region:  地域信息
        :param buyType:  购买类型, 1:创建 2:续费 3:升配
        :param timeSpan:  购买时长
        :param timeUnit:  时间单位，month, year
        :param packageType:  套餐类型 0高级版 1企业版
        :param appCode: (Optional) appCode,公有云为空，云鼎填自己的appCode
        :param serviceCode: (Optional) serviceCode,公有云为空，云鼎填自己的serviceCode
        """

        self.region = region
        self.buyType = buyType
        self.timeSpan = timeSpan
        self.timeUnit = timeUnit
        self.packageType = packageType
        self.appCode = appCode
        self.serviceCode = serviceCode
