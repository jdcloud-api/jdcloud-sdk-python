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


class Invocation(object):

    def __init__(self, status=None, commandId=None, commandName=None, sourceType=None, invokeId=None, instances=None, tags=None, invokeInstances=None, commandType=None, commandContent=None, commandDescription=None, invocationInstances=None, parameters=None, timeout=None, username=None, workdir=None, errorInfo=None, createTime=None, execTime=None):
        """
        :param status: (Optional) 命令执行状态,取值为：[`waiting`,`pending`,`running`,`stopping`,`failed`,`partial_failed`,`stopped`,`finish`]
        :param commandId: (Optional) 命令Id
        :param commandName: (Optional) 命令名称
        :param sourceType: (Optional) 命令来源，[`jdcloud`:公共命令, `self`:私有命令]
        :param invokeId: (Optional) 命令内容调用Id
        :param instances: (Optional) 请求执行命令的云主机Id
        :param tags: (Optional) 请求执行命令的云主机标签
        :param invokeInstances: (Optional) 执行命令的云主机
        :param commandType: (Optional) 命令类型
        :param commandContent: (Optional) 命令内容，base64编码
        :param commandDescription: (Optional) 命令描述
        :param invocationInstances: (Optional) 每个云主机的执行详情
        :param parameters: (Optional) 命令参数
        :param timeout: (Optional) 命令超时时间
        :param username: (Optional) 用户名
        :param workdir: (Optional) 命令执行路径
        :param errorInfo: (Optional) 命令调用的错误信息
        :param createTime: (Optional) 该次命令调用的开始时间
        :param execTime: (Optional) 该次命令配置的定时执行时间
        """

        self.status = status
        self.commandId = commandId
        self.commandName = commandName
        self.sourceType = sourceType
        self.invokeId = invokeId
        self.instances = instances
        self.tags = tags
        self.invokeInstances = invokeInstances
        self.commandType = commandType
        self.commandContent = commandContent
        self.commandDescription = commandDescription
        self.invocationInstances = invocationInstances
        self.parameters = parameters
        self.timeout = timeout
        self.username = username
        self.workdir = workdir
        self.errorInfo = errorInfo
        self.createTime = createTime
        self.execTime = execTime
