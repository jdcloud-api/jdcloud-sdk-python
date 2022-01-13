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


class WebRule(object):

    def __init__(self, id=None, instanceId=None, domain=None, cname=None, cnameStatus=None, serviceIp=None, serviceIpConfig=None, protocol=None, customPortStatus=None, port=None, httpsPort=None, httpOrigin=None, status=None, originType=None, originAddr=None, originDomain=None, onlineAddr=None, httpCertStatus=None, certId=None, certName=None, httpsCertContent=None, httpsRsaKey=None, bindCerts=None, forceJump=None, algorithm=None, ccStatus=None, webSocketStatus=None, blackListEnable=None, whiteListEnable=None, geoRsRoute=None, enableKeepalive=None, httpVersion=None, sslProtocols=None, suiteLevel=None, userSuiteLevel=None, jsFingerprintEnable=None, jsFingerprintScope=None, ccCustomStatus=None, enableHealthCheck=None, proxyConnectTimeout=None, enableUnderscores=None):
        """
        :param id: (Optional) 规则 Id
        :param instanceId: (Optional) 实例 Id
        :param domain: (Optional) 子域名
        :param cname: (Optional) 规则的 CNAME
        :param cnameStatus: (Optional) CNAME 解析状态, 0: 解析异常, 1: 解析正常
        :param serviceIp: (Optional) 该规则使用中的高防 IP
        :param serviceIpConfig: (Optional) 已配置的高防 IP 列表
        :param protocol: (Optional) 
        :param customPortStatus: (Optional) 是否为自定义端口号, 0: 为默认, 1: 为自定义
        :param port: (Optional) HTTP 协议的端口号, 如 80,81
        :param httpsPort: (Optional) HTTPS 协议的端口号, 如 443,8443
        :param httpOrigin: (Optional) 是否开启 HTTP 回源, 0: 为不开启, 1: 为开启, 当勾选 HTTPS 时可以配置该属性
        :param status: (Optional) 0: 防御状态, 1: 回源状态
        :param originType: (Optional) 回源类型: A 或者 CNAME
        :param originAddr: (Optional) 回源域名, originType 为 A 时返回该字段
        :param originDomain: (Optional) 回源域名, originType 为 CNAME 时返回该字段
        :param onlineAddr: (Optional) 备用的回源地址列表, 为一个域名或者多个 IP 地址
        :param httpCertStatus: (Optional) 证书状态. <br>- 0: 异常<br>- 1: 正常<br>- 2: 证书未上传
        :param certId: (Optional) 证书 Id, (废弃, 绑定证书信息通过 certs 字段查看)
        :param certName: (Optional) 证书名称, (废弃, 绑定证书信息通过 certs 字段查看)
        :param httpsCertContent: (Optional) 证书内容, (废弃, 绑定证书信息通过 certs 字段查看)
        :param httpsRsaKey: (Optional) 证书私钥, (废弃, 绑定证书信息通过 certs 字段查看)
        :param bindCerts: (Optional) 网站规则绑定证书信息
        :param forceJump: (Optional) 是否开启 HTTPS 强制跳转, 当 protocol 为 HTTP_HTTPS 时可以配置该属性<br>- 0: 不强跳<br>- 1: 开启强跳
        :param algorithm: (Optional) 转发规则. <br>- wrr: 带权重的轮询<br>- rr:  不带权重的轮询<br>- sh:  源地址hash
        :param ccStatus: (Optional) CC 状态, 0: CC 关闭, 1: CC 开启
        :param webSocketStatus: (Optional) webSocket 状态, 0: 关闭, 1: 开启
        :param blackListEnable: (Optional) 黑名单状态, 0: 关闭, 1: 开启
        :param whiteListEnable: (Optional) 白名单状态, 0: 关闭, 1: 开启
        :param geoRsRoute: (Optional) 按区域分流回源配置
        :param enableKeepalive: (Optional) 是否开启回源长连接, protocol 选项开启 https 时生效, 可取值<br>- on: 开启<br>- off: 关闭
        :param httpVersion: (Optional) http 版本, protocol 选项开启 https 时生效, 可取值 http1 或 http2
        :param sslProtocols: (Optional) SSL协议类型, protocol 选项开启 https 时生效, 可取值SSLv2,SSLv3,TLSv1.0,TLSv1.1,TLSv1.2
        :param suiteLevel: (Optional) 加密套件等级, protocol 选项开启 https 时生效, 可取值<br>- low: 低级<br>- middle: 中级<br>- high：高级<br>- custom：自定义
        :param userSuiteLevel: (Optional) 自定义加密套件等级, suiteLevel 为 custom 是有效
        :param jsFingerprintEnable: (Optional) 是否允许在 response 中插入 JS, 0: 关闭, 1: 开启
        :param jsFingerprintScope: (Optional) JS 指纹生效范围, 0: 所有页面, 1: 已配置的自定义页面
        :param ccCustomStatus: (Optional) CC自定义规则总开关, 0: 关闭, 1: 开启
        :param enableHealthCheck: (Optional) 健康检查开关, 0: 关闭, 1: 开启
        :param proxyConnectTimeout: (Optional) 回源连接超时时长, 单位 秒
        :param enableUnderscores: (Optional) 请求头支持下划线, 0: 关闭, 1: 开启
        """

        self.id = id
        self.instanceId = instanceId
        self.domain = domain
        self.cname = cname
        self.cnameStatus = cnameStatus
        self.serviceIp = serviceIp
        self.serviceIpConfig = serviceIpConfig
        self.protocol = protocol
        self.customPortStatus = customPortStatus
        self.port = port
        self.httpsPort = httpsPort
        self.httpOrigin = httpOrigin
        self.status = status
        self.originType = originType
        self.originAddr = originAddr
        self.originDomain = originDomain
        self.onlineAddr = onlineAddr
        self.httpCertStatus = httpCertStatus
        self.certId = certId
        self.certName = certName
        self.httpsCertContent = httpsCertContent
        self.httpsRsaKey = httpsRsaKey
        self.bindCerts = bindCerts
        self.forceJump = forceJump
        self.algorithm = algorithm
        self.ccStatus = ccStatus
        self.webSocketStatus = webSocketStatus
        self.blackListEnable = blackListEnable
        self.whiteListEnable = whiteListEnable
        self.geoRsRoute = geoRsRoute
        self.enableKeepalive = enableKeepalive
        self.httpVersion = httpVersion
        self.sslProtocols = sslProtocols
        self.suiteLevel = suiteLevel
        self.userSuiteLevel = userSuiteLevel
        self.jsFingerprintEnable = jsFingerprintEnable
        self.jsFingerprintScope = jsFingerprintScope
        self.ccCustomStatus = ccCustomStatus
        self.enableHealthCheck = enableHealthCheck
        self.proxyConnectTimeout = proxyConnectTimeout
        self.enableUnderscores = enableUnderscores
