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


class UpdateSubscribeRequest(JDCloudRequest):
    """
    更新日志消费
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(UpdateSubscribeRequest, self).__init__(
            '/regions/{regionId}/logsets/{logsetUID}/logtopics/{logtopicUID}/subscribe', 'PATCH', header, version)
        self.parameters = parameters


class UpdateSubscribeParameters(object):

    def __init__(self, regionId,logsetUID,logtopicUID,):
        """
        :param regionId: 地域 Id
        :param logsetUID: 日志集 UID
        :param logtopicUID: 日志主题 UID
        """

        self.regionId = regionId
        self.logsetUID = logsetUID
        self.logtopicUID = logtopicUID
        self.status = None

    def setStatus(self, status):
        """
        :param status: (Optional) 日志订阅状态，0表示未创建，1表示刚创建，2表示开启，3表示关闭
        """
        self.status = status
