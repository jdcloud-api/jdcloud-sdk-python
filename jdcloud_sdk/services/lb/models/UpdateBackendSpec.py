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


class UpdateBackendSpec(object):

    def __init__(self, backendName=None, healthCheckSpec=None, algorithm=None, targetGroupIds=None, agIds=None, proxyProtocol=None, description=None, sessionStickiness=None, sessionStickyTimeout=None, connectionDrainingSeconds=None, httpCookieExpireSeconds=None, httpForwardedProtocol=None, httpForwardedPort=None, httpForwardedHost=None, httpForwardedVip=None, closeHealthCheck=None):
        """
        :param backendName: (Optional) 后端服务名称,只允许输入中文、数字、大小写字母、英文下划线“_”及中划线“-”，不允许为空且不超过32字符
        :param healthCheckSpec: (Optional) 健康检查信息
        :param algorithm: (Optional) 调度算法 <br>【alb,nlb】取值范围为[IpHash, RoundRobin, LeastConn]（含义分别为：加权源Ip哈希，加权轮询和加权最小连接） <br>【dnlb】取值范围为[IpHash, QuintupleHash]（含义分别为：加权源Ip哈希和加权五元组哈希）
        :param targetGroupIds: (Optional) 虚拟服务器组的Id列表，目前只支持一个，且与agIds不能同时存在
        :param agIds: (Optional) 高可用组的Id列表，目前只支持一个，且与targetGroupIds不能同时存在
        :param proxyProtocol: (Optional) 【alb Tcp协议】是否启用Proxy ProtocolV1协议获取真实源ip, 取值为false(不开启)或者true(开启), 默认为false
        :param description: (Optional) 描述,允许输入UTF-8编码下的全部字符，不超过256字符
        :param sessionStickiness: (Optional) 会话保持, 取值为false(不开启)或者true(开启)，默认为false <br>【alb Http协议，RoundRobin算法】支持基于cookie的会话保持 <br>【nlb】支持基于报文源目的IP的会话保持
        :param sessionStickyTimeout: (Optional) 【nlb】会话保持超时时间，sessionStickiness开启时生效, 取值范围[1-3600]
        :param connectionDrainingSeconds: (Optional) 【nlb】连接耗尽超时，移除target前，连接的最大保持时间，默认300s，取值范围[0-3600]
        :param httpCookieExpireSeconds: (Optional) 【alb Http协议】cookie的过期时间,sessionStickiness开启时生效，取值范围为[0-86400], 0表示cookie与浏览器同生命周期
        :param httpForwardedProtocol: (Optional) 【alb Http协议】获取负载均衡的协议, 取值为False(不获取)或True(获取)
        :param httpForwardedPort: (Optional) 【alb Http协议】获取负载均衡的端口, 取值为False(不获取)或True(获取)
        :param httpForwardedHost: (Optional) 【alb Http协议】获取负载均衡的host信息, 取值为False(不获取)或True(获取)
        :param httpForwardedVip: (Optional) 【alb Http协议】获取负载均衡的vip, 取值为False(不获取)或True(获取)
        :param closeHealthCheck: (Optional) 【alb,dnlb】关闭健康检查，取值为false(不关闭)或true(关闭)
        """

        self.backendName = backendName
        self.healthCheckSpec = healthCheckSpec
        self.algorithm = algorithm
        self.targetGroupIds = targetGroupIds
        self.agIds = agIds
        self.proxyProtocol = proxyProtocol
        self.description = description
        self.sessionStickiness = sessionStickiness
        self.sessionStickyTimeout = sessionStickyTimeout
        self.connectionDrainingSeconds = connectionDrainingSeconds
        self.httpCookieExpireSeconds = httpCookieExpireSeconds
        self.httpForwardedProtocol = httpForwardedProtocol
        self.httpForwardedPort = httpForwardedPort
        self.httpForwardedHost = httpForwardedHost
        self.httpForwardedVip = httpForwardedVip
        self.closeHealthCheck = closeHealthCheck
