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


class GetViewTreeRequest(JDCloudRequest):
    """
    查询DNS所有解析线路
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(GetViewTreeRequest, self).__init__(
            '/regions/{regionId}/domain/{domainId}/viewTree', 'GET', header, version)
        self.parameters = parameters


class GetViewTreeParameters(object):

    def __init__(self, regionId, domainId, packId, viewId):
        """
        :param regionId: Region ID
        :param domainId: 域名ID
        :param packId: 套餐ID
        :param viewId: view ID，默认为0
        """

        self.regionId = regionId
        self.domainId = domainId
        self.loadMode = None
        self.packId = packId
        self.viewId = viewId

    def setLoadMode(self, loadMode):
        """
        :param loadMode: (Optional) 展示方式
        """
        self.loadMode = loadMode

