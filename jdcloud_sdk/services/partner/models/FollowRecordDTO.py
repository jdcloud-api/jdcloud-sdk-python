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


class FollowRecordDTO(object):

    def __init__(self, id=None, cmd=None, businessType=None, businessId=None, businessNo=None, businessNo2=None, followPerson=None, content=None, followTime=None, createTime=None, createUser=None, updateTime=None, updateUser=None, yn=None):
        """
        :param id: (Optional) ID
        :param cmd: (Optional) 业务操作（add添加、modify修改）
        :param businessType: (Optional) 业务类型（1 合作线索 2合作伙伴 3合作信息）
        :param businessId: (Optional) 业务ID
        :param businessNo: (Optional) 业务号码
        :param businessNo2: (Optional) 业务号码2
        :param followPerson: (Optional) 跟进人
        :param content: (Optional) 内容
        :param followTime: (Optional) 跟进时间
        :param createTime: (Optional) 创建时间
        :param createUser: (Optional) 创建人
        :param updateTime: (Optional) 修改时间
        :param updateUser: (Optional) 修改人
        :param yn: (Optional) 是否删除0未删除,1已删除
        """

        self.id = id
        self.cmd = cmd
        self.businessType = businessType
        self.businessId = businessId
        self.businessNo = businessNo
        self.businessNo2 = businessNo2
        self.followPerson = followPerson
        self.content = content
        self.followTime = followTime
        self.createTime = createTime
        self.createUser = createUser
        self.updateTime = updateTime
        self.updateUser = updateUser
        self.yn = yn
