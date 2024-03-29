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


class ConsoleInstanceVoucherVo(object):

    def __init__(self, instanceVoucherId=None, instanceVoucherType=None, isReserved=None, region=None, tips=None, label=None, count=None, unit=None, startTime=None, endTime=None, createTime=None, status=None):
        """
        :param instanceVoucherId: (Optional) 实例券id
        :param instanceVoucherType: (Optional) 实例券类型
        :param isReserved: (Optional) 资源预留(1 有预留、2 无预留)
        :param region: (Optional) 地域
        :param tips: (Optional) 展示说明
        :param label: (Optional) 展示实例族/规格
        :param count: (Optional) 数量
        :param unit: (Optional) 显示单位
        :param startTime: (Optional) 生效时间
        :param endTime: (Optional) 失效时间
        :param createTime: (Optional) 创建时间
        :param status: (Optional) 状态(1：正常: 2：已退订 -1:失效)
        """

        self.instanceVoucherId = instanceVoucherId
        self.instanceVoucherType = instanceVoucherType
        self.isReserved = isReserved
        self.region = region
        self.tips = tips
        self.label = label
        self.count = count
        self.unit = unit
        self.startTime = startTime
        self.endTime = endTime
        self.createTime = createTime
        self.status = status
