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


class EdgeAppList(object):

    def __init__(self, appName=None, appType=None, appDesc=None, appDisplayName=None, appVersion=None, releaseTime=None, appStatus=None, appSource=None, dsDesc=None):
        """
        :param appName: (Optional) App名称
        :param appType: (Optional) App类型 0-deviceService，1-app
        :param appDesc: (Optional) App描述
        :param appDisplayName: (Optional) App显示名称
        :param appVersion: (Optional) APP版本号
        :param releaseTime: (Optional) 发布日期
        :param appStatus: (Optional) App状态
        :param appSource: (Optional) 发布方 0-iotcore, 1-iothub ，2-第三方
        :param dsDesc: (Optional)  device serivce 的描述
        """

        self.appName = appName
        self.appType = appType
        self.appDesc = appDesc
        self.appDisplayName = appDisplayName
        self.appVersion = appVersion
        self.releaseTime = releaseTime
        self.appStatus = appStatus
        self.appSource = appSource
        self.dsDesc = dsDesc
