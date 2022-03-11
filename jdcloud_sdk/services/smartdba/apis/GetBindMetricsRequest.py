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


class GetBindMetricsRequest(JDCloudRequest):
    """
    查询实例已经绑定的监控项
    """

    def __init__(self, parameters, header=None, version="v2"):
        super(GetBindMetricsRequest, self).__init__(
            '/regions/{regionId}/instance/{gid}/getBindMetrics', 'GET', header, version)
        self.parameters = parameters


class GetBindMetricsParameters(object):

    def __init__(self, regionId,gid,panelType, dbType):
        """
        :param regionId: 地域代码
        :param gid: panelType为real_time/monitor时,代表实例Id, panelType为market时，代表大盘 panelGid
        :param panelType: 展示类型，取值为： real_time 表示实时监控页面支持的自定义类型, monitor 表示性能趋势页面支持的类型
        :param dbType: 数据库库类型，目前只支持MySQL
        """

        self.regionId = regionId
        self.gid = gid
        self.panelType = panelType
        self.dbType = dbType
