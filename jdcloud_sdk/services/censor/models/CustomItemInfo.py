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


class CustomItemInfo(object):

    def __init__(self, libId=None, itemId=None, resourceType=None, content=None, updateTime=None):
        """
        :param libId: (Optional) 敏感库id
        :param itemId: (Optional) 敏感库itemId
        :param resourceType: (Optional) 文件类型，text-文本，image-图片，audio-音频，video-视频
        :param content: (Optional) 敏感库Item的具体内容
        :param updateTime: (Optional) 更新时间
        """

        self.libId = libId
        self.itemId = itemId
        self.resourceType = resourceType
        self.content = content
        self.updateTime = updateTime
