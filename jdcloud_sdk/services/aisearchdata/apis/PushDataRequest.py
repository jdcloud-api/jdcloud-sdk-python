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


class PushDataRequest(JDCloudRequest):
    """
    推送爬取数据
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(PushDataRequest, self).__init__(
            '/pushData', 'POST', header, version)
        self.parameters = parameters


class PushDataParameters(object):

    def __init__(self,title, url, ):
        """
        :param title: 标题
        :param url: 链接
        """

        self.crawlerId = None
        self.taskId = None
        self.title = title
        self.url = url
        self.content = None
        self.publish_time = None
        self.category = None
        self.language = None
        self.author = None
        self.location = None

    def setCrawlerId(self, crawlerId):
        """
        :param crawlerId: (Optional) 爬虫id
        """
        self.crawlerId = crawlerId

    def setTaskId(self, taskId):
        """
        :param taskId: (Optional) 任务id
        """
        self.taskId = taskId

    def setContent(self, content):
        """
        :param content: (Optional) 提取内容
        """
        self.content = content

    def setPublish_time(self, publish_time):
        """
        :param publish_time: (Optional) 发布时间
        """
        self.publish_time = publish_time

    def setCategory(self, category):
        """
        :param category: (Optional) 分类 (分类长度不能超过64个字符)
        """
        self.category = category

    def setLanguage(self, language):
        """
        :param language: (Optional) 语言 (语言长度不能超过16个字符)
        """
        self.language = language

    def setAuthor(self, author):
        """
        :param author: (Optional) 作者
        """
        self.author = author

    def setLocation(self, location):
        """
        :param location: (Optional) 位置
        """
        self.location = location

