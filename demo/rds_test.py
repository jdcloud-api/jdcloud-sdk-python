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
from jdcloud_sdk.services.rds.apis.CreateBackupRequest import *
from jdcloud_sdk.services.rds.models.BackupSpec import *
from jdcloud_sdk.services.rds.models.DBInstanceSpec import *
from jdcloud_sdk.services.rds.apis.CreateInstanceRequest import *
from jdcloud_sdk.services.rds.apis.DescribeInstancesRequest import *
from jdcloud_sdk.services.common.models.Filter import *
from jdcloud_sdk.services.charge.models.ChargeSpec import *
from jdcloud_sdk.services.rds.apis.CreateInstanceByTimeRequest import *
from jdcloud_sdk.services.rds.apis.CreateInstanceFromBackupRequest import *
from jdcloud_sdk.services.rds.models.RestoredNewDBInstanceSpec import *


class RdsTest(unittest.TestCase):
    def setUp(self):
        access_key = 'ak'
        secret_key = 'sk'
        self.credential = Credential(access_key, secret_key)
        self.client = RdsClient(self.credential)

    # 查询实例列表
    def testDescribeInstances(self):
        parameters = DescribeInstancesParameters(regionId="cn-north-1")
        filter = Filter(name="engine", values=["SQL Server"])
        parameters.setFilters([filter])
        request = DescribeInstancesRequest(parameters)
        resp = self.client.send(request)

    # 创建实例
    def testCreateInstance(self):
        charge_spec = ChargeSpec(chargeMode="postpaid_by_duration")
        instance_spec = DBInstanceSpec(engine="SQL Server", engineVersion="2008R2 EE", instanceClass="db.sqlsvr.s1.large", instanceStorageGB=200, azId=["cn-north-1a"], vpcId="vpc-xx", subnetId="subnet-xx", chargeSpec=charge_spec, instanceName="test")
        parameters = CreateInstanceParameters(regionId="cn-north-1", instanceSpec=instance_spec)
        request = CreateInstanceRequest(parameters)
        resp = self.client.send(request)

    # 根据时间点创建
    def testCreateInstanceByTime(self):
        charge_spec = ChargeSpec(chargeMode="postpaid_by_duration")
        instance_spec = RestoredNewDBInstanceSpec(instanceClass="db.sqlsvr.s1.large", instanceStorageGB=200, azId=["cn-north-1a"], vpcId="vpc-xx", subnetId="subnet-xx", chargeSpec=charge_spec, instanceName="test_by_time")
        parameters = CreateInstanceByTimeParameters(regionId="cn-north-1", instanceId="sqlserver-pjxoc4o3tu", restoreTime="2019-05-06 02:00:37", instanceSpec=instance_spec)
        request = CreateInstanceByTimeRequest(parameters)
        resp = self.client.send(request)

    # 根据备份创建
    def testCreateInstanceFromBackup(self):
        charge_spec = ChargeSpec(chargeMode="postpaid_by_duration")
        instance_spec = RestoredNewDBInstanceSpec(instanceClass="db.sqlsvr.s1.large", instanceStorageGB=200, azId=["cn-north-1a"], vpcId="vpc-xx", subnetId="subnet-xx", chargeSpec=charge_spec, instanceName="test_by_backup")
        parameters = CreateInstanceFromBackupParameters(regionId="cn-north-1", backupId="sqlserver-xx", engine="SQL Server", instanceSpec=instance_spec)
        request = CreateInstanceFromBackupRequest(parameters)
        resp = self.client.send(request)

    # 创建账号
    def testCreateAccountRequest(self):
        parameters = CreateAccountParameters(regionId="cn-north-1", instanceId="sqlserver-tw2hff8xqf",accountName="testAccountpy",accountPassword="testPass1234")
        request = CreateAccountRequest(parameters)
        resp = self.client.send(request)

    # 删除账号
    def testDeleteAccountRequest(self):
        parameters = DeleteAccountParameters(regionId="cn-north-1", instanceId="sqlserver-tw2hff8xqf",accountName="testAccountpy")
        request = DeleteAccountRequest(parameters)
        resp = self.client.send(request)

    # 账号授权
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

    # 创建数据库
    def testCreateDatabaseRequest(self):
        parameters = CreateDatabaseParameters(regionId="cn-north-1", instanceId="sqlserver-tw2hff8xqf", dbName="newtestforpython2",characterSetName="Chinese_PRC_CI_AS")
        request = CreateDatabaseRequest(parameters)
        resp = self.client.send(request)

    # 删除数据库
    def testDeleteDatabaseRequest(self):
        parameters = DeleteDatabaseParameters(regionId="cn-north-1", instanceId="sqlserver-tw2hff8xqf", dbName="newtestforpython2")
        request = DeleteDatabaseRequest(parameters)
        resp = self.client.send(request)
        # self.assertTrue(resp.error is not None)
        # self.assertEqual(400, resp.error.code)

    # 创建数据库备份
    def testCreateBackupRequest(self):
        dbNames=["newtestforpython2"]
        backup_spec = BackupSpec(backupName="testBackup",dbNames=dbNames)
        parameters = CreateBackupParameters(regionId="cn-north-1")
        parameters.setInstanceId("sqlserver-tw2hff8xqf")
        parameters.setBackupSpec(backup_spec)
        request = CreateBackupRequest(parameters)
        resp = self.client.send(request)

    # 获取备份列表信息
    def testDescribeBackupsRequest(self):
        parameters = DescribeBackupsParameters('cn-north-1', "sqlserver-tw2hff8xqf", 1, 20)
        request = DescribeBackupsRequest(parameters)

        resp = self.client.send(request)
        self.assertTrue(resp.error is None)

    # 获取备份下载链接
    def testDescribeBackupDoenloadURLRequest(self):
        parameters = DescribeBackupDownloadURLParameters('cn-north-1', "sqlserver-9bbd056c-2d8a-4b76-aae9-a812d3c623c0")
        parameters.setFileName("newtestforpython2.bak")
        request = DescribeBackupDownloadURLRequest(parameters)
        resp = self.client.send(request)
        self.assertTrue(resp.error is None)
