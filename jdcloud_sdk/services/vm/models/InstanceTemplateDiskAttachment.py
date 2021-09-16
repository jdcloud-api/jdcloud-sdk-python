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


class InstanceTemplateDiskAttachment(object):

    def __init__(self, diskCategory=None, autoDelete=None, instanceTemplateDisk=None, deviceName=None, noDevice=None):
        """
        :param diskCategory: (Optional) 磁盘类型。
**系统盘**：取值为：`local` 本地系统盘 或 `cloud` 云盘系统盘。
**数据盘**：取值为：`cloud` 云盘数据盘。

        :param autoDelete: (Optional) 是否随实例一起删除，即删除实例时是否自动删除此磁盘。此参数仅对按配置计费的非多点挂载云硬盘生效。
`true`：随实例删除。
`false`：不随实例删除。

        :param instanceTemplateDisk: (Optional) 云硬盘配置。
        :param deviceName: (Optional) 磁盘逻辑挂载点。
**系统盘**：默认为vda。
**数据盘**：取值范围：`[vdb~vdbm]`。

        :param noDevice: (Optional) 排除设备，使用此参数 `noDevice` 配合 `deviceName` 一起使用。
创建镜像的场景下：使用此参数可以排除云主机实例中的云硬盘不参与制作快照。
创建实例模板的场景下：使用此参数可以排除镜像中的数据盘。
创建云主机的场景下：使用此参数可以排除实例模板、或镜像中的数据盘。
示例：如果镜像中除系统盘还包含一块或多块数据盘，期望仅使用镜像中的部分磁盘，可通过此参数忽略部分磁盘配置。此参数须配合 `deviceName` 一起使用。
例：`deviceName=vdb`、`noDevice=true`，则表示在使用镜像创建实例时，忽略数据盘vdb配置，不创建磁盘。

        """

        self.diskCategory = diskCategory
        self.autoDelete = autoDelete
        self.instanceTemplateDisk = instanceTemplateDisk
        self.deviceName = deviceName
        self.noDevice = noDevice
