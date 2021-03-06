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


class ConstraintsConf(object):

    def __init__(self, storageType=None, onSale=None, classCode=None, minCount=None, maxCount=None, defaultCount=None, stepCount=None, storageScale=None, minStorageGB=None, maxStorageGB=None, defaultStorageGB=None, stepStorageGB=None):
        """
        :param storageType: (Optional) 磁盘类型，zbs表示SSD云硬盘， local_ssd表示本地SSD盘
        :param onSale: (Optional) 是否在售
        :param classCode: (Optional) 规格代码，规格代码详情参见：https://docs.jdcloud.com/cn/jcs-for-elasticsearch/specifications
        :param minCount: (Optional) 节点数最小值
        :param maxCount: (Optional) 节点数最大值
        :param defaultCount: (Optional) 节点数默认值
        :param stepCount: (Optional) 节点数步长
        :param storageScale: (Optional) 是否包含存储
        :param minStorageGB: (Optional) 存储最小值
        :param maxStorageGB: (Optional) 存储最大值
        :param defaultStorageGB: (Optional) 存储默认值
        :param stepStorageGB: (Optional) 存储步长
        """

        self.storageType = storageType
        self.onSale = onSale
        self.classCode = classCode
        self.minCount = minCount
        self.maxCount = maxCount
        self.defaultCount = defaultCount
        self.stepCount = stepCount
        self.storageScale = storageScale
        self.minStorageGB = minStorageGB
        self.maxStorageGB = maxStorageGB
        self.defaultStorageGB = defaultStorageGB
        self.stepStorageGB = stepStorageGB
