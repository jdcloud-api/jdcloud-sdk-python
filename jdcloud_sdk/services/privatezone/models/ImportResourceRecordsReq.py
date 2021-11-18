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


class ImportResourceRecordsReq(object):

    def __init__(self, hostValue, recordType, hostRecord=None, ttl=None, priority=None, port=None, weight=None):
        """
        :param hostRecord: (Optional) 主机记录
        :param hostValue:  主机记录值
        :param recordType:  解析类型，目前支持类型 A AAAA CNAME TXT CAA SRV MX PTR
        :param ttl: (Optional) TTL值
        :param priority: (Optional) 优先级，只存在于MX, SRV解析记录类型
        :param port: (Optional) 端口，只存在于SRV解析记录类型
        :param weight: (Optional) 解析记录的权重
        """

        self.hostRecord = hostRecord
        self.hostValue = hostValue
        self.recordType = recordType
        self.ttl = ttl
        self.priority = priority
        self.port = port
        self.weight = weight