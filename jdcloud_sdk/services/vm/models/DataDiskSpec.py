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


class DataDiskSpec(object):

    def __init__(self, dataDiskSizeGB, imageUrl, diskFormat=None):
        """
        :param diskFormat: (Optional) 镜像数据盘格式，支持vhd、vmdk、qcow2、raw格式，默认为qcow2。
        :param dataDiskSizeGB:  镜像数据盘大小。
        :param imageUrl:  要导入镜像的对象存储外链地址。
        """

        self.diskFormat = diskFormat
        self.dataDiskSizeGB = dataDiskSizeGB
        self.imageUrl = imageUrl
