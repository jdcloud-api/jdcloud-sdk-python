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


class DescribeDDoSIpAttackLogsRequest(JDCloudRequest):
    """
    查询高防IP的 DDoS 攻击日志, 仅BGP实例返回的是IP级别的攻击记录, 非BGP实例返回的仍是实例级别的攻击记录(serviceIp 字段为空)
参数 serviceIp 优先级大于 instanceId.
- 指定 serviceIp 参数时, 忽略 instanceId 参数, 查询 ip 相关攻击记录.
- 未指定 serviceIp 时, 查询 instanceId 指定实例相关攻击记录.
- serviceIp 和 instanceId 均未指定时, 查询用户所有攻击记录

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeDDoSIpAttackLogsRequest, self).__init__(
            '/regions/{regionId}/attacklog:describeDDoSIpAttackLogs', 'GET', header, version)
        self.parameters = parameters


class DescribeDDoSIpAttackLogsParameters(object):

    def __init__(self, regionId,startTime, ):
        """
        :param regionId: 区域 ID, 高防不区分区域, 传 cn-north-1 即可
        :param startTime: 开始时间, 只能查询最近 90 天以内的数据, UTC 时间, 格式: yyyy-MM-dd'T'HH:mm:ssZ
        """

        self.regionId = regionId
        self.pageNumber = None
        self.pageSize = None
        self.startTime = startTime
        self.endTime = None
        self.instanceId = None
        self.serviceIp = None

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

    def setServiceIp(self, serviceIp):
        """
        :param serviceIp: (Optional) 高防IP列表. <br>- 使用 <a href='http://docs.jdcloud.com/anti-ddos-pro/api/describeServiceIpList'>describeServiceIpList</a> 接口查询实例的高防 IP
        """
        self.serviceIp = serviceIp

