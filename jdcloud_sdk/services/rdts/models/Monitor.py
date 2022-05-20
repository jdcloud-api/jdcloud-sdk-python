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


class Monitor(object):

    def __init__(self, ops=None, inputKBps=None, maxMemory=None, usedMemory=None):
        """
        :param ops: (Optional) 每秒请求个数
        :param inputKBps: (Optional) 输入流量，单位KBps
        :param maxMemory: (Optional) 源端内存规格（jimdb没有），单位Byte
        :param usedMemory: (Optional) 源端已使用内存（jimdb没有），单位Byte
        """

        self.ops = ops
        self.inputKBps = inputKBps
        self.maxMemory = maxMemory
        self.usedMemory = usedMemory
