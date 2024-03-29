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


class GetEvidenceResp(object):

    def __init__(self, evidenceId=None, messageId=None, evidenceMessageId=None, evidenceFileList=None):
        """
        :param evidenceId: (Optional) 存证编号
        :param messageId: (Optional) 取证请求流水号（单证据链存证用户无需关心）
        :param evidenceMessageId: (Optional) 存证请求的流水号（单证据链存证用户无需关心）
        :param evidenceFileList: (Optional) 取证结果文件
        """

        self.evidenceId = evidenceId
        self.messageId = messageId
        self.evidenceMessageId = evidenceMessageId
        self.evidenceFileList = evidenceFileList
