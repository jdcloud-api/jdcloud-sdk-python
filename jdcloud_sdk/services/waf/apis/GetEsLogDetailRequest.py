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


class GetEsLogDetailRequest(JDCloudRequest):
    """
    获取网站在一定时间内的日志详情。
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(GetEsLogDetailRequest, self).__init__(
            '/regions/{regionId}/chart:getEsLog', 'GET', header, version)
        self.parameters = parameters


class GetEsLogDetailParameters(object):

    def __init__(self,regionId, start, end, pageSize, pageIndex):
        """
        :param regionId: 实例所属的地域ID
        :param start: 开始时间戳，单位秒，时间间隔要求大于5分钟，小于30天。
        :param end: 结束时间戳，单位秒，时间间隔要求大于5分钟，小于30天。
        :param pageSize: 每页显示的个数，默认是10。
        :param pageIndex: 页数，默认是1。
        """

        self.regionId = regionId
        self.wafInstanceId = None
        self.domain = None
        self.remote_addr = None
        self.document_uri = None
        self.url = None
        self.anti_geo = None
        self.request_method = None
        self.action = None
        self.status = None
        self.logType = None
        self.logId = None
        self.request_id = None
        self.start = start
        self.end = end
        self.pageSize = pageSize
        self.pageIndex = pageIndex

    def setWafInstanceId(self, wafInstanceId):
        """
        :param wafInstanceId: (Optional) 实例id，代表要查询的WAF实例，为空时表示当前用户下的所有实例
        """
        self.wafInstanceId = wafInstanceId

    def setDomain(self, domain):
        """
        :param domain: (Optional) 域名，为空时表示当前实例下的所有域名
        """
        self.domain = domain

    def setRemote_addr(self, remote_addr):
        """
        :param remote_addr: (Optional) 来源ip，检索字段
        """
        self.remote_addr = remote_addr

    def setDocument_uri(self, document_uri):
        """
        :param document_uri: (Optional) URI，检索字段
        """
        self.document_uri = document_uri

    def setUrl(self, url):
        """
        :param url: (Optional) url，检索字段
        """
        self.url = url

    def setAnti_geo(self, anti_geo):
        """
        :param anti_geo: (Optional) 来源地域，检索字段
        """
        self.anti_geo = anti_geo

    def setRequest_method(self, request_method):
        """
        :param request_method: (Optional) 请求方法，检索字段
        """
        self.request_method = request_method

    def setAction(self, action):
        """
        :param action: (Optional) 动作，检索字段，支持类型：""(为空时，默认查询全部动作类型)，"-"(放行)，"notice"(观察)，"forbidden OR status"(拦截)，"redirect"(浏览器跳转)，"verify"(人机交互)
        """
        self.action = action

    def setStatus(self, status):
        """
        :param status: (Optional) 状态码，检索字段
        """
        self.status = status

    def setLogType(self, logType):
        """
        :param logType: (Optional) 日志类型，检索字段，支持类型：""(为空时，默认查询全部日志类型)，"access"(访问日志)，"waf"(wafSDK)，"acl"(自定义规则)，"skip"(白名单)，"deny"(黑名单)，"cc"(CC攻击)，"webcache"(网页防篡改)，"css"(跨站脚本攻击)，"sqli"(SQL注入攻击)，""fileinc"(文件读取/包含攻击)，"cmding"(命令/代码执行攻击)，"sdd"(敏感文件探测)，"malscan"(恶意扫描攻击)，"bckack"(恶意/后门文件攻击)，"xmli"(XML注入攻击)，"dirt"(目录遍历攻击)
        """
        self.logType = logType

    def setLogId(self, logId):
        """
        :param logId: (Optional) 日志Id，检索字段
        """
        self.logId = logId

    def setRequest_id(self, request_id):
        """
        :param request_id: (Optional) 请求Id，检索字段
        """
        self.request_id = request_id

