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


class NatGatewaySpec(object):

    def __init__(self, natType=None, natId=None, elasticIpSpec=None):
        """
        :param natType: (Optional) nat的类型，nat_vm/nat_gw/nat_none
        :param natId: (Optional) nat虚机id，或者nat网关的实例id
        :param elasticIpSpec: (Optional) Nat实例对应的公网IP的配置，只有nat_vm时才生效
        """

        self.natType = natType
        self.natId = natId
        self.elasticIpSpec = elasticIpSpec
