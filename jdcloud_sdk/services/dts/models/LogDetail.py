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


class LogDetail(object):

    def __init__(self, type=None, reason=None, message=None, lastUpdateTime=None, lastTransitionTime=None):
        """
        :param type: (Optional) 日志类型
        :param reason: (Optional) 错误原因
        :param message: (Optional) 错误信息
        :param lastUpdateTime: (Optional) 最后更新时间
        :param lastTransitionTime: (Optional) 最后一次状态变更时间
        """

        self.type = type
        self.reason = reason
        self.message = message
        self.lastUpdateTime = lastUpdateTime
        self.lastTransitionTime = lastTransitionTime