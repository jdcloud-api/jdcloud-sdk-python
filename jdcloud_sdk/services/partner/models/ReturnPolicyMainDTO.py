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


class ReturnPolicyMainDTO(object):

    def __init__(self, id=None, deptId=None, distributorType=None, returnType=None, returnPolicyName=None, remark=None, status=None, createTime=None, createUser=None, updateTime=None, updateUser=None, yn=None):
        """
        :param id: (Optional) ID
        :param deptId: (Optional) 部门ID
        :param distributorType: (Optional) 渠道商类型
        :param returnType: (Optional) 返还类型
        :param returnPolicyName: (Optional) 返还政策主名称
        :param remark: (Optional) 备注
        :param status: (Optional) 状态
        :param createTime: (Optional) 创建时间
        :param createUser: (Optional) 创建人
        :param updateTime: (Optional) 修改时间
        :param updateUser: (Optional) 修改人
        :param yn: (Optional) 是否删除0未删除,1已删除
        """

        self.id = id
        self.deptId = deptId
        self.distributorType = distributorType
        self.returnType = returnType
        self.returnPolicyName = returnPolicyName
        self.remark = remark
        self.status = status
        self.createTime = createTime
        self.createUser = createUser
        self.updateTime = updateTime
        self.updateUser = updateUser
        self.yn = yn
