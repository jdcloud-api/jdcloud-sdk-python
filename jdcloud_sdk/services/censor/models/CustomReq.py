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


class CustomReq(object):

    def __init__(self, resourceType, name, scenes, suggestion, censorType=None, websiteInstanceId=None, matchType=None, status=None, libId=None, source=None, bizType=None):
        """
        :param censorType: (Optional) 检测类型，api/oss/website,默认api
        :param websiteInstanceId: (Optional) 站点检查实例Id，多个以 , 分割；当censorType为website时，该参数必填
        :param resourceType:  文件类型，text-文本，image-图片，audio-音频，video-视频
        :param matchType: (Optional) 匹配方式，exact:精确匹配，fuzzy:模糊匹配；仅限文本类型,默认exact
        :param name:  敏感库名
        :param scenes:  文本/语音支持 antispam-反垃圾，视频/图片支持 porn-涉黄，terrorism-涉政暴恐，ad-图文广告
        :param suggestion:  pass 白名单，block 黑名单，review 疑似名单
        :param status: (Optional) 状态 1启用，0禁用,默认 1启用
        :param libId: (Optional) 敏感库id，更新时该参数必填
        :param source: (Optional) 敏感库来源：custom自定义，feedback系统库，更新时该参数必填
        :param bizType: (Optional) 机审策略，可以不填，为空时前端显示空即可
        """

        self.censorType = censorType
        self.websiteInstanceId = websiteInstanceId
        self.resourceType = resourceType
        self.matchType = matchType
        self.name = name
        self.scenes = scenes
        self.suggestion = suggestion
        self.status = status
        self.libId = libId
        self.source = source
        self.bizType = bizType
