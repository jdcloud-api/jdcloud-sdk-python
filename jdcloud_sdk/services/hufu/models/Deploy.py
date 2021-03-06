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


class Deploy(object):

    def __init__(self, revision, environment, backendServiceType=None, backendUrl=None, description=None, jdsfName=None, jdsfRegistryName=None, jdsfId=None):
        """
        :param revision:  发布的修订版本号
        :param environment:  环境：test、preview、online
        :param backendServiceType: (Optional) 后端服务类型：mock、unique、vpc
        :param backendUrl: (Optional) 后端地址
        :param description: (Optional) 描述
        :param jdsfName: (Optional) 微服务网关名称
        :param jdsfRegistryName: (Optional) 微服务注册中心ID
        :param jdsfId: (Optional) 微服务ID
        """

        self.revision = revision
        self.environment = environment
        self.backendServiceType = backendServiceType
        self.backendUrl = backendUrl
        self.description = description
        self.jdsfName = jdsfName
        self.jdsfRegistryName = jdsfRegistryName
        self.jdsfId = jdsfId
