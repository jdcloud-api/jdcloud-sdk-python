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


class ModifyElasticIpRequest(JDCloudRequest):
    """
    修改弹性公网IP，当弹性公网IP加入共享带宽包后，此公网IP限速需要调用共享带宽包的接口（修改共享带宽包内公网IP带宽上限）
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(ModifyElasticIpRequest, self).__init__(
            '/regions/{regionId}/elasticIps/{elasticIpId}', 'PATCH', header, version)
        self.parameters = parameters


class ModifyElasticIpParameters(object):

    def __init__(self,regionId, elasticIpId, bandwidthMbps):
        """
        :param regionId: Region ID
        :param elasticIpId: ElasticIp ID
        :param bandwidthMbps: 弹性公网IP的限速（单位：Mbps），取值范围为[1-200]
        """

        self.regionId = regionId
        self.elasticIpId = elasticIpId
        self.bandwidthMbps = bandwidthMbps

