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


class ContactPersonGroup(object):

    def __init__(self, id=None, pin=None, personId=None, groupId=None, created=None, modified=None, yn=None, isSelf=None):
        """
        :param id: (Optional) id
        :param pin: (Optional) 用户pin(创建人)
        :param personId: (Optional) 用户id
        :param groupId: (Optional) 联系人组id
        :param created: (Optional) 创建时间
        :param modified: (Optional) 修改时间
        :param yn: (Optional) 是否正常：0表示删除，1表示正常
        :param isSelf: (Optional) 1:账号联系人;2:非账号联系人
        """

        self.id = id
        self.pin = pin
        self.personId = personId
        self.groupId = groupId
        self.created = created
        self.modified = modified
        self.yn = yn
        self.isSelf = isSelf