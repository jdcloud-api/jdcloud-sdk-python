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


class DescribeZonesRes(object):

    def __init__(self, zoneId=None, name=None, status=None, paused=None, ty_pe=None, development_mode=None, verification_key=None, cname_suffix=None, original_name_servers=None, original_registrar=None, original_dnshost=None, modified_on=None, created_on=None, activated_on=None, name_servers=None, ips=None, ipType=None):
        """
        :param zoneId: (Optional) zone id
        :param name: (Optional) zone name
        :param status: (Optional) zone状态
        :param paused: (Optional) 是否暂停
        :param ty_pe: (Optional) zone接入类型
        :param development_mode: (Optional) 开发者模式
        :param verification_key: (Optional) 校验key
        :param cname_suffix: (Optional) cname后缀
        :param original_name_servers: (Optional) 源ns
        :param original_registrar: (Optional) 源注册商
        :param original_dnshost: (Optional) 源dns host
        :param modified_on: (Optional) 修改时间
        :param created_on: (Optional) 创建时间
        :param activated_on: (Optional) 激活时间
        :param name_servers: (Optional) name servers
        :param ips: (Optional) 域名对应的ip信息
        :param ipType: (Optional) ip类型
        """

        self.zoneId = zoneId
        self.name = name
        self.status = status
        self.paused = paused
        self.ty_pe = ty_pe
        self.development_mode = development_mode
        self.verification_key = verification_key
        self.cname_suffix = cname_suffix
        self.original_name_servers = original_name_servers
        self.original_registrar = original_registrar
        self.original_dnshost = original_dnshost
        self.modified_on = modified_on
        self.created_on = created_on
        self.activated_on = activated_on
        self.name_servers = name_servers
        self.ips = ips
        self.ipType = ipType
