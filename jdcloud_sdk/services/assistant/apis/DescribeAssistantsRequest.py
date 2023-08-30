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


class DescribeAssistantsRequest(JDCloudRequest):
    """
    
查询云助手客户端状态。

详细操作说明请参考帮助文档：[用户自定义命令概述](https://docs.jdcloud.com/cn/virtual-machines/assistant-overview)

## 接口说明
- 该接口用于查询云助手客户端状态。

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeAssistantsRequest, self).__init__(
            '/regions/{regionId}/describeAssistants', 'POST', header, version)
        self.parameters = parameters


class DescribeAssistantsParameters(object):

    def __init__(self,regionId, instances):
        """
        :param regionId: 地域ID。
        :param instances: 云主机Id
        """

        self.regionId = regionId
        self.instances = instances

