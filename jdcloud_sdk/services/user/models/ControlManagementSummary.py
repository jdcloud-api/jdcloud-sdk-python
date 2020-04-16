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


class ControlManagementSummary(object):

    def __init__(self, subUserCount=None, groupCount=None, policyCount=None, roleCount=None, idPCount=None, orgLoginUrl=None, subUserLoginUrl=None):
        """
        :param subUserCount: (Optional) 子用户个数
        :param groupCount: (Optional) 组个数
        :param policyCount: (Optional) 自定义权限个数
        :param roleCount: (Optional) 角色个数
        :param idPCount: (Optional) 身份提供商个数
        :param orgLoginUrl: (Optional) 角色个数
        :param subUserLoginUrl: (Optional) 子账号登录链接
        """

        self.subUserCount = subUserCount
        self.groupCount = groupCount
        self.policyCount = policyCount
        self.roleCount = roleCount
        self.idPCount = idPCount
        self.orgLoginUrl = orgLoginUrl
        self.subUserLoginUrl = subUserLoginUrl
