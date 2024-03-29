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


class DescribeZonesRes(object):

    def __init__(self, zoneId=None, zone=None, zoneType=None, recordCount=None, lock=None, retryRecurse=None, resolveStatus=None, createTime=None, bindVpc=None):
        """
        :param zoneId: (Optional) 域名id
        :param zone: (Optional) 域名
        :param zoneType: (Optional) 域名类型 LOCAL->云内全局 PTR->反向解析zone PV->私有zone
        :param recordCount: (Optional) 解析记录个数
        :param lock: (Optional) 是否锁定 true->锁定 false->未锁定
        :param retryRecurse: (Optional) 解析失败后是否进行递归解析
        :param resolveStatus: (Optional) 解析状态 NONE->没有解析 NORMAL->正常解析 PARTIAL->部分解析 PAUSE->暂停解析
        :param createTime: (Optional) 创建时间, UTC时间格式，例如2017-11-10T23:00:00Z
        :param bindVpc: (Optional) 绑定的vpc信息
        """

        self.zoneId = zoneId
        self.zone = zone
        self.zoneType = zoneType
        self.recordCount = recordCount
        self.lock = lock
        self.retryRecurse = retryRecurse
        self.resolveStatus = resolveStatus
        self.createTime = createTime
        self.bindVpc = bindVpc
