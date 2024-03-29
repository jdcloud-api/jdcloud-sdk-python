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


class BriefInstanceNetworkInterfaceAttachment(object):

    def __init__(self, deviceIndex=None, autoDelete=None):
        """
        :param deviceIndex: (Optional) 网卡设备Index。创建实例时此参数无须指定且指定无效。
对于主网卡默认Index为1，辅助网卡自动分配。

        :param autoDelete: (Optional) 是否随实例关联删除。
        """

        self.deviceIndex = deviceIndex
        self.autoDelete = autoDelete
