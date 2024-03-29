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


class UserDetail(object):

    def __init__(self, pin=None, updateTime=None, createTime=None, userType=None, surplusAmount=None, usedAmount=None, packagesAmount=None, packagesNum=None, tracking=None):
        """
        :param pin: (Optional) 用户名称
        :param updateTime: (Optional) 更新时间, yyyy-mm-dd hh:mm:ss格式
        :param createTime: (Optional) 创建时间, yyyy-mm-dd hh:mm:ss格式
        :param userType: (Optional) 用户类型，0-全部类型，1-付费用户，2-体验用户，3-无效用户
        :param surplusAmount: (Optional) 剩余调用量
        :param usedAmount: (Optional) 累计调用量
        :param packagesAmount: (Optional) 总购买量
        :param packagesNum: (Optional) 资源包数量
        :param tracking: (Optional) 跟踪描述
        """

        self.pin = pin
        self.updateTime = updateTime
        self.createTime = createTime
        self.userType = userType
        self.surplusAmount = surplusAmount
        self.usedAmount = usedAmount
        self.packagesAmount = packagesAmount
        self.packagesNum = packagesNum
        self.tracking = tracking
