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


class DescribeCabinetsRequest(JDCloudRequest):
    """
    查询机柜列表
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeCabinetsRequest, self).__init__(
            '/idcs/{idc}/cabinets', 'GET', header, version)
        self.parameters = parameters


class DescribeCabinetsParameters(object):

    def __init__(self,idc, ):
        """
        :param idc: IDC机房ID
        """

        self.idc = idc
        self.pageNumber = None
        self.pageSize = None
        self.cabinetType = None
        self.cabinetOpenStatus = None
        self.cabinetNo = None
        self.filters = None
        self.sorts = None

    def setPageNumber(self, pageNumber):
        """
        :param pageNumber: (Optional) 页码, 默认为1
        """
        self.pageNumber = pageNumber

    def setPageSize(self, pageSize):
        """
        :param pageSize: (Optional) 分页大小，默认为20
        """
        self.pageSize = pageSize

    def setCabinetType(self, cabinetType):
        """
        :param cabinetType: (Optional) 机柜类型 formal:正式机柜 reserved:预留机柜
        """
        self.cabinetType = cabinetType

    def setCabinetOpenStatus(self, cabinetOpenStatus):
        """
        :param cabinetOpenStatus: (Optional) 机柜开通状态 disabled:未开通 enabling:开通中 enabled:已开通 disabling:关电中
        """
        self.cabinetOpenStatus = cabinetOpenStatus

    def setCabinetNo(self, cabinetNo):
        """
        :param cabinetNo: (Optional) 机柜编码
        """
        self.cabinetNo = cabinetNo

    def setFilters(self, filters):
        """
        :param filters: (Optional) roomNo - 房间号，精确匹配，支持多个
cabinetId - 机柜ID，精确匹配，支持多个
cabinetNo - 机柜编码，精确匹配，支持多个
cabinetOpenStatus - 机柜开通状态，精确匹配，支持多个

        """
        self.filters = filters

    def setSorts(self, sorts):
        """
        :param sorts: (Optional) cabinetNo - 机柜编码 roomNo - 房间号
        """
        self.sorts = sorts

