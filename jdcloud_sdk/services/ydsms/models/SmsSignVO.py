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


class SmsSignVO(object):

    def __init__(self, appId=None, applyStatus=None, createTime=None, pin=None, signContent=None, signId=None, signTypeId=None, status=None, auditorExplanation=None, signPurpose=None, signAttorneyUrl=None, signCertificateUrl=None, signOtherCertificateUrl=None, updateTime=None):
        """
        :param appId: (Optional) 应用id
        :param applyStatus: (Optional) 申请状态，1申请中2拒绝3通过
        :param createTime: (Optional) 创建时间
        :param pin: (Optional) 用户pin
        :param signContent: (Optional) 签名内容
        :param signId: (Optional) 短信签名id
        :param signTypeId: (Optional) 短信签名类型id，调用 listSmsSignTypesUsingGET 接口查询
        :param status: (Optional) 短信签名状态，0未启用 1启用
        :param auditorExplanation: (Optional) 短信签名审核说明
        :param signPurpose: (Optional) 短信签名用途 0自用1他用
        :param signAttorneyUrl: (Optional) 授权委托书下载地址
        :param signCertificateUrl: (Optional) 证明材料下载地址
        :param signOtherCertificateUrl: (Optional) 其他证明材料下载地址
        :param updateTime: (Optional) 
        """

        self.appId = appId
        self.applyStatus = applyStatus
        self.createTime = createTime
        self.pin = pin
        self.signContent = signContent
        self.signId = signId
        self.signTypeId = signTypeId
        self.status = status
        self.auditorExplanation = auditorExplanation
        self.signPurpose = signPurpose
        self.signAttorneyUrl = signAttorneyUrl
        self.signCertificateUrl = signCertificateUrl
        self.signOtherCertificateUrl = signOtherCertificateUrl
        self.updateTime = updateTime
