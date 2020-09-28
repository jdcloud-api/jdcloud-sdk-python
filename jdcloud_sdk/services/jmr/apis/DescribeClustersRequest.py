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


class DescribeClustersRequest(JDCloudRequest):
    """
    查询用户集群的列表

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeClustersRequest, self).__init__(
            '/regions/{regionId}/clusters', 'GET', header, version)
        self.parameters = parameters


class DescribeClustersParameters(object):

    def __init__(self, regionId, ):
        """
        :param regionId: 地域ID
        """

        self.regionId = regionId
        self.dataCenter = None
        self.status = None
        self.clusterName = None
        self.orderBy = None
        self.pageNum = None
        self.pageSize = None

    def setDataCenter(self, dataCenter):
        """
        :param dataCenter: (Optional) 地域
        """
        self.dataCenter = dataCenter

    def setStatus(self, status):
        """
        :param status: (Optional) 集群状态，CREATING，RUNNING，RELEASED，FAILED等
        """
        self.status = status

    def setClusterName(self, clusterName):
        """
        :param clusterName: (Optional) 集群名称
        """
        self.clusterName = clusterName

    def setOrderBy(self, orderBy):
        """
        :param orderBy: (Optional) 排序，比如 id desc
        """
        self.orderBy = orderBy

    def setPageNum(self, pageNum):
        """
        :param pageNum: (Optional) 页数，默认为1
        """
        self.pageNum = pageNum

    def setPageSize(self, pageSize):
        """
        :param pageSize: (Optional) 每页数目，默认为10
        """
        self.pageSize = pageSize

