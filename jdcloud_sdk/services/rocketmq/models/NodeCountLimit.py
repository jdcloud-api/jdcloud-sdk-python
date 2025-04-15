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


class NodeCountLimit(object):

    def __init__(self, availableCount=None, minCount=None, defaultCount=None, stepCount=None):
        """
        :param availableCount: (Optional) 节点个数最大值
        :param minCount: (Optional) 节点个数最小值
        :param defaultCount: (Optional) 节点个数默认值
        :param stepCount: (Optional) 节点个数步长
        """

        self.availableCount = availableCount
        self.minCount = minCount
        self.defaultCount = defaultCount
        self.stepCount = stepCount
