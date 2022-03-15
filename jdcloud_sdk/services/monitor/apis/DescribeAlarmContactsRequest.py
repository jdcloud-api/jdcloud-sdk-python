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


class DescribeAlarmContactsRequest(JDCloudRequest):
    """
    查询规则的报警联系人
    """

    def __init__(self, parameters, header=None, version="v2"):
        super(DescribeAlarmContactsRequest, self).__init__(
            '/groupAlarms/{alarmId}/contacts', 'GET', header, version)
        self.parameters = parameters


class DescribeAlarmContactsParameters(object):

    def __init__(self, alarmId,):
        """
        :param alarmId: 规则id
        """

        self.alarmId = alarmId
        self.pageNumber = None
        self.pageSize = None
        self.referenceType = None

    def setPageNumber(self, pageNumber):
        """
        :param pageNumber: (Optional) 当前所在页，默认为1
        """
        self.pageNumber = pageNumber

    def setPageSize(self, pageSize):
        """
        :param pageSize: (Optional) 页面大小，默认为20；取值范围[1, 100]
        """
        self.pageSize = pageSize

    def setReferenceType(self, referenceType):
        """
        :param referenceType: (Optional) 联系人类型。0,联系人分组; 1,联系人
        """
        self.referenceType = referenceType

