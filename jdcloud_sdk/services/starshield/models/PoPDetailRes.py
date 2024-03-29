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


class PoPDetailRes(object):

    def __init__(self, id=None, name=None, region=None, city=None, status=None, isp=None, routing_modes=None, service_levels=None):
        """
        :param id: (Optional) PoP节点ID
        :param name: (Optional) PoP节点名称
        :param region: (Optional) 区域
        :param city: (Optional) 城市
        :param status: (Optional) 节点状态
        :param isp: (Optional) 运营商信息(CT->中国电信 CM->中国移动 CU->中国联通)
        :param routing_modes: (Optional) 
        :param service_levels: (Optional) 
        """

        self.id = id
        self.name = name
        self.region = region
        self.city = city
        self.status = status
        self.isp = isp
        self.routing_modes = routing_modes
        self.service_levels = service_levels
