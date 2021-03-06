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


class EdgeIpProvider(object):

    def __init__(self, provider=None, pointOfAccess=None, associationScope=None, serviceType=None, az=None):
        """
        :param provider: (Optional) 边缘公网IP的线路
        :param pointOfAccess: (Optional) 边缘公网IP的线路接入区
        :param associationScope: (Optional) 边缘公网IP的资源关联范围
        :param serviceType: (Optional) 边缘公网IP的服务类型
        :param az: (Optional) 边缘公网IP的可用区
        """

        self.provider = provider
        self.pointOfAccess = pointOfAccess
        self.associationScope = associationScope
        self.serviceType = serviceType
        self.az = az
