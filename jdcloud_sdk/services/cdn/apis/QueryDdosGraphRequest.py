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


class QueryDdosGraphRequest(JDCloudRequest):
    """
    DDOS攻击报表接口
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(QueryDdosGraphRequest, self).__init__(
            '/netProtectionData:ddosGraph', 'POST', header, version)
        self.parameters = parameters


class QueryDdosGraphParameters(object):

    def __init__(self,):
        """
        """

        self.startTime = None
        self.endTime = None

    def setStartTime(self, startTime):
        """
        :param startTime: (Optional) 查询起始时间,UTC时间，格式为:yyyy-MM-dd'T'HH:mm:ss'Z'，示例:2019-08-16T06:00:00Z
        """
        self.startTime = startTime

    def setEndTime(self, endTime):
        """
        :param endTime: (Optional) 查询截止时间,UTC时间，格式为:yyyy-MM-dd'T'HH:mm:ss'Z'，示例:2019-08-16T07:00:00Z
        """
        self.endTime = endTime

