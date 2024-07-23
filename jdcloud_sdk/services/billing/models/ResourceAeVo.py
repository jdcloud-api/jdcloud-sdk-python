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


class ResourceAeVo(object):

    def __init__(self, id=None, site=None, appCode=None, region=None, serviceCode=None, formula=None, pin=None, resourceId=None, billingType=None, subBillId=None, state=None, stateTime=None, op=None, isLastRecord=None, createTime=None, updateTime=None, toDeleteTime=None, capState=None):
        """
        :param id: (Optional) 自增主键
        :param site: (Optional) 站点标识1:中国 2:国际
        :param appCode: (Optional) 应用编码
        :param region: (Optional) 地域
        :param serviceCode: (Optional) 服务编码
        :param formula: (Optional) 配置项
        :param pin: (Optional) 用户pin
        :param resourceId: (Optional) 资源ID
        :param billingType: (Optional) 计费类型
        :param subBillId: (Optional) 账单ID
        :param state: (Optional) 状态 0:无 1:正常 2:欠费, 3:因欠费而停机, 4:欠费删除资源, 6:已删除但已不欠费, 7:欠费延期，8:删除并且欠费，9:欠费删除数据，12:已过期, 13:因过期而停机, 14:过期删除资源, 17:过期延期 19:过期删除数据23:管理员停服，24:管理员删除,34:用户删除,35:退款删除
        :param stateTime: (Optional) 首次欠费时间（各欠费状态）或过期时间（各过期状态）
        :param op: (Optional) 变成此状态的原因.0:无 1:账单欠费, 2:资源过期 ,3:加入、移出白名单 ,4:补扣款成功, 5:规则修改,6:续费 7:管理员操作,8:用户操作,9:加入/移出回收站
        :param isLastRecord: (Optional) 是否为最后状态记录
        :param createTime: (Optional) 本条记录生成时刻、进入当前state的时刻
        :param updateTime: (Optional) 修改时间
        :param toDeleteTime: (Optional) 资源预计释放时间
        :param capState: (Optional) 用于中间层判断的状态标识 1:正常(重启) 3:欠费停服 4:欠费删除 13：到期停服 14：到期删除、退款删除 24：运营删除 34:用户删除
        """

        self.id = id
        self.site = site
        self.appCode = appCode
        self.region = region
        self.serviceCode = serviceCode
        self.formula = formula
        self.pin = pin
        self.resourceId = resourceId
        self.billingType = billingType
        self.subBillId = subBillId
        self.state = state
        self.stateTime = stateTime
        self.op = op
        self.isLastRecord = isLastRecord
        self.createTime = createTime
        self.updateTime = updateTime
        self.toDeleteTime = toDeleteTime
        self.capState = capState
