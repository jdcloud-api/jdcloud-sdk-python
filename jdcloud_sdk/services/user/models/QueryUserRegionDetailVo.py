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


class QueryUserRegionDetailVo(object):

    def __init__(self, region=None, regionProvider=None, cloudManufacturer=None, alias=None, isReg=None, mapping=None):
        """
        :param region: (Optional) 地域 例：cn-north-1
        :param regionProvider: (Optional) 地域 例：cn-north-1(京东云)
        :param cloudManufacturer: (Optional) 云厂商
        :param alias: (Optional) 
        :param isReg: (Optional) 是否注册开通 0否，1是
        :param mapping: (Optional) 可用区集合
        """

        self.region = region
        self.regionProvider = regionProvider
        self.cloudManufacturer = cloudManufacturer
        self.alias = alias
        self.isReg = isReg
        self.mapping = mapping
