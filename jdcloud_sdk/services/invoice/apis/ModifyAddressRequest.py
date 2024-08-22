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

from jdcloud_sdk.core.jdcloudrequest import JDCloudRequest


class ModifyAddressRequest(JDCloudRequest):
    """
    修改发票邮寄地址
    """

    def __init__(self, parameters, header=None, version="v2"):
        super(ModifyAddressRequest, self).__init__(
            '/regions/{regionId}/address/{id}', 'PUT', header, version)
        self.parameters = parameters


class ModifyAddressParameters(object):

    def __init__(self,regionId, id, ):
        """
        :param regionId: 
        :param id: 
        """

        self.regionId = regionId
        self.id = id
        self.name = None
        self.phone = None
        self.province = None
        self.city = None
        self.county = None
        self.town = None
        self.address = None
        self.isDefault = None
        self.updateTime = None
        self.pin = None
        self.createTime = None
        self.zipCode = None
        self.provinceId = None
        self.cityId = None
        self.countyId = None
        self.townId = None

    def setName(self, name):
        """
        :param name: (Optional) 收件人姓名
        """
        self.name = name

    def setPhone(self, phone):
        """
        :param phone: (Optional) 收件人电话
        """
        self.phone = phone

    def setProvince(self, province):
        """
        :param province: (Optional) 省
        """
        self.province = province

    def setCity(self, city):
        """
        :param city: (Optional) 市
        """
        self.city = city

    def setCounty(self, county):
        """
        :param county: (Optional) 区
        """
        self.county = county

    def setTown(self, town):
        """
        :param town: (Optional) 县
        """
        self.town = town

    def setAddress(self, address):
        """
        :param address: (Optional) 邮编
        """
        self.address = address

    def setIsDefault(self, isDefault):
        """
        :param isDefault: (Optional) 是否默认收货地址
        """
        self.isDefault = isDefault

    def setUpdateTime(self, updateTime):
        """
        :param updateTime: (Optional) 更新时间
        """
        self.updateTime = updateTime

    def setPin(self, pin):
        """
        :param pin: (Optional) 用户pin
        """
        self.pin = pin

    def setCreateTime(self, createTime):
        """
        :param createTime: (Optional) 创建时间
        """
        self.createTime = createTime

    def setZipCode(self, zipCode):
        """
        :param zipCode: (Optional) 邮编
        """
        self.zipCode = zipCode

    def setProvinceId(self, provinceId):
        """
        :param provinceId: (Optional) 省id
        """
        self.provinceId = provinceId

    def setCityId(self, cityId):
        """
        :param cityId: (Optional) 市id
        """
        self.cityId = cityId

    def setCountyId(self, countyId):
        """
        :param countyId: (Optional) 区县id
        """
        self.countyId = countyId

    def setTownId(self, townId):
        """
        :param townId: (Optional) 乡镇id
        """
        self.townId = townId

