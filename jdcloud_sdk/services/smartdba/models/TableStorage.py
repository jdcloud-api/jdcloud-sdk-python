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


class TableStorage(object):

    def __init__(self, tableName=None, dbName=None, engine=None, totalSize=None, percentage=None, dataSize=None, idxSize=None, fragment=None, dataRows=None):
        """
        :param tableName: (Optional) 表名
        :param dbName: (Optional) 数据库名
        :param engine: (Optional) 引擎类型
        :param totalSize: (Optional) 表空间
        :param percentage: (Optional) 表空间占比，如 40%
        :param dataSize: (Optional) 数据空间
        :param idxSize: (Optional) 索引空间
        :param fragment: (Optional) 碎片率，如 0.99%
        :param dataRows: (Optional) 表行数
        """

        self.tableName = tableName
        self.dbName = dbName
        self.engine = engine
        self.totalSize = totalSize
        self.percentage = percentage
        self.dataSize = dataSize
        self.idxSize = idxSize
        self.fragment = fragment
        self.dataRows = dataRows
