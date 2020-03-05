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


class RouterBody(object):

    def __init__(self, routerType=None, routerInfoId=None, routerInfoName=None, identifier=None, productKey=None):
        """
        :param routerType: (Optional) router类型，subdevice或者app
        :param routerInfoId: (Optional) 设备或APP的编号
        :param routerInfoName: (Optional) 设备或APP名称
        :param identifier: (Optional) 设备三元组-identifier,类型为SUBDEVICE时必填
        :param productKey: (Optional) 设备三元组-identifier,类型为SUBDEVICE时必填
        """

        self.routerType = routerType
        self.routerInfoId = routerInfoId
        self.routerInfoName = routerInfoName
        self.identifier = identifier
        self.productKey = productKey
