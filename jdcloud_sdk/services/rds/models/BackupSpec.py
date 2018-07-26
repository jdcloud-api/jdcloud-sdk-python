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


class BackupSpec(object):

    def __init__(self, backupName=None, dbNames=None):
        """
        :param backupName: (Optional) 备份名称，缺省系统将分配一个随机名称
        :param dbNames: (Optional) 需要备份的数据库名称列表。如不填，则备份整个实例。</br>SQL Server支持该参数</br><strong>MySQL不支持该参数</strong>
        """

        self.backupName = backupName
        self.dbNames = dbNames
