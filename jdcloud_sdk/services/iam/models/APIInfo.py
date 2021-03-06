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


class APIInfo(object):

    def __init__(self, accessLevel=None, actionName=None, actionType=None, resource=None, resourceType=None, subResourceType=None, terResourceType=None):
        """
        :param accessLevel: (Optional) 访问级别
        :param actionName: (Optional) action name
        :param actionType: (Optional) action type
        :param resource: (Optional) 资源
        :param resourceType: (Optional) 资源类型
        :param subResourceType: (Optional) 子资源类型
        :param terResourceType: (Optional) 三级资源类型
        """

        self.accessLevel = accessLevel
        self.actionName = actionName
        self.actionType = actionType
        self.resource = resource
        self.resourceType = resourceType
        self.subResourceType = subResourceType
        self.terResourceType = terResourceType
