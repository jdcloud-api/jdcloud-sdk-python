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


class CreateLogDownloadTaskRequest(JDCloudRequest):
    """
    创建日志下载任务
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(CreateLogDownloadTaskRequest, self).__init__(
            '/regions/{regionId}/logtopics/{logtopicUID}/downloadtask', 'POST', header, version)
        self.parameters = parameters


class CreateLogDownloadTaskParameters(object):

    def __init__(self,regionId, logtopicUID, ):
        """
        :param regionId: 地域 Id
        :param logtopicUID: 日志主题 UID
        """

        self.regionId = regionId
        self.logtopicUID = logtopicUID
        self.name = None
        self.keyword = None
        self.compress = None
        self.format = None
        self.logCount = None
        self.quote = None
        self.fileSort = None
        self.startTimestamp = None
        self.endTimestamp = None

    def setName(self, name):
        """
        :param name: (Optional) Name 任务名
        """
        self.name = name

    def setKeyword(self, keyword):
        """
        :param keyword: (Optional) Keyword 查询关键字
        """
        self.keyword = keyword

    def setCompress(self, compress):
        """
        :param compress: (Optional) Compress 压缩方式：0：不压缩，1：gzip，2：snappy
        """
        self.compress = compress

    def setFormat(self, format):
        """
        :param format: (Optional) Format 文件格式：0: CSV, 1:JSON
        """
        self.format = format

    def setLogCount(self, logCount):
        """
        :param logCount: (Optional) 日志条数
        """
        self.logCount = logCount

    def setQuote(self, quote):
        """
        :param quote: (Optional) Quote quote：0：双引号；1：单引号
        """
        self.quote = quote

    def setFileSort(self, fileSort):
        """
        :param fileSort: (Optional) FileSort 文件排序，0：正序，1：倒序
        """
        self.fileSort = fileSort

    def setStartTimestamp(self, startTimestamp):
        """
        :param startTimestamp: (Optional) StartTimestamp 下载内容开始时间
        """
        self.startTimestamp = startTimestamp

    def setEndTimestamp(self, endTimestamp):
        """
        :param endTimestamp: (Optional) EndTimestamp 下载内容截止时间
        """
        self.endTimestamp = endTimestamp
