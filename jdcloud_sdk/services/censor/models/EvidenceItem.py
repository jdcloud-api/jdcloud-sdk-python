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


class EvidenceItem(object):

    def __init__(self, beginTime=None, endTime=None, type=None, url=None, censorSource=None, labels=None, frontPics=None, backPics=None):
        """
        :param beginTime: (Optional) 证据开始相对时间，单位为毫秒，调用方获取后可自行格式化为可视化时间，如：149000 转换为"00:02:29"
        :param endTime: (Optional) 证据结束相对时间，单位为毫秒，调用方获取后可自行格式化为可视化时间，如：149000 转换为"00:02:29"
        :param type: (Optional) 1：图片，2：视频
        :param url: (Optional) 证据信息
        :param censorSource: (Optional) 审核来源，0：京东人审，1：客户人审，2：京东机审
        :param labels: (Optional) 证据结果数组
        :param frontPics: (Optional) 关联信息-命中前截图信息
        :param backPics: (Optional) 关联信息-命中后截图信息
        """

        self.beginTime = beginTime
        self.endTime = endTime
        self.type = type
        self.url = url
        self.censorSource = censorSource
        self.labels = labels
        self.frontPics = frontPics
        self.backPics = backPics
