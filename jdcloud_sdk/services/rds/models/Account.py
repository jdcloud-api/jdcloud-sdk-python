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


class Account(object):

    def __init__(self, accountName=None, accountStatus=None, accountType=None, createTime=None, updateTime=None, notes=None, createDB=None, createRole=None, replication=None, accountPrivileges=None):
        """
        :param accountName: (Optional) 账号名，账号名的具体规则可参见帮助中心文档:[名称及密码限制](../../../documentation/Database-and-Cache-Service/RDS/Introduction/Restrictions/SQLServer-Restrictions.md)
        :param accountStatus: (Optional) 账号状态，参见[枚举参数定义](../Enum-Definitions/Enum-Definitions.md)<br>- **MySQL：不支持，不返回该字段**<br>- **SQL Server：返回该字段**
        :param accountType: (Optional) 账号类型，normal：普通，super：高权限<br>- 支持SQL Server，PostgreSQL
        :param createTime: (Optional) 创建账号时间，格式为：YYYY-MM-DD HH:mm:ss<br>- 仅支持PostgreSQL，已弃用
        :param updateTime: (Optional) 修改账号时间，格式为：YYYY-MM-DD HH:mm:ss<br>- 仅支持PostgreSQL，已弃用
        :param notes: (Optional) 账号备注内容<br>- 仅支持PostgreSQL
        :param createDB: (Optional) 账号创建数据库权限
        :param createRole: (Optional) 账号创建角色权限
        :param replication: (Optional) 账号复制权限
        :param accountPrivileges: (Optional) 具有的权限
        """

        self.accountName = accountName
        self.accountStatus = accountStatus
        self.accountType = accountType
        self.createTime = createTime
        self.updateTime = updateTime
        self.notes = notes
        self.createDB = createDB
        self.createRole = createRole
        self.replication = replication
        self.accountPrivileges = accountPrivileges
