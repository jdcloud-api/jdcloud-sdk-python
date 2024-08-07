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


class DescribeGrayProdVo(object):

    def __init__(self, id=None, prod=None, eName=None, createTime=None, userCount=None, status=None, updateTime=None, creator=None, receiver=None, oldName=None, clientType=None, codeSource=None):
        """
        :param id: (Optional) id
        :param prod: (Optional) 产品线名称
        :param eName: (Optional) eName
        :param createTime: (Optional) 创建时间
        :param userCount: (Optional) 使用人数
        :param status: (Optional) 状态
        :param updateTime: (Optional) 修改时间
        :param creator: (Optional) 创建人
        :param receiver: (Optional) 管理员
        :param oldName: (Optional) 曾用名
        :param clientType: (Optional) 属性
        :param codeSource: (Optional) 来源
        """

        self.id = id
        self.prod = prod
        self.eName = eName
        self.createTime = createTime
        self.userCount = userCount
        self.status = status
        self.updateTime = updateTime
        self.creator = creator
        self.receiver = receiver
        self.oldName = oldName
        self.clientType = clientType
        self.codeSource = codeSource
