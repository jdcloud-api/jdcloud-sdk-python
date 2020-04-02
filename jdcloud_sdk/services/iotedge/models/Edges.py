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


class Edges(object):

    def __init__(self, edgeName=None, productKey=None, identifier=None, status=None, createTime=None, lastOnlineTime=None):
        """
        :param edgeName: (Optional) Edge名称
        :param productKey: (Optional) Edge产品Key
        :param identifier: (Optional) Edge的identifier
        :param status: (Optional) 在线状态，0-未激活，1-离线状态，2-在线状态
        :param createTime: (Optional) Edge创建时间
        :param lastOnlineTime: (Optional) 最后在线时间
        """

        self.edgeName = edgeName
        self.productKey = productKey
        self.identifier = identifier
        self.status = status
        self.createTime = createTime
        self.lastOnlineTime = lastOnlineTime