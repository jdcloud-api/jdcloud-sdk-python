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


class CreateInstanceRequest(JDCloudRequest):
    """
    新购或升级高防实例
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(CreateInstanceRequest, self).__init__(
            '/regions/{regionId}/instances', 'POST', header, version)
        self.parameters = parameters


class CreateInstanceParameters(object):

    def __init__(self, regionId,createInstanceSpec, ):
        """
        :param regionId: 区域 ID, 高防不区分区域, 传 cn-north-1 即可
        :param createInstanceSpec: 新购或升级实例请求参数
        """

        self.regionId = regionId
        self.createInstanceSpec = createInstanceSpec
        self.autoRenewalSpec = None
        self.autoPay = None

    def setAutoRenewalSpec(self, autoRenewalSpec):
        """
        :param autoRenewalSpec: (Optional) 自动续费配置, 默认不开通, 仅新购实例时可设置
        """
        self.autoRenewalSpec = autoRenewalSpec

    def setAutoPay(self, autoPay):
        """
        :param autoPay: (Optional) 自动支付标识
        """
        self.autoPay = autoPay

