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


class VpcAttachment(object):

    def __init__(self, vpcAttachmentId=None, vpcAttachmentName=None, bgwId=None, vpcId=None, propagateType=None, status=None, propagateCidrInfos=None, createdTime=None):
        """
        :param vpcAttachmentId: (Optional) vpc接口的Id
        :param vpcAttachmentName: (Optional) vpc接口的名称
        :param bgwId: (Optional) vpc接口对应的bgwId
        :param vpcId: (Optional) vpc接口对应的vpcId
        :param propagateType: (Optional) 选择传播网段的方式all，partial，none
        :param status: (Optional) 创建vpc接口的状态:active
        :param propagateCidrInfos: (Optional) Vpc接口传播的网段信息列表
        :param createdTime: (Optional) vpc接口创建的时间
        """

        self.vpcAttachmentId = vpcAttachmentId
        self.vpcAttachmentName = vpcAttachmentName
        self.bgwId = bgwId
        self.vpcId = vpcId
        self.propagateType = propagateType
        self.status = status
        self.propagateCidrInfos = propagateCidrInfos
        self.createdTime = createdTime
