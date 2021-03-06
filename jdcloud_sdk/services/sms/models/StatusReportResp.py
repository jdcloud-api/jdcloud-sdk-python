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


class StatusReportResp(object):

    def __init__(self, phoneNum=None, sequenceNumber=None, sendTime=None, reportTime=None, status=None, code=None, splitNum=None):
        """
        :param phoneNum: (Optional) 手机号
        :param sequenceNumber: (Optional) 发送短信的序列号
        :param sendTime: (Optional) 短信发送时间（yyyy-MM-dd HH:mm:ss)
        :param reportTime: (Optional) 接收到回执的时间（yyyy-MM-dd HH:mm:ss)
        :param status: (Optional) 发送状态
        :param code: (Optional) 错误码
        :param splitNum: (Optional) 长短信拆分序号（短短信直接返回1)
        """

        self.phoneNum = phoneNum
        self.sequenceNumber = sequenceNumber
        self.sendTime = sendTime
        self.reportTime = reportTime
        self.status = status
        self.code = code
        self.splitNum = splitNum
