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


class JmrTaskViewModel(object):

    def __init__(self, id=None, taskId=None, taskName=None, taskType=None, status=None, startTime=None, endTime=None, duration=None, userpin=None, dataCenter=None, jobId=None, planId=None, workflowId=None, workflowInstanceId=None):
        """
        :param id: (Optional) 
        :param taskId: (Optional) 作业Id
        :param taskName: (Optional) 作业名称
        :param taskType: (Optional) 作业类型
        :param status: (Optional) 状态
        :param startTime: (Optional) 开始时间
        :param endTime: (Optional) 结束时间
        :param duration: (Optional) 持续时间
        :param userpin: (Optional) 用户名
        :param dataCenter: (Optional) 数据中心，即regionId
        :param jobId: (Optional) 
        :param planId: (Optional) 
        :param workflowId: (Optional) 工作流Id
        :param workflowInstanceId: (Optional) 工作流实例Id
        """

        self.id = id
        self.taskId = taskId
        self.taskName = taskName
        self.taskType = taskType
        self.status = status
        self.startTime = startTime
        self.endTime = endTime
        self.duration = duration
        self.userpin = userpin
        self.dataCenter = dataCenter
        self.jobId = jobId
        self.planId = planId
        self.workflowId = workflowId
        self.workflowInstanceId = workflowInstanceId
