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


class CreateImageRequest(JDCloudRequest):
    """
    为云主机创建私有镜像。云主机状态必须为<b>stopped</b>。<br>
云主机没有正在进行中的任务才可制作镜像。<br>
如果云主机中挂载了数据盘，默认会将数据盘创建快照，生成打包镜像。<br>
调用接口后，需要等待镜像状态变为<b>ready</b>后，才能正常使用镜像。

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(CreateImageRequest, self).__init__(
            '/regions/{regionId}/instances/{instanceId}:createImage', 'POST', header, version)
        self.parameters = parameters


class CreateImageParameters(object):

    def __init__(self, regionId, instanceId, name, description, ):
        """
        :param regionId: 地域ID
        :param instanceId: 云主机ID
        :param name: 镜像名称，<a href="https://www.jdcloud.com/help/detail/3870/isCatalog/1">参考公共参数规范</a>。
        :param description: 镜像描述，<a href="https://www.jdcloud.com/help/detail/3870/isCatalog/1">参考公共参数规范</a>。
        """

        self.regionId = regionId
        self.instanceId = instanceId
        self.name = name
        self.description = description
        self.dataDisks = None

    def setDataDisks(self, dataDisks):
        """
        :param dataDisks: (Optional) 数据盘列表，可以在打包镜像的基础上，额外增加新的快照、空盘、或排除云主机中的数据盘。
        """
        self.dataDisks = dataDisks

