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


class DownloadCertDesc(object):

    def __init__(self, certId=None, certName=None, keyFile=None, certFile=None, digest=None, caCertFile=None, serverType=None, certEncryptePassword=None, commonName=None):
        """
        :param certId: (Optional) 证书Id
        :param certName: (Optional) 证书名称
        :param keyFile: (Optional) 私钥
        :param certFile: (Optional) 证书
        :param digest: (Optional) 对私钥文件使用sha256算法计算的摘要信息
        :param caCertFile: (Optional) 中间证书
        :param serverType: (Optional) 证书应用服务器类型
        :param certEncryptePassword: (Optional) 证书加密密码
        :param commonName: (Optional) 域名
        """

        self.certId = certId
        self.certName = certName
        self.keyFile = keyFile
        self.certFile = certFile
        self.digest = digest
        self.caCertFile = caCertFile
        self.serverType = serverType
        self.certEncryptePassword = certEncryptePassword
        self.commonName = commonName
