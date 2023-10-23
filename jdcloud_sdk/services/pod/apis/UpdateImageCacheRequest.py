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


class UpdateImageCacheRequest(JDCloudRequest):
    """
    修改镜像缓存的属性。

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(UpdateImageCacheRequest, self).__init__(
            '/regions/{regionId}/imageCache/{imageCacheId}:update', 'PATCH', header, version)
        self.parameters = parameters


class UpdateImageCacheParameters(object):

    def __init__(self,regionId, imageCacheId, ):
        """
        :param regionId: Region ID
        :param imageCacheId: imageCacheId
        """

        self.regionId = regionId
        self.imageCacheId = imageCacheId
        self.name = None
        self.retentionDays = None

    def setName(self, name):
        """
        :param name: (Optional) 新的镜像缓存名称
        """
        self.name = name

    def setRetentionDays(self, retentionDays):
        """
        :param retentionDays: (Optional) 新的保留日期，以创建时间为准计算过期时间，新的过期时间不得为当前时间之前
        """
        self.retentionDays = retentionDays

