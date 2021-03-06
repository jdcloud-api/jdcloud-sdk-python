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


class ModifyTemplateInfoRequest(JDCloudRequest):
    """
    修改域名信息模板
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(ModifyTemplateInfoRequest, self).__init__(
            '/regions/{regionId}/template/{templateId}', 'PUT', header, version)
        self.parameters = parameters


class ModifyTemplateInfoParameters(object):

    def __init__(self, regionId, templateId, ):
        """
        :param regionId: 实例所属的地域ID
        :param templateId: 模板ID
        """

        self.regionId = regionId
        self.templateId = templateId
        self.nationCodeCh = None
        self.nationCodeEn = None
        self.provinceCodeCh = None
        self.provinceCodeEn = None
        self.cityCodeCh = None
        self.cityCodeEn = None
        self.addressCh = None
        self.addressEn = None
        self.zipCode = None
        self.phone = None
        self.fax = None
        self.email = None
        self.ownerType = None

    def setNationCodeCh(self, nationCodeCh):
        """
        :param nationCodeCh: (Optional) 国家及地区（中文）
        """
        self.nationCodeCh = nationCodeCh

    def setNationCodeEn(self, nationCodeEn):
        """
        :param nationCodeEn: (Optional) 国家及地区（英文）中国：china
        """
        self.nationCodeEn = nationCodeEn

    def setProvinceCodeCh(self, provinceCodeCh):
        """
        :param provinceCodeCh: (Optional) 省份（中文）
        """
        self.provinceCodeCh = provinceCodeCh

    def setProvinceCodeEn(self, provinceCodeEn):
        """
        :param provinceCodeEn: (Optional) 省份（英文）
        """
        self.provinceCodeEn = provinceCodeEn

    def setCityCodeCh(self, cityCodeCh):
        """
        :param cityCodeCh: (Optional) 城市（中文）
        """
        self.cityCodeCh = cityCodeCh

    def setCityCodeEn(self, cityCodeEn):
        """
        :param cityCodeEn: (Optional) 城市（英文）
        """
        self.cityCodeEn = cityCodeEn

    def setAddressCh(self, addressCh):
        """
        :param addressCh: (Optional) 通信地址（中文）
        """
        self.addressCh = addressCh

    def setAddressEn(self, addressEn):
        """
        :param addressEn: (Optional) 通信地址（英文）
        """
        self.addressEn = addressEn

    def setZipCode(self, zipCode):
        """
        :param zipCode: (Optional) 邮编 6位数字
        """
        self.zipCode = zipCode

    def setPhone(self, phone):
        """
        :param phone: (Optional) 联系电话，国家区号-地区区号(或手机号码前3位)-电话号码（或手机号码后8位) 例:86-138-12345678
        """
        self.phone = phone

    def setFax(self, fax):
        """
        :param fax: (Optional) 传真，国家区号-地区区号(或手机号码前3位)-电话号码（或手机号码后8位) 例:86-138-12345678
        """
        self.fax = fax

    def setEmail(self, email):
        """
        :param email: (Optional) 邮件
        """
        self.email = email

    def setOwnerType(self, ownerType):
        """
        :param ownerType: (Optional) 所有者类型  1个人 2企业
        """
        self.ownerType = ownerType

