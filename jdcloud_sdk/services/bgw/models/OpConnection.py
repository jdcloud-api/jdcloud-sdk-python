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


class OpConnection(object):

    def __init__(self, connectionId=None, connectionName=None, location=None, partner=None, type=None, bandwidthMbps=None, orderId=None, vifIds=None, connectionStatus=None, description=None, createdTime=None, idcAddress=None, contactName=None, phoneNumber=None, rejectedReason=None, connectionOwner=None, charge=None):
        """
        :param connectionId: (Optional) Connection的Id
        :param connectionName: (Optional) 专线的名称, 只允许输入中文、数字、大小写字母、英文下划线“_”及中划线“-”，不允许为空且不超过32字符。
        :param location: (Optional) 自助专线开通的地域信息；只有自助专线才有location信息
        :param partner: (Optional) 专线服务商的信息;只在type为jcloud_partner时有合作伙伴信息详情
        :param type: (Optional) 类型, jcloud_hosted:托管连接; jcloud_partner:合作伙伴连接; jcloud:自助连接。
        :param bandwidthMbps: (Optional) 申请的专线带宽：Mbps
        :param orderId: (Optional) 订单编号
        :param vifIds: (Optional) connection上通道Id列表
        :param connectionStatus: (Optional) 专线的状态，取值为：待审核(Ordering)、待支付(Installation_Paying)、施工中(Pending)、等待确认(Confirming)、可用(Active)、不可用(InActive)、删除中(Deleting)、已删除(Deleted)、审核未通过(Rejected)
        :param description: (Optional) connection的描述, 允许输入UTF-8编码下的全部字符，不超过256字符。
        :param createdTime: (Optional) 专线申请的时间
        :param idcAddress: (Optional) 客户idc地址，取值范围：1~100个字符
        :param contactName: (Optional) 联系人名称，只允许输入中文、数字、大小写字母、英文下划线“_”及中划线“-”，不允许为空且不超过32字符。
        :param phoneNumber: (Optional) 联系人手机号码，11位数字且需要13、14、15、16、17、18、19开头
        :param rejectedReason: (Optional) 审核不通过的原因
        :param connectionOwner: (Optional) 专线所有者的用户pin
        :param charge: (Optional) 计费信息
        """

        self.connectionId = connectionId
        self.connectionName = connectionName
        self.location = location
        self.partner = partner
        self.type = type
        self.bandwidthMbps = bandwidthMbps
        self.orderId = orderId
        self.vifIds = vifIds
        self.connectionStatus = connectionStatus
        self.description = description
        self.createdTime = createdTime
        self.idcAddress = idcAddress
        self.contactName = contactName
        self.phoneNumber = phoneNumber
        self.rejectedReason = rejectedReason
        self.connectionOwner = connectionOwner
        self.charge = charge
