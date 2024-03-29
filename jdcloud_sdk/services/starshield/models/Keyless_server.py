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


class Keyless_server(object):

    def __init__(self, port=None, enabled=None, permissions=None, host=None, name=None, status=None, modified_on=None, created_on=None, id=None):
        """
        :param port: (Optional) 用于在星盾和客户的无密钥SSL服务器之间通信的无密钥SSL端口
        :param enabled: (Optional) 无钥匙SSL是否开启或关闭
        :param permissions: (Optional) 当前用户的无密钥SSL的可用权限
        :param host: (Optional) 无密钥SSL主机名或ip
        :param name: (Optional) 无密钥SSL名称
        :param status: (Optional) 无密钥SSL的状态
        :param modified_on: (Optional) 上次修改无密钥SSL的时间
        :param created_on: (Optional) 创建无密钥SSL的时间
        :param id: (Optional) 无密钥证书标识符标签
        """

        self.port = port
        self.enabled = enabled
        self.permissions = permissions
        self.host = host
        self.name = name
        self.status = status
        self.modified_on = modified_on
        self.created_on = created_on
        self.id = id
