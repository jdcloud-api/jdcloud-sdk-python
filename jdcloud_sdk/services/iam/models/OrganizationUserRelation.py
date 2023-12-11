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


class OrganizationUserRelation(object):

    def __init__(self, orgId=None, userId=None, subUserName=None, departmentPathName=None, createTime=None):
        """
        :param orgId: (Optional) 组织ID
        :param userId: (Optional) 组织用户标识，如：erp
        :param subUserName: (Optional) 关联的子用户名
        :param departmentPathName: (Optional) 组织部门路径名称
        :param createTime: (Optional) 创建时间
        """

        self.orgId = orgId
        self.userId = userId
        self.subUserName = subUserName
        self.departmentPathName = departmentPathName
        self.createTime = createTime
