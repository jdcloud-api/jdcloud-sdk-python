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


class ModifySubnetRequest(JDCloudRequest):
    """
    修改子网接口
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(ModifySubnetRequest, self).__init__(
            '/regions/{regionId}/subnets/{subnetId}', 'PATCH', header, version)
        self.parameters = parameters


class ModifySubnetParameters(object):

    def __init__(self,regionId, subnetId, ):
        """
        :param regionId: Region ID
        :param subnetId: Subnet ID
        """

        self.regionId = regionId
        self.subnetId = subnetId
        self.subnetName = None
        self.description = None
        self.ipMaskLen = None

    def setSubnetName(self, subnetName):
        """
        :param subnetName: (Optional) 子网名称,只允许输入中文、数字、大小写字母、英文下划线“_”及中划线“-”，不允许为空且不超过32字符。
        """
        self.subnetName = subnetName

    def setDescription(self, description):
        """
        :param description: (Optional) 子网描述信息，允许输入UTF-8编码下的全部字符，不超过256字符。
        """
        self.description = description

    def setIpMaskLen(self, ipMaskLen):
        """
        :param ipMaskLen: (Optional) 子网内预留网段掩码长度，此网段IP地址按照单个申请，子网内其余部分IP地址以网段形式分配。此参数非必选，缺省值为0，代表子网内所有IP地址都按照单个申请
        """
        self.ipMaskLen = ipMaskLen

