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


class InternalCode(object):

    def __init__(self, ossBucketName, ossObjectName, codeCheckSum, codeSize, ):
        """
        :param ossBucketName:  存放函数代码ZIP包的OSS Bucket名称。
        :param ossObjectName:  存放函数代码ZIP包的OSS Object名称。
        :param codeCheckSum:  部署包的 sha256 hash。
        :param codeSize:  代码包大小。
        """

        self.ossBucketName = ossBucketName
        self.ossObjectName = ossObjectName
        self.codeCheckSum = codeCheckSum
        self.codeSize = codeSize
