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


class DescribeAttachedSubUserPoliciesScopeRequest(JDCloudRequest):
    """
    查询子用户绑定的策略对应资源组列表
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeAttachedSubUserPoliciesScopeRequest, self).__init__(
            '/subUser/{subUser}/policiesScope', 'GET', header, version)
        self.parameters = parameters


class DescribeAttachedSubUserPoliciesScopeParameters(object):

    def __init__(self,subUser, policyID, ):
        """
        :param subUser: 子用户名
        :param policyID: 策略ID
        """

        self.subUser = subUser
        self.policyID = policyID
        self.filterBindResGroup = None

    def setFilterBindResGroup(self, filterBindResGroup):
        """
        :param filterBindResGroup: (Optional) 滤绑定策略资源组："Deny" 不允许，Allow 允许，空情况默认不允许，兼容历史数据
        """
        self.filterBindResGroup = filterBindResGroup

