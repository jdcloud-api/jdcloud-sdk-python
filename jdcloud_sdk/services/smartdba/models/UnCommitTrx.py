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


class UnCommitTrx(object):

    def __init__(self, user=None, db=None, host=None, state=None, startTime=None, lastSql=None):
        """
        :param user: (Optional) 会话用户
        :param db: (Optional) 数据库
        :param host: (Optional) 会话源端IP
        :param state: (Optional) 当前状态
        :param startTime: (Optional) session开始时间
        :param lastSql: (Optional) 最后执行的sql
        """

        self.user = user
        self.db = db
        self.host = host
        self.state = state
        self.startTime = startTime
        self.lastSql = lastSql
