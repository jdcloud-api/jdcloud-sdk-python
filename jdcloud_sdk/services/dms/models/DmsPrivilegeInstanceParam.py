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


class DmsPrivilegeInstanceParam(object):

    def __init__(self, instanceId=None, instanceName=None, instanceType=None, regionId=None):
        """
        :param instanceId: (Optional) 实例Id。
        :param instanceName: (Optional) 实例名称。
        :param instanceType: (Optional) 实例类型。
        :param regionId: (Optional) 实例所属区域。
        """

        self.instanceId = instanceId
        self.instanceName = instanceName
        self.instanceType = instanceType
        self.regionId = regionId
