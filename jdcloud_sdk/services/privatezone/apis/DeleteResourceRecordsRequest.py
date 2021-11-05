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


class DeleteResourceRecordsRequest(JDCloudRequest):
    """
    删除解析记录。批量删除时多个resourceRecordId用","分隔。批量删除每次最多不超过100个记录

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DeleteResourceRecordsRequest, self).__init__(
            '/regions/{regionId}/zone/{zoneId}/resourceRecords/{resourceRecordId}', 'DELETE', header, version)
        self.parameters = parameters


class DeleteResourceRecordsParameters(object):

    def __init__(self, regionId, zoneId, resourceRecordId, ):
        """
        :param regionId: 地域ID
        :param zoneId: zone id
        :param resourceRecordId: 解析记录ID
        """

        self.regionId = regionId
        self.zoneId = zoneId
        self.resourceRecordId = resourceRecordId

