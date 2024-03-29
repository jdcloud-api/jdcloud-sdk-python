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


class IpbanUsrConf(object):

    def __init__(self, enable=None, ipbanTime=None, detectTime=None, threshold=None, action=None):
        """
        :param enable: (Optional) 是否使能 0表示否
        :param ipbanTime: (Optional) 封禁时间，秒
        :param detectTime: (Optional) 检测时间，秒
        :param threshold: (Optional) 封禁阈值
        :param action: (Optional) 动作配置
        """

        self.enable = enable
        self.ipbanTime = ipbanTime
        self.detectTime = detectTime
        self.threshold = threshold
        self.action = action
