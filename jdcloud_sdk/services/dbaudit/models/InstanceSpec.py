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


class InstanceSpec(object):

    def __init__(self, orderType=None, insName=None, insDesc=None, insZone=None, insType=None, vpcId=None, subnetId=None, chargeMode=None, timeUnit=None, timeSpan=None, quantity=None, extraInfo=None, formula=None, taskId=None, autoRenew=None, renewTimeUnit=None, renewTimeSpan=None, returnUrl=None, serviceCode=None, appCode=None, ydCode=None):
        """
        :param orderType: (Optional) 订单类型：新购-NEW，变配-RESIZE_FORMULA，暂只支持新购
        :param insName: (Optional) 实例名称,长度限制32字节,允许英文字母,数字,下划线,中划线和中文
        :param insDesc: (Optional) 实例描述,长度限制128字节
        :param insZone: (Optional) 可用区
        :param insType: (Optional) 实例规格: basic:标准版 professional:企业版 enterprise:增强版 ultimate:旗舰版
        :param vpcId: (Optional) 私有网络Id(VPCId)
        :param subnetId: (Optional) 私有网络子网Id(SubNetId)
        :param chargeMode: (Optional) 资源计费类型（CONFIG-按配置，FLOW-按用量，MONTHLY-包年包月，ONCE-按次付费，暂只支持包年包月
        :param timeUnit: (Optional) 购买时长类型, 新购时必传. 
MONTH: 按月购买
YEAR: 按年购买

        :param timeSpan: (Optional) 购买时长, 新购时必传. 
timeUnit = MONTH 时, 可取值 1-9
timeUnit = YEAR 时, 可取值 1-3

        :param quantity: (Optional) 购买数量
        :param extraInfo: (Optional) 商品规格参数,支付确认页面显示商品详情用
        :param formula: (Optional) 计费配置项
        :param taskId: (Optional) 打包标识
        :param autoRenew: (Optional) OPEN-开通自动续费,CLOSE-关闭自动续费,默认关闭
        :param renewTimeUnit: (Optional) 自动续费时间单位(MONTH-月,YEAR-年)
        :param renewTimeSpan: (Optional) 自动续费时长
1. renewTimeUnit=MONTH 时，取值范围 [1,9]
2. renewTimeUnit=YEAR 时，取值范围 [1,3]

        :param returnUrl: (Optional) 跳转页面
        :param serviceCode: (Optional) ServiceCode，用作计费使用
        :param appCode: (Optional) appCode，用作计费使用
        :param ydCode: (Optional) ydCode, 云鼎业务线用来关联订单
        """

        self.orderType = orderType
        self.insName = insName
        self.insDesc = insDesc
        self.insZone = insZone
        self.insType = insType
        self.vpcId = vpcId
        self.subnetId = subnetId
        self.chargeMode = chargeMode
        self.timeUnit = timeUnit
        self.timeSpan = timeSpan
        self.quantity = quantity
        self.extraInfo = extraInfo
        self.formula = formula
        self.taskId = taskId
        self.autoRenew = autoRenew
        self.renewTimeUnit = renewTimeUnit
        self.renewTimeSpan = renewTimeSpan
        self.returnUrl = returnUrl
        self.serviceCode = serviceCode
        self.appCode = appCode
        self.ydCode = ydCode