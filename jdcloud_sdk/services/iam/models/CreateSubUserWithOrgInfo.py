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


class CreateSubUserWithOrgInfo(object):

    def __init__(self, orgId, orgUserId, description=None, createAk=None, consoleLogin=None):
        """
        :param orgId:  组织ID
        :param orgUserId:  组织用户标识
        :param description: (Optional) 描述，0~256个字符
        :param createAk: (Optional) 是否创建accessKey，默认false
        :param consoleLogin: (Optional) 子用户是否支持控制台登录，默认true
        """

        self.orgId = orgId
        self.orgUserId = orgUserId
        self.description = description
        self.createAk = createAk
        self.consoleLogin = consoleLogin
