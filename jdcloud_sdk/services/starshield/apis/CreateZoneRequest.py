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


class CreateZoneRequest(JDCloudRequest):
    """
    
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(CreateZoneRequest, self).__init__(
            '/zones', 'POST', header, version)
        self.parameters = parameters


class CreateZoneParameters(object):

    def __init__(self, name, account, ):
        """
        :param name: 域名
        :param account: 
        """

        self.name = name
        self.account = account
        self.jump_start = None
        self.ty_pe = None

    def setJump_start(self, jump_start):
        """
        :param jump_start: (Optional) 自动尝试获取现有DNS记录
        """
        self.jump_start = jump_start

    def setTy_pe(self, ty_pe):
        """
        :param ty_pe: (Optional) 全接入域意味着DNS由星盾托管。半接入域通常是合作伙伴托管的域或CNAME设置。
        """
        self.ty_pe = ty_pe
