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


class ScanConf(object):

    def __init__(self, enable, scense=None, frozen=None, threshold=None, fileType=None, fileSuffix=None):
        """
        :param enable:  0-不开启检测，1-开启检测
        :param scense: (Optional) 检测场景，audio-语音违规-视频支持，porn-涉黄-图片视频支持，terrorism-涉政暴恐-图片视频支持，antispam-反垃圾-文本语音支持，enable为1时必须
        :param frozen: (Optional) 0-不开启自动冻结，1-开启自动冻结
        :param threshold: (Optional) 自动冻结阈值
        :param fileType: (Optional) 检测类型，all-全部
        :param fileSuffix: (Optional) 文件后缀，all-表示全部
        """

        self.enable = enable
        self.scense = scense
        self.frozen = frozen
        self.threshold = threshold
        self.fileType = fileType
        self.fileSuffix = fileSuffix
