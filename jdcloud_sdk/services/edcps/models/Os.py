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


class Os(object):

    def __init__(self, osTypeId=None, osName=None, osType=None, osVersion=None, deviceType=None):
        """
        :param osTypeId: (Optional) 操作系统系统类型ID
        :param osName: (Optional) 操作系统系统名称, 如 Ubuntu 16.04(x86_64)
        :param osType: (Optional) 操作系统类型, 如 ubuntu/centos
        :param osVersion: (Optional) 操作系统版本, 如 14.04/16.04
        :param deviceType: (Optional) 实例类型, 如 edcps.c.normal1
        """

        self.osTypeId = osTypeId
        self.osName = osName
        self.osType = osType
        self.osVersion = osVersion
        self.deviceType = deviceType
