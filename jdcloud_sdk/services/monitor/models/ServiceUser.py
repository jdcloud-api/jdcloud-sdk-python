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


class ServiceUser(object):

    def __init__(self, id=None, erp=None, isAdmin=None, serviceCode=None, serviceCodes=None, column=None, dir=None, number=None, size=None):
        """
        :param id: (Optional) 自增id
        :param erp: (Optional) erp
        :param isAdmin: (Optional) 是否为管理员
        :param serviceCode: (Optional) 业务线代码
        :param serviceCodes: (Optional) 业务线代码
        :param column: (Optional) 排序字段
        :param dir: (Optional) 排序方式
        :param number: (Optional) 页码
        :param size: (Optional) 查询条数
        """

        self.id = id
        self.erp = erp
        self.isAdmin = isAdmin
        self.serviceCode = serviceCode
        self.serviceCodes = serviceCodes
        self.column = column
        self.dir = dir
        self.number = number
        self.size = size
