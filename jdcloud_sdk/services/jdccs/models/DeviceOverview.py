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


class DeviceOverview(object):

    def __init__(self, sum=None, server=None, network=None, storage=None, other=None, opened=None, launched=None, operating=None, modifying=None, canceling=None):
        """
        :param sum: (Optional) 设备总数目
        :param server: (Optional) 服务器总数目
        :param network: (Optional) 网络设备总数目
        :param storage: (Optional) 存储设备总数目
        :param other: (Optional) 其它设备总数目
        :param opened: (Optional) 已开通
        :param launched: (Optional) 已上架
        :param operating: (Optional) 操作中
        :param modifying: (Optional) 变更中
        :param canceling: (Optional) 退订中
        """

        self.sum = sum
        self.server = server
        self.network = network
        self.storage = storage
        self.other = other
        self.opened = opened
        self.launched = launched
        self.operating = operating
        self.modifying = modifying
        self.canceling = canceling
