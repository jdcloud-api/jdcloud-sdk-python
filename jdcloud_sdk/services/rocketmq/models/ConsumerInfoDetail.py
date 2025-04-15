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


class ConsumerInfoDetail(object):

    def __init__(self, consumerAddress=None, consumeBeginTime=None, consumeEndTime=None, costTime=None, retryTimes=None, consumerStatus=None):
        """
        :param consumerAddress: (Optional) 消费者客户端地址
        :param consumeBeginTime: (Optional) 消费开始时间
        :param consumeEndTime: (Optional) 消费结束时间
        :param costTime: (Optional) 消费耗时
        :param retryTimes: (Optional) 重试次数
        :param consumerStatus: (Optional) 消费状态
        """

        self.consumerAddress = consumerAddress
        self.consumeBeginTime = consumeBeginTime
        self.consumeEndTime = consumeEndTime
        self.costTime = costTime
        self.retryTimes = retryTimes
        self.consumerStatus = consumerStatus
