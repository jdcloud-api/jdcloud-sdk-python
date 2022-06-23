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


class CreateExportFlowRequest(JDCloudRequest):
    """
    创建数据导出工单
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(CreateExportFlowRequest, self).__init__(
            '/regions/{regionId}/exportFlow:create', 'POST', header, version)
        self.parameters = parameters


class CreateExportFlowParameters(object):

    def __init__(self, regionId,):
        """
        :param regionId: 地域代码，取值范围参见[《各地域及可用区对照表》](../Enum-Definitions/Regions-AZ.md)
        """

        self.regionId = regionId
        self.dataSourceId = None
        self.dbName = None
        self.taskPlanTypeEnum = None
        self.dbaApproveTypeEnum = None
        self.memo = None
        self.exportTypeEnum = None
        self.exportFileTypeEnum = None
        self.rowsNum = None
        self.ignoreError = None
        self.ignoreReason = None
        self.exportSqlText = None
        self.tableFilters = None
        self.exportContentTypeEnum = None

    def setDataSourceId(self, dataSourceId):
        """
        :param dataSourceId: (Optional) 数据库id
        """
        self.dataSourceId = dataSourceId

    def setDbName(self, dbName):
        """
        :param dbName: (Optional) 数据库名称
        """
        self.dbName = dbName

    def setTaskPlanTypeEnum(self, taskPlanTypeEnum):
        """
        :param taskPlanTypeEnum: (Optional) 执行方式，AUTO("AUTO", 0), BY_CREATOR("BY_CREATOR", 1)
        """
        self.taskPlanTypeEnum = taskPlanTypeEnum

    def setDbaApproveTypeEnum(self, dbaApproveTypeEnum):
        """
        :param dbaApproveTypeEnum: (Optional) DBA审批方式，AUTO("AUTO", 0), MANUAL("MANUAL", 1)
        """
        self.dbaApproveTypeEnum = dbaApproveTypeEnum

    def setMemo(self, memo):
        """
        :param memo: (Optional) 申请原因
        """
        self.memo = memo

    def setExportTypeEnum(self, exportTypeEnum):
        """
        :param exportTypeEnum: (Optional) 导出类型， RESULT_SET("RESULT_SET", 0), DB("DB", 1)
        """
        self.exportTypeEnum = exportTypeEnum

    def setExportFileTypeEnum(self, exportFileTypeEnum):
        """
        :param exportFileTypeEnum: (Optional) 导出格式，CSV("CSV", 0), SQL("SQL", 1)
        """
        self.exportFileTypeEnum = exportFileTypeEnum

    def setRowsNum(self, rowsNum):
        """
        :param rowsNum: (Optional) 影响行数，导出类型为结果集导出时，必填
        """
        self.rowsNum = rowsNum

    def setIgnoreError(self, ignoreError):
        """
        :param ignoreError: (Optional) 是否跳过检验，导出类型为结果集导出时，必填
        """
        self.ignoreError = ignoreError

    def setIgnoreReason(self, ignoreReason):
        """
        :param ignoreReason: (Optional) 跳过检验原因，ignoreError为true时，必填
        """
        self.ignoreReason = ignoreReason

    def setExportSqlText(self, exportSqlText):
        """
        :param exportSqlText: (Optional) 导出SQL文本，导出类型为结果集导出时，必填
        """
        self.exportSqlText = exportSqlText

    def setTableFilters(self, tableFilters):
        """
        :param tableFilters: (Optional) 导出表及过滤条件，为空时导出全部表。导出类型为数据库导出时，必填
        """
        self.tableFilters = tableFilters

    def setExportContentTypeEnum(self, exportContentTypeEnum):
        """
        :param exportContentTypeEnum: (Optional) 导出内容，DATA("DATA", 0), STRUCT("STRUCT", 1), STRUCT_DATA("STRUCT_DATA", 2)，导出类型为数据库导出时，必填
        """
        self.exportContentTypeEnum = exportContentTypeEnum

