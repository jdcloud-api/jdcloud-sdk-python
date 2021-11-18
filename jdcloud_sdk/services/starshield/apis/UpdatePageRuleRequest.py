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


class UpdatePageRuleRequest(JDCloudRequest):
    """
    替换页面规则。最终规则将与此请求传递的数据完全匹配。
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(UpdatePageRuleRequest, self).__init__(
            '/zones/{zone_identifier}/pagerules/{identifier}', 'PUT', header, version)
        self.parameters = parameters


class UpdatePageRuleParameters(object):

    def __init__(self, zone_identifier, identifier, ):
        """
        :param zone_identifier: 
        :param identifier: 
        """

        self.zone_identifier = zone_identifier
        self.identifier = identifier
        self.targets = None
        self.actions = None
        self.priority = None
        self.status = None

    def setTargets(self, targets):
        """
        :param targets: (Optional) 根据请求评估的目标
        """
        self.targets = targets

    def setActions(self, actions):
        """
        :param actions: (Optional) 如果此规则的目标与请求匹配，则要执行的操作集。操作可以将url重定向到另一个url或覆盖设置（但不能同时覆盖两者）
        """
        self.actions = actions

    def setPriority(self, priority):
        """
        :param priority: (Optional) 一个数字，表示一个页面规则优先于另一个页面规则。
如果您可能有一个全面的页面规则（例如#1 “/images/”）
但是想要更具体的规则优先（例如#2 '/images/special/'），
您需要在后者（#2）上指定更高的优先级，以便它将覆盖第一个优先级。

        """
        self.priority = priority

    def setStatus(self, status):
        """
        :param status: (Optional) 页面规则的状态
        """
        self.status = status

