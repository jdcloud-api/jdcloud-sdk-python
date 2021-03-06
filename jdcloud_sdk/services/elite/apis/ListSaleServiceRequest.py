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


class ListSaleServiceRequest(JDCloudRequest):
    """
    分页查询交付单信息
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(ListSaleServiceRequest, self).__init__(
            '/regions/{regionId}/listSaleService', 'GET', header, version)
        self.parameters = parameters


class ListSaleServiceParameters(object):

    def __init__(self, regionId, pageNo, pageSize, ):
        """
        :param regionId: 地域ID
        :param pageNo: 页码（最小1）
        :param pageSize: 每页记录数（最小10，最大100）
        """

        self.regionId = regionId
        self.pageNo = pageNo
        self.pageSize = pageSize
        self.deliverNumber = None
        self.deliverStatus = None
        self.createDtStart = None
        self.createDtEnd = None

    def setDeliverNumber(self, deliverNumber):
        """
        :param deliverNumber: (Optional) 交付单号
        """
        self.deliverNumber = deliverNumber

    def setDeliverStatus(self, deliverStatus):
        """
        :param deliverStatus: (Optional) 交付状态
        """
        self.deliverStatus = deliverStatus

    def setCreateDtStart(self, createDtStart):
        """
        :param createDtStart: (Optional) 交付单创建起始时间，格式：yyyy-MM-dd HH:mm:ss
        """
        self.createDtStart = createDtStart

    def setCreateDtEnd(self, createDtEnd):
        """
        :param createDtEnd: (Optional) 交付单创建结束时间，格式：yyyy-MM-dd HH:mm:ss
        """
        self.createDtEnd = createDtEnd

