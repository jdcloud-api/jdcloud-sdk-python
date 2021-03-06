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


class Scene(object):

    def __init__(self, appId, sceneName, sceneType, sceneAvgQps, sceneMaxQps, sceneId=None, sceneSecret=None, appName=None, description=None, createTime=None):
        """
        :param sceneId: (Optional) 场景id,更新时必填
        :param sceneSecret: (Optional) 场景密钥
        :param appId:  所属应用id
        :param appName: (Optional) 所属应用名称
        :param sceneName:  场景名称
        :param sceneType:  场景类型：account：账号场景（登录、注册等）activity：活动场景（秒杀、领券等）content：内容场景（发帖评论、签到投票等）other：其它
        :param sceneAvgQps:  平均qps
        :param sceneMaxQps:  高峰期qps
        :param description: (Optional) 场景描述
        :param createTime: (Optional) 创建时间
        """

        self.sceneId = sceneId
        self.sceneSecret = sceneSecret
        self.appId = appId
        self.appName = appName
        self.sceneName = sceneName
        self.sceneType = sceneType
        self.sceneAvgQps = sceneAvgQps
        self.sceneMaxQps = sceneMaxQps
        self.description = description
        self.createTime = createTime
