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


class Listener(object):

    def __init__(self, listenerId=None, loadBalancerId=None, protocol=None, port=None, algorithm=None, stickySession=None, realIp=None, status=None, name=None, description=None, healthCheck=None, healthCheckTimeout=None, healthCheckInterval=None, healthyThreshold=None, unhealthyThreshold=None, healthCheckIp=None, serverGroupId=None, stickySessionTimeout=None, cookieType=None, healthCheckUri=None, healthCheckHttpCode=None, certificateId=None, headers=None):
        """
        :param listenerId: (Optional) 监听器ID
        :param loadBalancerId: (Optional) 负载均衡ID
        :param protocol: (Optional) 协议
        :param port: (Optional) 端口
        :param algorithm: (Optional) 调度算法
        :param stickySession: (Optional) 会话保持状态，取值on|off
        :param realIp: (Optional) 获取真实ip
        :param status: (Optional) 状态
        :param name: (Optional) 名称
        :param description: (Optional) 描述
        :param healthCheck: (Optional) 健康检查状态，取值on|off
        :param healthCheckTimeout: (Optional) 健康检查响应的最大超时时间，单位s
        :param healthCheckInterval: (Optional) 健康检查响应的最大间隔时间，单位s
        :param healthyThreshold: (Optional) 健康检查结果为success的阈值
        :param unhealthyThreshold: (Optional) 健康检查结果为fail的阈值
        :param healthCheckIp: (Optional) 健康检查ip
        :param serverGroupId: (Optional) 服务器组id
        :param stickySessionTimeout: (Optional) 会话保持超时时间，单位s
        :param cookieType: (Optional) 会话类型，植入Cookie or 重写Cookie
        :param healthCheckUri: (Optional) 检查路径
        :param healthCheckHttpCode: (Optional) 正常态码，要使用的Http状态码
        :param certificateId: (Optional) 证书ID
        :param headers: (Optional) 获取HTTP头字段：X-Forwarded-For、X-Forwarded-Proto、X- Forwarded-Port、X-Forwarded-LBIP
        """

        self.listenerId = listenerId
        self.loadBalancerId = loadBalancerId
        self.protocol = protocol
        self.port = port
        self.algorithm = algorithm
        self.stickySession = stickySession
        self.realIp = realIp
        self.status = status
        self.name = name
        self.description = description
        self.healthCheck = healthCheck
        self.healthCheckTimeout = healthCheckTimeout
        self.healthCheckInterval = healthCheckInterval
        self.healthyThreshold = healthyThreshold
        self.unhealthyThreshold = unhealthyThreshold
        self.healthCheckIp = healthCheckIp
        self.serverGroupId = serverGroupId
        self.stickySessionTimeout = stickySessionTimeout
        self.cookieType = cookieType
        self.healthCheckUri = healthCheckUri
        self.healthCheckHttpCode = healthCheckHttpCode
        self.certificateId = certificateId
        self.headers = headers
