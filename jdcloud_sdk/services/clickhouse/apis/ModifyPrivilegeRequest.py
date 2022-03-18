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


class ModifyPrivilegeRequest(JDCloudRequest):
    """
    修改账号权限
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(ModifyPrivilegeRequest, self).__init__(
            '/regions/{regionId}/instances/{instanceId}/accounts/{accountName}:modifyPrivilege', 'POST', header, version)
        self.parameters = parameters


class ModifyPrivilegeParameters(object):

    def __init__(self, regionId,instanceId,accountName,):
        """
        :param regionId: 地域代码
        :param instanceId: 实例ID
        :param accountName: 账号名称
        """

        self.regionId = regionId
        self.instanceId = instanceId
        self.accountName = accountName
        self.privileges = None

    def setPrivileges(self, privileges):
        """
        :param privileges: (Optional) 账号的访问权限
        """
        self.privileges = privileges

