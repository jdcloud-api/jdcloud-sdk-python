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
import time
from jdcloud_sdk.core.credential import Credential
from jdcloud_sdk.core.const import SCHEME_HTTP
from jdcloud_sdk.core.config import Config
from jdcloud_sdk.core.logger import Logger
from jdcloud_sdk.services.vm.client.VmClient import VmClient
from jdcloud_sdk.services.vm.apis.DescribeInstanceTypesRequest import *
from jdcloud_sdk.services.vm.apis.DescribeInstancesRequest import *
from jdcloud_sdk.services.vm.apis.DescribeInstanceRequest import *
from jdcloud_sdk.services.vm.apis.CreateInstancesRequest import *
from jdcloud_sdk.services.vm.apis.DeleteInstanceRequest import *
from jdcloud_sdk.services.vm.apis.StopInstanceRequest import *
from jdcloud_sdk.services.vm.models.InstanceSpec import InstanceSpec
from jdcloud_sdk.services.vm.models.InstanceNetworkInterfaceAttachmentSpec import InstanceNetworkInterfaceAttachmentSpec
from jdcloud_sdk.services.vm.models.InstanceDiskAttachmentSpec import InstanceDiskAttachmentSpec
from jdcloud_sdk.services.vpc.models.NetworkInterfaceSpec import NetworkInterfaceSpec
from jdcloud_sdk.services.common.models.Filter import Filter


class VmTest(unittest.TestCase):

    def setUp(self):
        access_key = 'ak'
        secret_key = 'sk'
        self.credential = Credential(access_key, secret_key)
        # 指定使用http方式访问vpc专用域名，超时为20s
        config = Config('vm.internal.cn-north-1.jdcloud-api.com', SCHEME_HTTP, 20)
        logger = Logger(3) # FATAL = 0 ERROR = 1 WARN = 2 INFO = 3；如果不想输出日志，可将日志级别设置为0（FATAL）；不设置logger，则默认为INFO
        self.client = VmClient(self.credential, config, logger)

    def testDescribeInstanceTypes(self):
        parameters = DescribeInstanceTypesParameters('cn-north-1')
        request = DescribeInstanceTypesRequest(parameters)

        resp = self.client.send(request)
        self.assertTrue(resp.error is None)

    def testDescribeInstances(self):
        param = DescribeInstancesParameters('cn-north-1')
        request = DescribeInstancesRequest(param)

        resp = self.client.send(request)
        self.assertTrue(resp.error is None)

    def testDescribeInstancesPaging(self):
        param = DescribeInstancesParameters('cn-north-1')
        param.setPageNumber(2)
        param.setPageSize(10)
        request = DescribeInstancesRequest(param)

        resp = self.client.send(request)
        self.assertEqual(10, len(resp.result['instances']))

    def testDescribeInstancesFilter(self):
        f = Filter('instanceId', ['i-d4c1a56z3p'], 'eq')
        param = DescribeInstancesParameters('cn-north-1')
        param.setFilters([f])
        request = DescribeInstancesRequest(param)

        resp = self.client.send(request)
        self.assertEqual(1, len(resp.result['instances']))

    def testDescribeInstance(self):
        param = DescribeInstanceParameters('cn-north-1', 'i-d4c1a56z3p')
        request = DescribeInstanceRequest(param)

        resp = self.client.send(request)
        self.assertTrue(resp.error is None)

    def testCreateAndDeleteInstance(self):
        # create instance
        networkInterface = NetworkInterfaceSpec(az='cn-north-1a', subnetId='subnet-3dm13k30gh')
        network = InstanceNetworkInterfaceAttachmentSpec(networkInterface=networkInterface)
        sysDisk = InstanceDiskAttachmentSpec('local')
        instanceSpec = InstanceSpec(az='cn-north-1a', instanceType='g.s1.micro', name='python-sdk-test',
                                    imageId='98d44a0f-88c1-451a-8971-f1f769073b6c',
                                    primaryNetworkInterface=network, systemDisk=sysDisk,
                                    dataDisks=None, keyNames=None, description='python-sdk-vm')
        param = CreateInstancesParameters('cn-north-1', instanceSpec)
        param.setMaxCount(1)
        request = CreateInstancesRequest(param)
        create_resp = self.client.send(request)
        self.assertTrue(create_resp.error is None)
        instance_id = create_resp.result['instanceIds'][0]

        # stop instance
        def _stop_instance():
            param = StopInstanceParameters('cn-north-1', instance_id)
            request = StopInstanceRequest(param)
            stop_resp = self.client.send(request)
            return stop_resp.error is None

        result = self._try(10, 5, _stop_instance)
        self.assertTrue(result)

        # delete instance, may need try many times
        def _delete_instance():
            param = DeleteInstanceParameters('cn-north-1', instance_id)
            request = DeleteInstanceRequest(param)
            delete_resp = self.client.send(request)
            return delete_resp.error is None

        result = self._try(10, 5, _delete_instance)
        self.assertTrue(result)

    def _try(self, count, wait, func):
        try_count = count
        result = False
        while try_count > 0:
            print 'try_count=', try_count
            time.sleep(wait)
            result = func()
            if result:
                break
            try_count -= 1
        return result

