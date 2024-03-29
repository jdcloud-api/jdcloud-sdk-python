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


class DmsOnlineTask(object):

    def __init__(self, id=None, dataSourceId=None, dbName=None, taskType=None, planTime=None, transaction=None, parallel=None, ignoreError=None, runStatus=None, createdDate=None, finishDate=None, createUser=None, status=None, message=None, runIp=None):
        """
        :param id: (Optional) 主键id。
        :param dataSourceId: (Optional) 数据源id。
        :param dbName: (Optional) 数据库名称。
        :param taskType: (Optional) 任务类型，DDL， DML。
        :param planTime: (Optional) 计划时间。
        :param transaction: (Optional) 是否为事务。
        :param parallel: (Optional) 是否为并行执行。
        :param ignoreError: (Optional) 是否忽略错误。
        :param runStatus: (Optional) 运行状态。CREATE("CREATE", 1),RUNNING("RUNNING", 2), SUCCESS("SUCCESS", 3), FAILED("FAILED", 4), SUSPEND("SUSPEND", 5);
        :param createdDate: (Optional) 创建日期。
        :param finishDate: (Optional) 结束日期。
        :param createUser: (Optional) 创建用户。
        :param status: (Optional) 状态0有效，1无效。
        :param message: (Optional) 执行消息。
        :param runIp: (Optional) 运行ip。
        """

        self.id = id
        self.dataSourceId = dataSourceId
        self.dbName = dbName
        self.taskType = taskType
        self.planTime = planTime
        self.transaction = transaction
        self.parallel = parallel
        self.ignoreError = ignoreError
        self.runStatus = runStatus
        self.createdDate = createdDate
        self.finishDate = finishDate
        self.createUser = createUser
        self.status = status
        self.message = message
        self.runIp = runIp
