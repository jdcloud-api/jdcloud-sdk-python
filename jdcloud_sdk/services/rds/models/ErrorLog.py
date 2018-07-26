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


class ErrorLog(object):

    def __init__(self, name=None, sizeByte=None, lastUpdateTime=None, uploadTime=None, publicURL=None, internalURL=None):
        """
        :param name: (Optional) 错误日志名称
        :param sizeByte: (Optional) 错误日志大小，单位Byte
        :param lastUpdateTime: (Optional) 错误日志最后更新时间，格式为：YYYY-MM-DD HH:mm:ss
        :param uploadTime: (Optional) 错误日志上传时间，格式为：YYYY-MM-DD HH:mm:ss
        :param publicURL: (Optional) 公网下载链接
        :param internalURL: (Optional) 内网下载链接
        """

        self.name = name
        self.sizeByte = sizeByte
        self.lastUpdateTime = lastUpdateTime
        self.uploadTime = uploadTime
        self.publicURL = publicURL
        self.internalURL = internalURL