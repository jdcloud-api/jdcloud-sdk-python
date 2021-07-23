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


class ResourceCountBo(object):

    def __init__(self, pin=None, appCode=None, appCodeName=None, serviceCode=None, serviceCodeName=None, count=None):
        """
        :param pin: (Optional) pin
        :param appCode: (Optional) 应用码code
        :param appCodeName: (Optional) 应用码名称
        :param serviceCode: (Optional) 服务码code
        :param serviceCodeName: (Optional) 服务码名称
        :param count: (Optional) 资源数量
        """

        self.pin = pin
        self.appCode = appCode
        self.appCodeName = appCodeName
        self.serviceCode = serviceCode
        self.serviceCodeName = serviceCodeName
        self.count = count
