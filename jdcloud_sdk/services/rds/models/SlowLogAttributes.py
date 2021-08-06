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


class SlowLogAttributes(object):

    def __init__(self, dbName=None, user=None, sql=None, executionTime=None, elapsedTime=None, lockTime=None, rowsExamined=None, rowsReturned=None):
        """
        :param dbName: (Optional) 数据库名，表示该SQL是在哪个数据库中执行的
        :param user: (Optional) 数据库账号，表示该SQL是哪个数据库账号发起的
        :param sql: (Optional) SQL语句
        :param executionTime: (Optional) SQL语句执行的开始时间，格式为YYYY-MM-DD hh:mm:ss
        :param elapsedTime: (Optional) SQL语句执行的时长，单位秒
        :param lockTime: (Optional) SQL语句等待锁的时间，单位秒
        :param rowsExamined: (Optional) SQL语句扫描的行数
        :param rowsReturned: (Optional) SQL语句返回的行数
        """

        self.dbName = dbName
        self.user = user
        self.sql = sql
        self.executionTime = executionTime
        self.elapsedTime = elapsedTime
        self.lockTime = lockTime
        self.rowsExamined = rowsExamined
        self.rowsReturned = rowsReturned
