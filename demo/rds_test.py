# coding=utf8

# Copyright 2018-2025 JDCLOUD.COM
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http:#www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest
from jdcloud_sdk.core.credential import Credential
from jdcloud_sdk.core.config import *
from jdcloud_sdk.core.const import *
from jdcloud_sdk.services.rds.client.RdsClient import RdsClient
from jdcloud_sdk.services.rds.apis.DescribeBackupsRequest import *
from jdcloud_sdk.services.rds.apis.DescribeBackupDownloadURLRequest import *
from jdcloud_sdk.services.rds.apis.CreateDatabaseRequest import *
from jdcloud_sdk.services.rds.apis.DeleteDatabaseRequest import *
from jdcloud_sdk.services.rds.apis.CreateAccountRequest import *
from jdcloud_sdk.services.rds.apis.DeleteAccountRequest import *
from jdcloud_sdk.services.rds.apis.GrantPrivilegeRequest import *
from jdcloud_sdk.services.rds.models.AccountPrivilege import *
from jdcloud_sdk.services.rds.apis.ResetPasswordRequest import *
from jdcloud_sdk.services.rds.apis.RestoreSingleDatabaseRequest import *
from jdcloud_sdk.services.rds.apis.CreateBackupRequest import *
from jdcloud_sdk.services.rds.models.BackupSpec import *


class RdsTest(unittest.TestCase):
    def setUp(self):
        access_key = 'ak'
        secret_key = 'sk'
        self.credential = Credential(access_key, secret_key)
        self.client = RdsClient(self.credential)
    #创建账号
    def testCreateAccountRequest(self):
        parameters = CreateAccountParameters(regionId="cn-north-1", instanceId="sqlserver-tw2hff8xqf",accountName="testAccountpy",accountPassword="testPass1234")
        request = CreateAccountRequest(parameters)
        resp = self.client.send(request)
    #删除账号
    def testDeleteAccountRequest(self):
        parameters = DeleteAccountParameters(regionId="cn-north-1", instanceId="sqlserver-tw2hff8xqf",accountName="testAccountpy")
        request = DeleteAccountRequest(parameters)
        resp = self.client.send(request)
    #账号授权
    def testGrantPrivilegeRequest(self):
        privilege = AccountPrivilege(dbName="newtestforpython",privilege="ro")
        account_privileges = [privilege]
        parameters = GrantPrivilegeParameters(regionId="cn-north-1", instanceId="sqlserver-tw2hff8xqf",accountName="testAccountpy",accountPrivileges=account_privileges)
        request = GrantPrivilegeRequest(parameters)
        resp = self.client.send(request)
    #密码重置
    def testResetPasswordRequest(self):
        parameters = ResetPasswordParameters(regionId="cn-north-1", instanceId="sqlserver-tw2hff8xqf",accountName="testAccountpy",accountPassword="testPass12345")
        request = ResetPasswordRequest(parameters)
        resp = self.client.send(request)

    #创建数据库
    def testCreateDatabaseRequest(self):
        parameters = CreateDatabaseParameters(regionId="cn-north-1", instanceId="sqlserver-tw2hff8xqf", dbName="newtestforpython2",characterSetName="Chinese_PRC_CI_AS")
        request = CreateDatabaseRequest(parameters)
        resp = self.client.send(request)

    #删除数据库
    def testDeleteDatabaseRequest(self):
        parameters = DeleteDatabaseParameters(regionId="cn-north-1", instanceId="sqlserver-tw2hff8xqf", dbName="newtestforpython2")
        request = DeleteDatabaseRequest(parameters)
        resp = self.client.send(request)
        # self.assertTrue(resp.error is not None)
        # self.assertEqual(400, resp.error.code)

    #单库备份恢复
    def testRestoreSingleDatabaseRequest(self):
        parameters = RestoreSingleDatabaseParameters(regionId="cn-north-1", instanceId="sqlserver-tw2hff8xqf", dbName="newtestforpython2",backupId="sqlserver-9bbd056c-2d8a-4b76-aae9-a812d3c623c0",backupFileName="newtestforpython2.bak")
        request = RestoreSingleDatabaseRequest(parameters)
        resp = self.client.send(request)

    #创建数据库备份
    def testCreateBackupRequest(self):
        dbNames=["newtestforpython2"]
        backup_spec = BackupSpec(backupName="testBackup",dbNames=dbNames)
        parameters = CreateBackupParameters(regionId="cn-north-1", instanceId="sqlserver-tw2hff8xqf",backupSpec=backup_spec)
        request = CreateBackupRequest(parameters)
        resp = self.client.send(request)

    #获取备份列表信息
    def testDescribeBackupsRequest(self):
        parameters = DescribeBackupsParameters('cn-north-1', "sqlserver-tw2hff8xqf", None, 1, 20)
        request = DescribeBackupsRequest(parameters)

        resp = self.client.send(request)
        self.assertTrue(resp.error is None)

    #获取备份下载链接
    def testDescribeBackupDoenloadURLRequest(self):
        parameters = DescribeBackupDownloadURLParameters('cn-north-1', "sqlserver-9bbd056c-2d8a-4b76-aae9-a812d3c623c0", "newtestforpython2.bak")
        request = DescribeBackupDownloadURLRequest(parameters)
        resp = self.client.send(request)
        self.assertTrue(resp.error is None)
