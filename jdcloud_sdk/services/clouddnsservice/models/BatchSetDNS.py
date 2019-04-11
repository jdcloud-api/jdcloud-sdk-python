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


class BatchSetDNS(object):

    def __init__(self, domainId, hostRecord, hostValue, id, ttl, type, viewValue, jcloudRes=None, mxPriority=None, port=None, weight=None):
        """
        :param domainId:  解析记录对应的主域名的ID。一次请求里面应该是相同的domainId。请使用getDomains接口获取。
        :param hostRecord:  主机记录
        :param hostValue:  解析记录的值
        :param id:  解析记录的ID, 如果是新增请填0，如果是更新，请使用searchRR接口查询解析记录ID。
        :param jcloudRes: (Optional) 是否是京东云资源
        :param mxPriority: (Optional) 优先级，只存在于MX, SRV解析记录类型
        :param port: (Optional) 端口，只存在于SRV解析记录类型
        :param ttl:  解析记录的生存时间
        :param type:  解析的类型，请参考<a href="https://docs.jdcloud.com/cn/jd-cloud-dns/detailed-interpretation-of-parsed-records">解析记录类型详解</a>
        :param weight: (Optional) 解析记录的权重，目前支持权重的有：A/AAAA/CNAME/JNAME。
        :param viewValue:  解析线路的ID，请调用getViewTree接口获取基础解析线路的ID，使用getUserView接口获取自定义线路的ID。
        """

        self.domainId = domainId
        self.hostRecord = hostRecord
        self.hostValue = hostValue
        self.id = id
        self.jcloudRes = jcloudRes
        self.mxPriority = mxPriority
        self.port = port
        self.ttl = ttl
        self.type = type
        self.weight = weight
        self.viewValue = viewValue
