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


class DeleteSecretRequest(JDCloudRequest):
    """
    删除单个 secret

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DeleteSecretRequest, self).__init__(
            '/regions/{regionId}/secrets/{name}', 'DELETE', header, version)
        self.parameters = parameters


class DeleteSecretParameters(object):

    def __init__(self,regionId, name):
        """
        :param regionId: Region ID
        :param name: Secret Name
        """

        self.regionId = regionId
        self.name = name

