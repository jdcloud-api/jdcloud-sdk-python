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


class ProtectedObject(object):

    def __init__(self, type=None, count=None, ipList=None):
        """
        :param type: (Optional) 防护对象类型: eip: 弹性公网 IP, cps: 云物理服务器公网 IP, waf: Web应用防护墙 IP, ccs: 托管区公网 IP
        :param count: (Optional) 已防护 IP 个数
        :param ipList: (Optional) 防护 IP 列表
        """

        self.type = type
        self.count = count
        self.ipList = ipList
