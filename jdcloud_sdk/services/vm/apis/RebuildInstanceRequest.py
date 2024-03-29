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


class RebuildInstanceRequest(JDCloudRequest):
    """
    
重置云主机系统。

需要注意的是，重装系统会导致系统盘的内容全部丢失，数据盘的数据不受影响（但需要重新识别）。因此，在需要保留系统运行数据的情况下，强烈建议您在重置系统前制作私有镜像，之后重置时选择该私有镜像即可实现保留系统运行数据。

详细操作说明请参考帮助文档：[重置系统](https://docs.jdcloud.com/cn/virtual-machines/rebuild-instance)

## 接口说明
- 云主机的状态必须为 `stopped` 状态。
- 若实例基于私有镜像创建，而私有镜像已被删除，则无法使用原镜像重置系统，即无法恢复至刚创建时的系统状态，建议保留被实例引用的私有镜像。
- 重置系统需要重新指定密码，对于 `Linux` 系统您还可以重新指定 `SSH密钥`。
- 对于云盘作系统盘的实例，当前系统盘大小不能超过目标镜像对应系统盘快照的容量。
- 云主机系统盘类型必须与待更换镜像支持的系统盘类型保持一致，若当前云主机系统盘为 `local` 类型，则更换镜像的系统盘类型必须为 `loaclDisk` 类型；同理，若当前云主机系统盘为 `cloud` 类型，则更换镜像的系统盘类型必须为 `cloudDisk` 类型。可查询 [DescribeImages](https://docs.jdcloud.com/virtual-machines/api/describeimages) 接口获得指定地域的镜像信息。
- 指定的镜像必须能够支持当前主机的实例规格 `instanceType`，否则会返回错误。可查询 [DescribeImageConstraints](docs.jdcloud.com/virtual-machines/api/describeimageconstraints) 接口获得指定镜像支持的系统盘类型信息。

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(RebuildInstanceRequest, self).__init__(
            '/regions/{regionId}/instances/{instanceId}:rebuildInstance', 'POST', header, version)
        self.parameters = parameters


class RebuildInstanceParameters(object):

    def __init__(self,regionId, instanceId, ):
        """
        :param regionId: 地域ID。
        :param instanceId: 云主机ID。
        """

        self.regionId = regionId
        self.instanceId = instanceId
        self.password = None
        self.imageId = None
        self.keyNames = None
        self.hostname = None
        self.metadata = None
        self.userdata = None
        self.passWordAuth = None
        self.imageInherit = None

    def setPassword(self, password):
        """
        :param password: (Optional) 实例密码。
可用于SSH登录和VNC登录。
长度为8\~30个字符，必须同时包含大、小写英文字母、数字和特殊符号中的三类字符。特殊符号包括：`\(\)\`~!@#$%^&\*\_-+=\|{}\[ ]:";'<>,.?/，`。
更多密码输入要求请参见 [公共参数规范](https://docs.jdcloud.com/virtual-machines/api/general_parameters)。

        """
        self.password = password

    def setImageId(self, imageId):
        """
        :param imageId: (Optional) 镜像ID。
若不指定镜像ID，默认使用当前主机的原镜像重置系统。
可查询 [DescribeImages](https://docs.jdcloud.com/virtual-machines/api/describeimages) 接口获得指定地域的镜像信息。

        """
        self.imageId = imageId

    def setKeyNames(self, keyNames):
        """
        :param keyNames: (Optional) 密钥对名称。仅Linux系统下该参数生效，当前仅支持输入单个密钥。

        """
        self.keyNames = keyNames

    def setHostname(self, hostname):
        """
        :param hostname: (Optional) 实例hostname。
若不指定hostname，则默认以实例名称`name`作为hostname，但是会以RFC 952和RFC 1123命名规范做一定转义。
**Windows系统**：长度为2\~15个字符，允许大小写字母、数字或连字符（-），不能以连字符（-）开头或结尾，不能连续使用连字符（-），也不能全部使用数字。不支持点号（.）。
**Linux系统**：长度为2-64个字符，允许支持多个点号，点之间为一段，每段允许使用大小写字母、数字或连字符（-），但不能连续使用点号（.）或连字符（-），不能以点号（.）或连字符（-）开头或结尾。

        """
        self.hostname = hostname

    def setMetadata(self, metadata):
        """
        :param metadata: (Optional) 用户自定义元数据。
以 `key-value` 键值对形式指定，可在实例系统内通过元数据服务查询获取。最多支持40对键值对，且 `key` 不超过256字符，`value` 不超过16KB，不区分大小写。
注意：`key` 不要以连字符(-)结尾，否则此 `key` 不生效。

        """
        self.metadata = metadata

    def setUserdata(self, userdata):
        """
        :param userdata: (Optional) 自定义脚本。
目前仅支持启动脚本，即 `launch-script`，须Base64编码且编码前数据长度不能超过16KB。
**linux系统**：支持bash和python，编码前须分别以 `#!/bin/bash` 和 `#!/usr/bin/env python` 作为内容首行。
**Windows系统**：支持 `bat` 和 `powershell`，编码前须分别以 `<cmd></cmd>和<powershell></powershell>` 作为内容首、尾行。

        """
        self.userdata = userdata

    def setPassWordAuth(self, passWordAuth):
        """
        :param passWordAuth: (Optional) 密码授权，若存在密匙，则根据此参数决定是否使用密码，若没有密匙，此参数无效，会强制使用密码。
若不使用密码，且密匙对解绑后，用户需重置密码，方可使用密码登录。
此参数在windows系统中必须为yes。

        """
        self.passWordAuth = passWordAuth

    def setImageInherit(self, imageInherit):
        """
        :param imageInherit: (Optional) 继承镜像中的登录验证方式，"yes"为使用，"no"为不使用，""默认为"no"
        """
        self.imageInherit = imageInherit

