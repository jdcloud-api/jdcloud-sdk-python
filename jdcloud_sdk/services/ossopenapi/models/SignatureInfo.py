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


class SignatureInfo(object):

    def __init__(self, endpoint, httpMethod, resourcePath, xAmzContentSha256, additionalSignatureHeaders=None, signatureParameters=None):
        """
        :param endpoint:  签名的endpoint, 例如 http://s3.cn-east-1.jcloudcs.com
        :param httpMethod:  http method
        :param resourcePath:  资源路径,不包含query string
        :param xAmzContentSha256:  上传文件的sha256
        :param additionalSignatureHeaders: (Optional) 附加的签名header
        :param signatureParameters: (Optional) 签名的参数，query string
        """

        self.endpoint = endpoint
        self.httpMethod = httpMethod
        self.resourcePath = resourcePath
        self.xAmzContentSha256 = xAmzContentSha256
        self.additionalSignatureHeaders = additionalSignatureHeaders
        self.signatureParameters = signatureParameters
