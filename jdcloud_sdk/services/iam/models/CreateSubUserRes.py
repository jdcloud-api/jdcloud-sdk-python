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


class CreateSubUserRes(object):

    def __init__(self, name=None, password=None, email=None, phone=None, accessKey=None, secretAccessKey=None, createTime=None, updateTime=None, nickName=None):
        """
        :param name: (Optional) 用户名
        :param password: (Optional) 密码
        :param email: (Optional) 邮箱
        :param phone: (Optional) 手机号码
        :param accessKey: (Optional) accessKey
        :param secretAccessKey: (Optional) AccessKey secret
        :param createTime: (Optional) 创建时间
        :param updateTime: (Optional) 更新时间
        :param nickName: (Optional) 姓名
        """

        self.name = name
        self.password = password
        self.email = email
        self.phone = phone
        self.accessKey = accessKey
        self.secretAccessKey = secretAccessKey
        self.createTime = createTime
        self.updateTime = updateTime
        self.nickName = nickName
