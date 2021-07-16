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


class ResourceRefundReq(object):

    def __init__(self, resourceId, refundType=None, refundChannel=None, refundWay=None, refundReason=None, refundReasonOther=None, refundArea=None):
        """
        :param refundType: (Optional) 退款类型 1-订单(资源)退款 2-充值单退款 3-线下退款（人工退款）4-出货失败退款
        :param resourceId:  资源id
        :param refundChannel: (Optional) 退款渠道 1 原支付方式返回  2 退款至余额
        :param refundWay: (Optional) 退款方式   1-退款退货 2-退款不退货
        :param refundReason: (Optional) 退款原因 0-产品不好用/不想要 1-产品功能无法满足需求 2-产品操作体验差 3-服务体验差 4-其他
        :param refundReasonOther: (Optional) 其他退款原因
        :param refundArea: (Optional) 退款范围： 1-仅退现金  2-全部退款（含代金券）
        """

        self.refundType = refundType
        self.resourceId = resourceId
        self.refundChannel = refundChannel
        self.refundWay = refundWay
        self.refundReason = refundReason
        self.refundReasonOther = refundReasonOther
        self.refundArea = refundArea
