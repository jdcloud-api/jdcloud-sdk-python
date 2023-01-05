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


class DescribeInstanceTemplateRequest(JDCloudRequest):
    """
    
查询实例模板详情。

详细操作说明请参考帮助文档：[实例模板](https://docs.jdcloud.com/cn/virtual-machines/instance-template-overview)

## 接口说明
- 该接口与查询实例模板列表返回的信息一致。
- 只需要查询单个实例模板详细信息的时候可以调用该接口。

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeInstanceTemplateRequest, self).__init__(
            '/regions/{regionId}/instanceTemplates/{instanceTemplateId}', 'GET', header, version)
        self.parameters = parameters


class DescribeInstanceTemplateParameters(object):

    def __init__(self,regionId, instanceTemplateId):
        """
        :param regionId: 地域ID。
        :param instanceTemplateId: 实例模板ID。
        """

        self.regionId = regionId
        self.instanceTemplateId = instanceTemplateId

