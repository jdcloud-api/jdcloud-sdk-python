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

from jdcloud_sdk.core.jdcloudrequest import JDCloudRequest


class ModifyNodeNumRequest(JDCloudRequest):
    """
    修改 TiDB 实例中各类节点的数量。如果当前实例无TiFlash和TiCDC节点，那么在增加TiFlash和TiCDC节点数目时，可同时指定其规格。
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(ModifyNodeNumRequest, self).__init__(
            '/regions/{regionId}/instances/{instanceId}:modifyNodeNum', 'POST', header, version)
        self.parameters = parameters


class ModifyNodeNumParameters(object):

    def __init__(self,regionId, instanceId, ):
        """
        :param regionId: 地域代码
        :param instanceId: 实例ID
        """

        self.regionId = regionId
        self.instanceId = instanceId
        self.tidbNodeNum = None
        self.tikvNodeNum = None
        self.pdNodeNum = None
        self.tiflashNodeSpec = None
        self.ticdcNodeSpec = None

    def setTidbNodeNum(self, tidbNodeNum):
        """
        :param tidbNodeNum: (Optional) 调整后的tidb节点数
        """
        self.tidbNodeNum = tidbNodeNum

    def setTikvNodeNum(self, tikvNodeNum):
        """
        :param tikvNodeNum: (Optional) 调整后的tikv节点数
        """
        self.tikvNodeNum = tikvNodeNum

    def setPdNodeNum(self, pdNodeNum):
        """
        :param pdNodeNum: (Optional) 调整后的pd节点数
        """
        self.pdNodeNum = pdNodeNum

    def setTiflashNodeSpec(self, tiflashNodeSpec):
        """
        :param tiflashNodeSpec: (Optional) TiFlash节点规格和数目
        """
        self.tiflashNodeSpec = tiflashNodeSpec

    def setTicdcNodeSpec(self, ticdcNodeSpec):
        """
        :param ticdcNodeSpec: (Optional) Ticdc节点规格和数目
        """
        self.ticdcNodeSpec = ticdcNodeSpec

