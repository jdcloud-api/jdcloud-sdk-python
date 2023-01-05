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


class AssociateElasticIpRequest(JDCloudRequest):
    """
    
为云主机绑定弹性公网IP。

详细操作说明请参考帮助文档：[绑定弹性公网IP](https://docs.jdcloud.com/cn/virtual-machines/associate-elastic-ip)

## 接口说明
- 该接口只支持在实例的主网卡的主内网IP上绑定弹性公网IP。
- 一台云主机的主网卡的主内网IP只能绑定一个弹性公网IP，若已绑定弹性公网IP，操作绑定会返回错误。
- 弹性公网IP所在的可用区需要与云主机的可用区保持一致，或者弹性公网IP是全可用区类型的，才允许绑定操作。

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(AssociateElasticIpRequest, self).__init__(
            '/regions/{regionId}/instances/{instanceId}:associateElasticIp', 'POST', header, version)
        self.parameters = parameters


class AssociateElasticIpParameters(object):

    def __init__(self,regionId, instanceId, elasticIpId):
        """
        :param regionId: 地域ID。
        :param instanceId: 云主机ID。
        :param elasticIpId: 弹性公网IP的ID。
        """

        self.regionId = regionId
        self.instanceId = instanceId
        self.elasticIpId = elasticIpId

