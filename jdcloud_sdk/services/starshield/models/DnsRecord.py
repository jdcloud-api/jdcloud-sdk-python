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


class DnsRecord(object):

    def __init__(self, meta=None, locked=None, data=None, name=None, ttl=None, zone_id=None, modified_on=None, created_on=None, proxiable=None, content=None, ty_pe=None, id=None, proxied=None, zone_name=None, priority=None):
        """
        :param meta: (Optional) 
        :param locked: (Optional) 此记录是否可以被修改/删除（true意味着它由星盾管理）。
        :param data: (Optional) 
        :param name: (Optional) DNS记录名称
        :param ttl: (Optional) DNS记录的生存时间。值为1是 "自动"。
        :param zone_id: (Optional) 域标识符标签
        :param modified_on: (Optional) 记录最近修改时间
        :param created_on: (Optional) 创建记录时间
        :param proxiable: (Optional) 记录是否由星盾代理
        :param content: (Optional) 有效的IPv4地址
        :param ty_pe: (Optional) 记录类型
        :param id: (Optional) DNS记录标识符标签
        :param proxied: (Optional) 是否利用星盾的性能和安全优势
        :param zone_name: (Optional) 记录的域名
        :param priority: (Optional) 与一些记录如MX和SRV一起使用，以确定优先级。如果你没有为MX记录提供一个优先级，默认值为0将被设置。
        """

        self.meta = meta
        self.locked = locked
        self.data = data
        self.name = name
        self.ttl = ttl
        self.zone_id = zone_id
        self.modified_on = modified_on
        self.created_on = created_on
        self.proxiable = proxiable
        self.content = content
        self.ty_pe = ty_pe
        self.id = id
        self.proxied = proxied
        self.zone_name = zone_name
        self.priority = priority
