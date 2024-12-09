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


class InstanceCollectConfigModifyRequest(JDCloudRequest):
    """
    修改产品实例采集配置信息
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(InstanceCollectConfigModifyRequest, self).__init__(
            '/instanceCollectConfigModify', 'POST', header, version)
        self.parameters = parameters


class InstanceCollectConfigModifyParameters(object):

    def __init__(self,pin, product, instance, ):
        """
        :param pin: 租户，必填
        :param product: 产品名，必填
        :param instance: 实例，必填
        """

        self.pin = pin
        self.product = product
        self.instance = instance
        self.configs = None

    def setConfigs(self, configs):
        """
        :param configs: (Optional) 修改的采集配置信息
        """
        self.configs = configs

