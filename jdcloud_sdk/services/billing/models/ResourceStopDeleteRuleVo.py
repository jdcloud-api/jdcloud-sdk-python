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


class ResourceStopDeleteRuleVo(object):

    def __init__(self, id=None, site=None, appCode=None, appCodeName=None, serviceCode=None, serviceCodeName=None, ruleType=None, pin=None, arrearStop=None, arrearStopDelayHours=None, arrearDelete=None, arrearDeleteDelayHours=None, expireStop=None, expireStopDelayHours=None, expireDelete=None, expireDeleteDelayHours=None, createTime=None, arrearDeleteType=None, expireDeleteType=None, flowArrearStop=None, flowArrearStopDelayHours=None, flowArrearDelete=None, flowArrearDeleteDelayHours=None, flowArrearDeleteType=None, clientType=None):
        """
        :param id: (Optional) 主键
        :param site: (Optional) 站点
        :param appCode: (Optional) 产品线编码
        :param appCodeName: (Optional) 产品线名称
        :param serviceCode: (Optional) 产品编码
        :param serviceCodeName: (Optional) 产品名称
        :param ruleType: (Optional) 规则类型 1：试用规则 2、用户产品规则 3：用户规则 4：产品规则 5：通用规则 6：用户等级产品规则
        :param pin: (Optional) pin
        :param arrearStop: (Optional) 按配置欠费是否停服  1：欠费需要停服 0：欠费不需要停服
        :param arrearStopDelayHours: (Optional) 按配置欠费停服延后时长
        :param arrearDelete: (Optional) 按配置欠费停服是否释放资源  1：需要释放资源 0：不需要释放资源
        :param arrearDeleteDelayHours: (Optional) 按配置欠费停服释放资源延后时长
        :param expireStop: (Optional) 到期是否停服  1：到期需要停服 0：到期不需要停服
        :param expireStopDelayHours: (Optional) 到期停服延后时长
        :param expireDelete: (Optional) 到期停服是否释放资源  1：需要释放资源 0：不需要释放资源
        :param expireDeleteDelayHours: (Optional) 到期停服释放资源延后时长
        :param createTime: (Optional) 创建时间
        :param arrearDeleteType: (Optional) 按配置欠费释放类型 1：释放资源  2：释放数据
        :param expireDeleteType: (Optional) 到期释放类型 1：释放资源  2：释放数据
        :param flowArrearStop: (Optional) 按用量欠费是否停服  1：欠费需要停服 0：欠费不需要停服
        :param flowArrearStopDelayHours: (Optional) 按用量欠费停服延后时长
        :param flowArrearDelete: (Optional) 按用量欠费停服是否释放资源  1：需要释放资源 0：不需要释放资源
        :param flowArrearDeleteDelayHours: (Optional) 按用量欠费停服释放资源延后时长
        :param flowArrearDeleteType: (Optional) 按用量欠费释放类型 1：释放资源  2：释放数据
        :param clientType: (Optional) 客户级别 1-普通客户 2-VIP客户
        """

        self.id = id
        self.site = site
        self.appCode = appCode
        self.appCodeName = appCodeName
        self.serviceCode = serviceCode
        self.serviceCodeName = serviceCodeName
        self.ruleType = ruleType
        self.pin = pin
        self.arrearStop = arrearStop
        self.arrearStopDelayHours = arrearStopDelayHours
        self.arrearDelete = arrearDelete
        self.arrearDeleteDelayHours = arrearDeleteDelayHours
        self.expireStop = expireStop
        self.expireStopDelayHours = expireStopDelayHours
        self.expireDelete = expireDelete
        self.expireDeleteDelayHours = expireDeleteDelayHours
        self.createTime = createTime
        self.arrearDeleteType = arrearDeleteType
        self.expireDeleteType = expireDeleteType
        self.flowArrearStop = flowArrearStop
        self.flowArrearStopDelayHours = flowArrearStopDelayHours
        self.flowArrearDelete = flowArrearDelete
        self.flowArrearDeleteDelayHours = flowArrearDeleteDelayHours
        self.flowArrearDeleteType = flowArrearDeleteType
        self.clientType = clientType
