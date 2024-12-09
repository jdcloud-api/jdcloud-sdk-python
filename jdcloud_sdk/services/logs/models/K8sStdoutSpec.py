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


class K8sStdoutSpec(object):

    def __init__(self, nameSpaceSelectorSpec, selectorType, container=None, labelSelectorSpec=None, workLoads=None):
        """
        :param container: (Optional) container为空表所有的，不为空采集指定的容器
        :param labelSelectorSpec: (Optional) 
        :param nameSpaceSelectorSpec:  
        :param selectorType:  选择器类型。Enum<string>: allContainers, workload, labels
        :param workLoads: (Optional) 工作负载信息。注意：此字段可能返回 null，表示取不到有效值。
        """

        self.container = container
        self.labelSelectorSpec = labelSelectorSpec
        self.nameSpaceSelectorSpec = nameSpaceSelectorSpec
        self.selectorType = selectorType
        self.workLoads = workLoads
