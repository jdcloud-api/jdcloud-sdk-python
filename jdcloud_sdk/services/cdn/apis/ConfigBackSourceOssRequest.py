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


class ConfigBackSourceOssRequest(JDCloudRequest):
    """
    设置回源OSS鉴权
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(ConfigBackSourceOssRequest, self).__init__(
            '/domain/{domain}/configBackSourceOss', 'POST', header, version)
        self.parameters = parameters


class ConfigBackSourceOssParameters(object):

    def __init__(self,domain, ):
        """
        :param domain: 用户域名
        """

        self.domain = domain
        self.status = None
        self.accessKey = None
        self.secretKey = None
        self.bucket = None
        self.suffix = None
        self.domain2 = None

    def setStatus(self, status):
        """
        :param status: (Optional) on/off，若为on则以下必传参数不可为空[accessKey,secretKey,bucket,domain2],若为off则以下参数均不能有值[accessKey,secretKey,bucket,suffix,domain2]
        """
        self.status = status

    def setAccessKey(self, accessKey):
        """
        :param accessKey: (Optional) status 为on时必填
        """
        self.accessKey = accessKey

    def setSecretKey(self, secretKey):
        """
        :param secretKey: (Optional) status 为on时必填
        """
        self.secretKey = secretKey

    def setBucket(self, bucket):
        """
        :param bucket: (Optional) oss桶名,status 为on时必填
        """
        self.bucket = bucket

    def setSuffix(self, suffix):
        """
        :param suffix: (Optional) oss后缀,status 为on时选填
        """
        self.suffix = suffix

    def setDomain2(self, domain2):
        """
        :param domain2: (Optional) status 为on时必填
        """
        self.domain2 = domain2

