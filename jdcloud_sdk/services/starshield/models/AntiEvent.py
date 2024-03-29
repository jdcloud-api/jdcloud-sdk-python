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


class AntiEvent(object):

    def __init__(self, remoteAddr=None, csaInfo=None, riskLevel=None, area=None, accessTime=None, method=None, attackType=None, url=None, payLoad=None, action=None, ruleName=None, logId=None, isReported=None, wafInstanceId=None, status=None, upstreamErr=None, skipExist=None, denyExist=None, antiReqRaw=None):
        """
        :param remoteAddr: (Optional) 源ip
        :param csaInfo: (Optional) 情报标签
        :param riskLevel: (Optional) 风险等级
        :param area: (Optional) 来源地区
        :param accessTime: (Optional) 产生时间
        :param method: (Optional) 方法
        :param attackType: (Optional) 攻击类型
        :param url: (Optional) url
        :param payLoad: (Optional) 恶意负载
        :param action: (Optional) 动作
        :param ruleName: (Optional) 规则名称
        :param logId: (Optional) 日志Id
        :param isReported: (Optional) 该信息是否已上报AI平台，0表示否
        :param wafInstanceId: (Optional) 实例id
        :param status: (Optional) 状态码
        :param upstreamErr: (Optional) 状态标识
        :param skipExist: (Optional) 是否已加入白名单，0表示否
        :param denyExist: (Optional) 是否已加入黑名单，0表示否
        :param antiReqRaw: (Optional) 攻击详情
        """

        self.remoteAddr = remoteAddr
        self.csaInfo = csaInfo
        self.riskLevel = riskLevel
        self.area = area
        self.accessTime = accessTime
        self.method = method
        self.attackType = attackType
        self.url = url
        self.payLoad = payLoad
        self.action = action
        self.ruleName = ruleName
        self.logId = logId
        self.isReported = isReported
        self.wafInstanceId = wafInstanceId
        self.status = status
        self.upstreamErr = upstreamErr
        self.skipExist = skipExist
        self.denyExist = denyExist
        self.antiReqRaw = antiReqRaw
