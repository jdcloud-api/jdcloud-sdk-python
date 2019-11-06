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


class VpcIpResource(object):

    def __init__(self, ip=None, binded=None, resourceType=None):
        """
        :param ip: (Optional) 云内 IP 地址
        :param binded: (Optional) 是否绑定
        :param resourceType: (Optional) 公网 IP 类型或绑定资源类型. <br>- 0: 未知类型<br>- 1: 弹性公网 IP(IP 为弹性公网 IP, 绑定资源类型未知)<br>- 10: 弹性公网 IP(IP 为弹性公网 IP, 但未绑定资源)<br>- 11: 弹性公网 IP, 绑定了云主机<br>- 12: 弹性公网 IP, 绑定了负载均衡<br>- 13: 弹性公网 IP, 绑定了原生容器实例<br>- 14: 弹性公网 IP, 绑定了原生容器 Pod<br>- 2: 云物理服务器公网 IP
        """

        self.ip = ip
        self.binded = binded
        self.resourceType = resourceType
