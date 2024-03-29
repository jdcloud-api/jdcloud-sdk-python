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


class DeleteCacheInstanceRequest(JDCloudRequest):
    """
    删除按配置计费、或包年包月已到期的缓存Redis实例，包年包月未到期不可删除。
只有处于运行running或者错误error状态才可以删除，其余状态不可以删除。
白名单用户不能删除包年包月已到期的缓存Redis实例。

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DeleteCacheInstanceRequest, self).__init__(
            '/regions/{regionId}/cacheInstance/{cacheInstanceId}', 'DELETE', header, version)
        self.parameters = parameters


class DeleteCacheInstanceParameters(object):

    def __init__(self,regionId, cacheInstanceId):
        """
        :param regionId: 缓存Redis实例所在区域的Region ID。目前有华北-北京、华南-广州、华东-上海三个区域，Region ID分别为cn-north-1、cn-south-1、cn-east-2
        :param cacheInstanceId: 缓存Redis实例ID，是访问实例的唯一标识
        """

        self.regionId = regionId
        self.cacheInstanceId = cacheInstanceId

