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


class PostAddress(object):

    def __init__(self, id=None, name=None, phone=None, province=None, city=None, county=None, town=None, address=None, isDefault=None, updateTime=None, pin=None, createTime=None, zipCode=None, provinceId=None, cityId=None, countyId=None, townId=None):
        """
        :param id: (Optional) id
        :param name: (Optional) 收件人姓名
        :param phone: (Optional) 收件人电话
        :param province: (Optional) 省
        :param city: (Optional) 市
        :param county: (Optional) 区
        :param town: (Optional) 县
        :param address: (Optional) 邮编
        :param isDefault: (Optional) 是否默认收货地址
        :param updateTime: (Optional) 更新时间
        :param pin: (Optional) 用户pin
        :param createTime: (Optional) 创建时间
        :param zipCode: (Optional) 邮编
        :param provinceId: (Optional) 省id
        :param cityId: (Optional) 市id
        :param countyId: (Optional) 区县id
        :param townId: (Optional) 乡镇id
        """

        self.id = id
        self.name = name
        self.phone = phone
        self.province = province
        self.city = city
        self.county = county
        self.town = town
        self.address = address
        self.isDefault = isDefault
        self.updateTime = updateTime
        self.pin = pin
        self.createTime = createTime
        self.zipCode = zipCode
        self.provinceId = provinceId
        self.cityId = cityId
        self.countyId = countyId
        self.townId = townId