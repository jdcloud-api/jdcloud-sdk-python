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


class Volume(object):

    def __init__(self, name=None, jdcloudDisk=None, cfs=None, configFile=None, emptyDir=None):
        """
        :param name: (Optional) volume名字，在一个Pod唯一。
        :param jdcloudDisk: (Optional) 提供给Pod的cloud disk.
        :param cfs: (Optional) 提供给Pod的CFS.
        :param configFile: (Optional) 提供给Pod的ConfigFile.
        :param emptyDir: (Optional) EmptyDir卷源
        """

        self.name = name
        self.jdcloudDisk = jdcloudDisk
        self.cfs = cfs
        self.configFile = configFile
        self.emptyDir = emptyDir
