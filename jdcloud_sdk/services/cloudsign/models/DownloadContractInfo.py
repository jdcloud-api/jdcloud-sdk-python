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


class DownloadContractInfo(object):

    def __init__(self, contractId=None, contractName=None, contractContent=None, contractDigest=None, createTime=None):
        """
        :param contractId: (Optional) 合同id
        :param contractName: (Optional) 合同名称
        :param contractContent: (Optional) 合同base64
        :param contractDigest: (Optional) 合同hash
        :param createTime: (Optional) 操作时间 格式：yyyy-MM-dd HH:mm:ss
        """

        self.contractId = contractId
        self.contractName = contractName
        self.contractContent = contractContent
        self.contractDigest = contractDigest
        self.createTime = createTime
