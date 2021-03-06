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


class VerifyQuotaResVo(object):

    def __init__(self, pin=None, appCode=None, serviceCode=None, serviceName=None, region=None, regionName=None, userQuota=None):
        """
        :param pin: (Optional) 用户pin
        :param appCode: (Optional) 业务线
        :param serviceCode: (Optional) 产品线
        :param serviceName: (Optional) 产品线名称
        :param region: (Optional) 地域
        :param regionName: (Optional) 地域名称
        :param userQuota: (Optional) 用户该地域该资源下的配额值
        """

        self.pin = pin
        self.appCode = appCode
        self.serviceCode = serviceCode
        self.serviceName = serviceName
        self.region = region
        self.regionName = regionName
        self.userQuota = userQuota
