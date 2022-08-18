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


class ModifyFileSystemAttributeRequest(JDCloudRequest):
    """
    修改文件系统属性(name 和 description 必须要指定一个)
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(ModifyFileSystemAttributeRequest, self).__init__(
            '/regions/{regionId}/fileSystems/{fileSystemId}', 'PATCH', header, version)
        self.parameters = parameters


class ModifyFileSystemAttributeParameters(object):

    def __init__(self,regionId, fileSystemId, ):
        """
        :param regionId: 地域ID
        :param fileSystemId: 文件系统ID
        """

        self.regionId = regionId
        self.fileSystemId = fileSystemId
        self.name = None
        self.description = None

    def setName(self, name):
        """
        :param name: (Optional) 文件系统名称(参数规则：不可为空，只支持中文、数字、大小写字母、英文下划线“_”及中划线“-”，且不能超过32字符)
        """
        self.name = name

    def setDescription(self, description):
        """
        :param description: (Optional) 文件系统描述(参数规则：不能超过256字符)
        """
        self.description = description

