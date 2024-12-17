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


class UnreleasedSc(object):

    def __init__(self, accessType=None, serviceCode=None, serviceCodeName=None, desc=None, scUrl=None, resourceCount=None):
        """
        :param accessType: (Optional) 类型  1:可一键处理 2:需手动处理
        :param serviceCode: (Optional) 产品编码
        :param serviceCodeName: (Optional) 产品名称
        :param desc: (Optional) 描述
        :param scUrl: (Optional) 控制台链接
        :param resourceCount: (Optional) 实例数量
        """

        self.accessType = accessType
        self.serviceCode = serviceCode
        self.serviceCodeName = serviceCodeName
        self.desc = desc
        self.scUrl = scUrl
        self.resourceCount = resourceCount
