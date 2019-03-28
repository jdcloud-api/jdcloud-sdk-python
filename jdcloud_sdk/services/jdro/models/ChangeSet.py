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


class ChangeSet(object):

    def __init__(self, action=None, changeInfo=None, changeMap=None, createTime=None, describe=None, id=None, isRun=None, name=None, region=None, runTime=None, stackId=None, status=None, statusReason=None, templateId=None):
        """
        :param action: (Optional) 更改集操作
        :param changeInfo: (Optional) 更改信息
        :param changeMap: (Optional) changeset的详细信息
        :param createTime: (Optional) 创建时间
        :param describe: (Optional) 更改集描述
        :param id: (Optional) 
        :param isRun: (Optional) 是否执行
        :param name: (Optional) 更改集名称
        :param region: (Optional) 地域信息
        :param runTime: (Optional) 执行时间
        :param stackId: (Optional) 对应资源栈ID
        :param status: (Optional) 状态
        :param statusReason: (Optional) 状态原因
        :param templateId: (Optional) 对应模板ID
        """

        self.action = action
        self.changeInfo = changeInfo
        self.changeMap = changeMap
        self.createTime = createTime
        self.describe = describe
        self.id = id
        self.isRun = isRun
        self.name = name
        self.region = region
        self.runTime = runTime
        self.stackId = stackId
        self.status = status
        self.statusReason = statusReason
        self.templateId = templateId