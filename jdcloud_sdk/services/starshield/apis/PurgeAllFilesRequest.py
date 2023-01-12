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


class PurgeAllFilesRequest(JDCloudRequest):
    """
    从星盾的缓存中删除所有文件
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(PurgeAllFilesRequest, self).__init__(
            '/zones/{identifier}/purge_cache__purgeAllFiles', 'POST', header, version)
        self.parameters = parameters


class PurgeAllFilesParameters(object):

    def __init__(self,identifier, purge_everything):
        """
        :param identifier: 
        :param purge_everything: 指示星盾缓存中的所有资源都应该删除的标志。
注意，执行此操作后，可能会对源服务器负载产生显著影响。

        """

        self.identifier = identifier
        self.purge_everything = purge_everything

