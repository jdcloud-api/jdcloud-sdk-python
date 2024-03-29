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


class DescribeDispatchRulesRequest(JDCloudRequest):
    """
    查询某个实例下的防护调度规则
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeDispatchRulesRequest, self).__init__(
            '/regions/{regionId}/instances/{instanceId}/dispatchRules', 'GET', header, version)
        self.parameters = parameters


class DescribeDispatchRulesParameters(object):

    def __init__(self, regionId,instanceId,):
        """
        :param regionId: 区域 ID, 高防不区分区域, 传 cn-north-1 即可
        :param instanceId: 高防实例 Id
        """

        self.regionId = regionId
        self.instanceId = instanceId
        self.pageNumber = None
        self.pageSize = None
        self.name = None
        self.innerIp = None
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

    def setName(self, name):
        """
        :param name: (Optional) 实例名称, 可模糊匹配
        """
        self.name = name

    def setInnerIp(self, innerIp):
        """
        :param innerIp: (Optional) 云内IP, 可模糊匹配
        """
        self.innerIp = innerIp

    def setServiceIp(self, serviceIp):
        """
        :param serviceIp: (Optional) 高防IP, 可模糊匹配
        """
        self.serviceIp = serviceIp

