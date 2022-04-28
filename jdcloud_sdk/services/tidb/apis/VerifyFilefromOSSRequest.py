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


class VerifyFilefromOSSRequest(JDCloudRequest):
    """
    校验需要导入的备份文件在OSS上是否存在，需要的读取权限是否具备
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(VerifyFilefromOSSRequest, self).__init__(
            '/regions/{regionId}/instances/{instanceId}/migration:verifyFilefromOSS', 'POST', header, version)
        self.parameters = parameters


class VerifyFilefromOSSParameters(object):

    def __init__(self, regionId,instanceId,ossLink):
        """
        :param regionId: 地域代码
        :param instanceId: 实例ID
        :param ossLink: 要校验的文件bucket及路径,例如Bucket为db_bak,文件路径为test_server/db1/20181013.bak,则ossLink为db_bak/test_server/db1/20181013.bak
        """

        self.regionId = regionId
        self.instanceId = instanceId
        self.ossLink = ossLink

