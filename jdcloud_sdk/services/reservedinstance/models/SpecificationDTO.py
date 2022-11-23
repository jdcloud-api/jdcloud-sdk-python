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


class SpecificationDTO(object):

    def __init__(self, appCode=None, serviceCode=None, reservedInstanceType=None, isReserved=None, instanceTypeFamily=None, usingServiceCode=None, instanceType=None, standardFactor=None, status=None):
        """
        :param appCode: (Optional) 产品线
        :param serviceCode: (Optional) 产品
        :param reservedInstanceType: (Optional) 券类型
        :param isReserved: (Optional) 预留类型
        :param instanceTypeFamily: (Optional) 券规格
        :param usingServiceCode: (Optional) 可抵扣产品
        :param instanceType: (Optional) 可抵扣规格
        :param standardFactor: (Optional) 标准化因子
        :param status: (Optional) 状态
        """

        self.appCode = appCode
        self.serviceCode = serviceCode
        self.reservedInstanceType = reservedInstanceType
        self.isReserved = isReserved
        self.instanceTypeFamily = instanceTypeFamily
        self.usingServiceCode = usingServiceCode
        self.instanceType = instanceType
        self.standardFactor = standardFactor
        self.status = status