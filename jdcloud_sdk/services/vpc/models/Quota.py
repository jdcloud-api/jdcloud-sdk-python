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


class Quota(object):

    def __init__(self, type=None, parentResourceId=None, maxLimit=None, count=None):
        """
        :param type: (Optional) 资源类型，取值范围：vpc、elastic_ip、subnet、security_group、vpcpeering、network_interface（配额只统计辅助网卡）、acl、aclRule、routeTable、staticRoute、propagatedRoute、securityGroupRule、network_interface_cidr、natGateway、natGatewayFip、trafficMirrorSession、trafficMirrorFilter、trafficMirrorFilterRule、trafficMirrorSource
        :param parentResourceId: (Optional) vpc、elastic_ip、network_interface、natGateway、trafficMirrorSession、trafficMirrorFilter为空, subnet、security_group、vpcpeering、acl、routeTable为vpcId, aclRule为aclId，staticRoute、propagatedRoute为routeTableId, securityGroupRule为securityGroupId, network_interface_cidr为networkInterfaceId，natGatewayFip为natGatewayId,trafficMirrorFilterRule设置为trafficMirrorFilterId,trafficMirrorSource设置为trafficMirrorSessionId
        :param maxLimit: (Optional) 配额大小
        :param count: (Optional) 已存在的资源数量
        """

        self.type = type
        self.parentResourceId = parentResourceId
        self.maxLimit = maxLimit
        self.count = count
