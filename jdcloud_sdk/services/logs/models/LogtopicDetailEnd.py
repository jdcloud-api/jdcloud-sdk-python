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


class LogtopicDetailEnd(object):

    def __init__(self, collectInfo=None, uID=None, appCode=None, appName=None, collectInfoUID=None, createTime=None, description=None, inOrder=None, lastRecordTime=None, lifeCycle=None, logsetName=None, logsetUID=None, name=None, prePattern=None, region=None, serviceCode=None, tags=None):
        """
        :param collectInfo: (Optional) 
        :param uID: (Optional) UID
        :param appCode: (Optional) 日志来源,只在查询单个日志主题并且创建了采集配置时返回值
        :param appName: (Optional) 日志主题采集的日志类型
        :param collectInfoUID: (Optional) 采集配置UID
        :param createTime: (Optional) 创建时间
        :param description: (Optional) 描述信息
        :param inOrder: (Optional) 保序标识
        :param lastRecordTime: (Optional) 最新日志上报时间
        :param lifeCycle: (Optional) 生命周期
        :param logsetName: (Optional) 所属日志集名称
        :param logsetUID: (Optional) 所属日志集
        :param name: (Optional) 日志主题名称
        :param prePattern: (Optional) 预处理模式
        :param region: (Optional) 地域信息
        :param serviceCode: (Optional) 产品线serviceCode
        :param tags: (Optional) 标签列表
        """

        self.collectInfo = collectInfo
        self.uID = uID
        self.appCode = appCode
        self.appName = appName
        self.collectInfoUID = collectInfoUID
        self.createTime = createTime
        self.description = description
        self.inOrder = inOrder
        self.lastRecordTime = lastRecordTime
        self.lifeCycle = lifeCycle
        self.logsetName = logsetName
        self.logsetUID = logsetUID
        self.name = name
        self.prePattern = prePattern
        self.region = region
        self.serviceCode = serviceCode
        self.tags = tags
