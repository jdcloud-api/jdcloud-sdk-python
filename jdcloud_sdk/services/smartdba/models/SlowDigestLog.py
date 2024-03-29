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


class SlowDigestLog(object):

    def __init__(self, execTime=None, lockTime=None, rowsSent=None, rowsExamined=None, sql=None, database=None, queryCount=None):
        """
        :param execTime: (Optional) 执行时间
        :param lockTime: (Optional) 锁等待时间
        :param rowsSent: (Optional) 返回行数
        :param rowsExamined: (Optional) 扫描行数
        :param sql: (Optional) sql模板
        :param database: (Optional) 数据库
        :param queryCount: (Optional) 执行次数
        """

        self.execTime = execTime
        self.lockTime = lockTime
        self.rowsSent = rowsSent
        self.rowsExamined = rowsExamined
        self.sql = sql
        self.database = database
        self.queryCount = queryCount
