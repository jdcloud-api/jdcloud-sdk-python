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


class ModifyVpcPolicyRequest(JDCloudRequest):
    """
    修改VPC Policy接口
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(ModifyVpcPolicyRequest, self).__init__(
            '/regions/{regionId}/vpcPolicy/{vpcPolicyId}', 'PATCH', header, version)
        self.parameters = parameters


class ModifyVpcPolicyParameters(object):

    def __init__(self,regionId, vpcPolicyId, ):
        """
        :param regionId: Region ID
        :param vpcPolicyId: policy ID
        """

        self.regionId = regionId
        self.vpcPolicyId = vpcPolicyId
        self.vpcPolicyName = None
        self.policyDocument = None

    def setVpcPolicyName(self, vpcPolicyName):
        """
        :param vpcPolicyName: (Optional) VpcPolicy的名称,不为空(有变更再传)。取值范围：1-32个中文、英文大小写的字母、数字和下划线分隔符
        """
        self.vpcPolicyName = vpcPolicyName

    def setPolicyDocument(self, policyDocument):
        """
        :param policyDocument: (Optional) 具体策略内容(格式参考样例)
        """
        self.policyDocument = policyDocument
