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


class ExportImageRequest(JDCloudRequest):
    """
    导出镜像，将京东云私有镜像导出至京东云以外环境

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(ExportImageRequest, self).__init__(
            '/regions/{regionId}/images/{imageId}:exportImage', 'POST', header, version)
        self.parameters = parameters


class ExportImageParameters(object):

    def __init__(self, regionId, imageId, roleName, ossUrl, ):
        """
        :param regionId: 地域ID
        :param imageId: 镜像ID
        :param roleName: 用户创建的服务角色名称
        :param ossUrl: 存储导出镜像文件的oss bucket的域名，请填写以 https:// 开头的完整url
        """

        self.regionId = regionId
        self.imageId = imageId
        self.roleName = roleName
        self.ossUrl = ossUrl
        self.ossPrefix = None
        self.clientToken = None

    def setOssPrefix(self, ossPrefix):
        """
        :param ossPrefix: (Optional) 导出镜像文件名前缀，仅支持英文字母和数字，不能超过32个字符
        """
        self.ossPrefix = ossPrefix

    def setClientToken(self, clientToken):
        """
        :param clientToken: (Optional) 用户导出镜像的幂等性保证。每次导出请传入不同的值，如果传值与某次的clientToken相同，则返还同一个请求结果，不能超过64个字符
        """
        self.clientToken = clientToken

