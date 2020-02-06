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


class DebugApi(object):

    def __init__(self, host, uri, method, authType, region, reqBodyType, assessKey=None, secretKey=None, queryString=None, body=None, editableReqBodyType=None, headerString=None):
        """
        :param assessKey: (Optional) assessKey：京东云用户、API调用者、订阅密钥key
        :param secretKey: (Optional) secretKey：京东云用户、API调用者
        :param host:  请求host
        :param uri:  请求uri,分组路径前缀+API请求路径，如：/todo/api/v1/creatApi
        :param method:  请求方式
        :param authType:  访问授权方式：None（免鉴权）,jd_cloud（京东云用户），jd_apikms（API调用者），jd_subscription_key（订阅密钥）
        :param region:  api所属region
        :param queryString: (Optional) query参数，用&分隔，如：id=1&version=v1
        :param body: (Optional) body参数，传json字符串的base64编码，例如body的值为：{"title":"desk","desc":"cheap"}，应传值为："eyJ0aXRsZSI6ImRlc2siLCJkZXNjIjoiY2hlYXAifQ=="
        :param reqBodyType:  请求格式类型,1:application/json,2:text/xml,3:其他
        :param editableReqBodyType: (Optional) 请求格式类型,当reqBodyType等于3时,使用该请求格式类型
        :param headerString: (Optional) header参数，传json字符串
        """

        self.assessKey = assessKey
        self.secretKey = secretKey
        self.host = host
        self.uri = uri
        self.method = method
        self.authType = authType
        self.region = region
        self.queryString = queryString
        self.body = body
        self.reqBodyType = reqBodyType
        self.editableReqBodyType = editableReqBodyType
        self.headerString = headerString
