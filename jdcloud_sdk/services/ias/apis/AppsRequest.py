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


class AppsRequest(JDCloudRequest):
    """
    运营后台查询app
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(AppsRequest, self).__init__(
            '/regions/{regionId}/operate_backend/apps', 'GET', header, version)
        self.parameters = parameters


class AppsParameters(object):

    def __init__(self, regionId, pin, appName, clientId, multiTenant, state, scope, startTime, endTime, accountType, pageIndex, pageSize, offset):
        """
        :param regionId: 
        :param pin: pin
        :param appName: appName
        :param clientId: clientId
        :param multiTenant: multiTenant
        :param state: state
        :param scope: scope
        :param startTime: startTime
        :param endTime: endTime
        :param accountType: accountType
        :param pageIndex: pageIndex
        :param pageSize: pageSize
        :param offset: offset
        """

        self.regionId = regionId
        self.pin = pin
        self.appName = appName
        self.clientId = clientId
        self.multiTenant = multiTenant
        self.state = state
        self.scope = scope
        self.startTime = startTime
        self.endTime = endTime
        self.accountType = accountType
        self.pageIndex = pageIndex
        self.pageSize = pageSize
        self.offset = offset
