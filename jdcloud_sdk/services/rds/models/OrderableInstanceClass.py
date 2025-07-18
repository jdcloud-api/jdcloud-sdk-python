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


class OrderableInstanceClass(object):

    def __init__(self, instanceClass=None, instanCluster=None, cpu=None, memoryMB=None, instanceStorageFieldType=None, instanceStorageGB=None, priceCode=None):
        """
        :param instanceClass: (Optional) 可售卖的实例规格代码
        :param instanCluster: (Optional) 实例规格族，可能的参数值：S1：标准型，C1：内存优化型
        :param cpu: (Optional) cpu核数
        :param memoryMB: (Optional) 内存大小
        :param instanceStorageFieldType: (Optional) 存储空间可取值类型；0：表示列表；1：表示区间
        :param instanceStorageGB: (Optional) 磁盘，单位GB
        :param priceCode: (Optional) 实例规格价格code
        """

        self.instanceClass = instanceClass
        self.instanCluster = instanCluster
        self.cpu = cpu
        self.memoryMB = memoryMB
        self.instanceStorageFieldType = instanceStorageFieldType
        self.instanceStorageGB = instanceStorageGB
        self.priceCode = priceCode
