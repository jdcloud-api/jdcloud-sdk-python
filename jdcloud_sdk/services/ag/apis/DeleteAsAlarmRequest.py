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


class DeleteAsAlarmRequest(JDCloudRequest):
    """
    删除告警任务
- 所有参数取值为字符串类型的都严格区分大小写
- 伸缩功能开启或者关闭的情况下，都支持调用此接口
- 目标跟踪规则生成的告警任务不允许删除
- 告警任务关联简单规则，告警任务可以删除
- 告警任务关联步进规则，告警任务不允许删除，但是可以删除步进规则，删除步进规则后，关联的告警任务会保留

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DeleteAsAlarmRequest, self).__init__(
            '/regions/{regionId}/asAlarms/{asAlarmId}', 'DELETE', header, version)
        self.parameters = parameters


class DeleteAsAlarmParameters(object):

    def __init__(self,regionId, asAlarmId):
        """
        :param regionId: 地域ID
        :param asAlarmId: 告警任务ID
        """

        self.regionId = regionId
        self.asAlarmId = asAlarmId

