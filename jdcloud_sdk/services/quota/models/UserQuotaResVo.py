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


class UserQuotaResVo(object):

    def __init__(self, pin=None, appCode=None, serviceCode=None, serviceName=None, region=None, regionName=None, userQuota=None, maxUserQuota=None, expireTime=None, availableQuota=None, preOccupyAmount=None, createdTime=None, updatedTime=None, resourceId=None, parentResourceId=None, productName=None, siteType=None, quotaAmount=None, quotaBeyondFlag=None, isSubResource=None, failReason=None):
        """
        :param pin: (Optional) 用户pin
        :param appCode: (Optional) 业务线
        :param serviceCode: (Optional) 产品线
        :param serviceName: (Optional) 产品线名称
        :param region: (Optional) 地域
        :param regionName: (Optional) 地域名称
        :param userQuota: (Optional) 用户该地域该资源下的配额值
        :param maxUserQuota: (Optional) 用户该地域该资源下的最大可用配额值
        :param expireTime: (Optional) 配额到期时间
        :param availableQuota: (Optional) 可用配额
        :param preOccupyAmount: (Optional) 预占配额
        :param createdTime: (Optional) 创建时间
        :param updatedTime: (Optional) 更新时间
        :param resourceId: (Optional) 资源id
        :param parentResourceId: (Optional) 父资源id
        :param productName: (Optional) 产品名称
        :param siteType: (Optional) 站点类型
        :param quotaAmount: (Optional) 已用配额
        :param quotaBeyondFlag: (Optional) 配额超出标识,[已使用配额，大于等于配额总量，false]，[已使用配额，小于配额总量，返回true]
        :param isSubResource: (Optional) 是否资资源
        :param failReason: (Optional) 失败原因
        """

        self.pin = pin
        self.appCode = appCode
        self.serviceCode = serviceCode
        self.serviceName = serviceName
        self.region = region
        self.regionName = regionName
        self.userQuota = userQuota
        self.maxUserQuota = maxUserQuota
        self.expireTime = expireTime
        self.availableQuota = availableQuota
        self.preOccupyAmount = preOccupyAmount
        self.createdTime = createdTime
        self.updatedTime = updatedTime
        self.resourceId = resourceId
        self.parentResourceId = parentResourceId
        self.productName = productName
        self.siteType = siteType
        self.quotaAmount = quotaAmount
        self.quotaBeyondFlag = quotaBeyondFlag
        self.isSubResource = isSubResource
        self.failReason = failReason
