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


class DmsPrivilegeVO(object):

    def __init__(self, id=None, username=None, pin=None, privilegeName=None, instanceId=None, instanceName=None, databaseName=None, tableName=None, fieldName=None, authStatus=None, authDate=None, expireDate=None, releaseStatus=None, instanceType=None, regionId=None):
        """
        :param id: (Optional) 主键Id。
        :param username: (Optional) 用户名。
        :param pin: (Optional) 用户pin。
        :param privilegeName: (Optional) 用户权限名称。
        :param instanceId: (Optional) 实例ID。
        :param instanceName: (Optional) 实例名称。
        :param databaseName: (Optional) 数据库库名。
        :param tableName: (Optional) 表名。
        :param fieldName: (Optional) 字段名称。
        :param authStatus: (Optional) 授权状态。
        :param authDate: (Optional) 用户的添加时间，格式为：YYYY-MM-DD HH:mm:ss。
        :param expireDate: (Optional) 用户的添加时间，格式为：YYYY-MM-DD HH:mm:ss。
        :param releaseStatus: (Optional) 权限是否已经释放。
        :param instanceType: (Optional) 实例类型。
        :param regionId: (Optional) 实例所属区域。
        """

        self.id = id
        self.username = username
        self.pin = pin
        self.privilegeName = privilegeName
        self.instanceId = instanceId
        self.instanceName = instanceName
        self.databaseName = databaseName
        self.tableName = tableName
        self.fieldName = fieldName
        self.authStatus = authStatus
        self.authDate = authDate
        self.expireDate = expireDate
        self.releaseStatus = releaseStatus
        self.instanceType = instanceType
        self.regionId = regionId
