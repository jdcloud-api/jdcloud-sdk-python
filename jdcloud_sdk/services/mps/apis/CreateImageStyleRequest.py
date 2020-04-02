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


class CreateImageStyleRequest(JDCloudRequest):
    """
    添加图片样式
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(CreateImageStyleRequest, self).__init__(
            '/regions/{regionId}/buckets/{bucketName}/imageStyles', 'POST', header, version)
        self.parameters = parameters


class CreateImageStyleParameters(object):

    def __init__(self, regionId, bucketName, ):
        """
        :param regionId: 区域ID
        :param bucketName: Bucket名称
        """

        self.regionId = regionId
        self.bucketName = bucketName
        self.id = None
        self.userId = None
        self.styleName = None
        self.params = None
        self.paramAlias = None
        self.regionId = None
        self.bucketName = None
        self.status = None
        self.modifyTime = None
        self.createdTime = None

    def setId(self, id):
        """
        :param id: (Optional) 图片样式id(readOnly)
        """
        self.id = id

    def setUserId(self, userId):
        """
        :param userId: (Optional) 用户id(readOnly)
        """
        self.userId = userId

    def setStyleName(self, styleName):
        """
        :param styleName: (Optional) 图片样式名称
        """
        self.styleName = styleName

    def setParams(self, params):
        """
        :param params: (Optional) 图片样式参数
        """
        self.params = params

    def setParamAlias(self, paramAlias):
        """
        :param paramAlias: (Optional) 图片样式参数别名
        """
        self.paramAlias = paramAlias

    def setRegionId(self, regionId):
        """
        :param regionId: (Optional) 所属区域(readOnly)
        """
        self.regionId = regionId

    def setBucketName(self, bucketName):
        """
        :param bucketName: (Optional) 所属Bucket(readOnly)
        """
        self.bucketName = bucketName

    def setStatus(self, status):
        """
        :param status: (Optional) 图片样式状态(readOnly)
        """
        self.status = status

    def setModifyTime(self, modifyTime):
        """
        :param modifyTime: (Optional) 修改时间(readOnly)
        """
        self.modifyTime = modifyTime

    def setCreatedTime(self, createdTime):
        """
        :param createdTime: (Optional) 创建时间(readOnly)
        """
        self.createdTime = createdTime
