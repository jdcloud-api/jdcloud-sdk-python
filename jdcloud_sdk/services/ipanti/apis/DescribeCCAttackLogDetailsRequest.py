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

from jdcloud_sdk.core.jdcloudrequest import JDCloudRequest


class DescribeCCAttackLogDetailsRequest(JDCloudRequest):
    """
    查询 CC 攻击日志详情.
- 参数 attackId 优先级高于 instanceId, attackId 不为空时, 忽略 instanceId

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeCCAttackLogDetailsRequest, self).__init__(
            '/regions/{regionId}/attacklog:describeCCAttackLogDetails', 'GET', header, version)
        self.parameters = parameters


class DescribeCCAttackLogDetailsParameters(object):

    def __init__(self, regionId,):
        """
        :param regionId: 区域 ID, 高防不区分区域, 传 cn-north-1 即可
        """

        self.regionId = regionId
        self.pageNumber = None
        self.pageSize = None
        self.startTime = None
        self.endTime = None
        self.instanceId = None
        self.subDomain = None
        self.attackId = None

    def setPageNumber(self, pageNumber):
        """
        :param pageNumber: (Optional) 页码, 默认为1
        """
        self.pageNumber = pageNumber

    def setPageSize(self, pageSize):
        """
        :param pageSize: (Optional) 分页大小, 默认为10, 取值范围[10, 100]
        """
        self.pageSize = pageSize

    def setStartTime(self, startTime):
        """
        :param startTime: (Optional) 开始时间, 只能查询最近 90 天以内的数据, UTC 时间, 格式: yyyy-MM-dd'T'HH:mm:ssZ, attackId 为空时必传
        """
        self.startTime = startTime

    def setEndTime(self, endTime):
        """
        :param endTime: (Optional) 查询的结束时间, UTC 时间, 格式: yyyy-MM-dd'T'HH:mm:ssZ
        """
        self.endTime = endTime

    def setInstanceId(self, instanceId):
        """
        :param instanceId: (Optional) 高防实例 ID
        """
        self.instanceId = instanceId

    def setSubDomain(self, subDomain):
        """
        :param subDomain: (Optional) 查询的子域名, 只有选中某一个实例后才能多选子域名
        """
        self.subDomain = subDomain

    def setAttackId(self, attackId):
        """
        :param attackId: (Optional) CC 攻击记录 Id, 不为空时忽略 startTime, endTime
        """
        self.attackId = attackId

