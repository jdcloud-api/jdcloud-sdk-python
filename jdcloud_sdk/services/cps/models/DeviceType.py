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


class DeviceType(object):

    def __init__(self, nameEN=None, nameZH=None, useTypeEN=None, useTypeZH=None, region=None, cpuConcise=None, cpuDetail=None, memConcise=None, memDetail=None, ifConcise=None, ifDetail=None, systemDiskConcise=None, systemDiskDetail=None, dataDiskConcise=None, dataDiskDetail=None, gpuConcise=None, gpuDetail=None):
        """
        :param nameEN: (Optional) 服务器类型英文名称, 如 cps.c.normal
        :param nameZH: (Optional) 服务器类型中文名称, 如 计算型
        :param useTypeEN: (Optional) 使用场景类型英文描述, 如 standard
        :param useTypeZH: (Optional) 使用场景类型中文描述, 如 标准型
        :param region: (Optional) 区域代码, 如 cn-east-1
        :param cpuConcise: (Optional) CPU概要描述
        :param cpuDetail: (Optional) CPU详细信息
        :param memConcise: (Optional) 内存概要信息
        :param memDetail: (Optional) 内存详细信息
        :param ifConcise: (Optional) 网口概要信息
        :param ifDetail: (Optional) 网口详细信息
        :param systemDiskConcise: (Optional) 系统磁盘概要信息
        :param systemDiskDetail: (Optional) 系统磁盘详细信息
        :param dataDiskConcise: (Optional) 系统磁盘概要信息
        :param dataDiskDetail: (Optional) 系统磁盘详细信息
        :param gpuConcise: (Optional) GPU概要信息
        :param gpuDetail: (Optional) GPU详细信息
        """

        self.nameEN = nameEN
        self.nameZH = nameZH
        self.useTypeEN = useTypeEN
        self.useTypeZH = useTypeZH
        self.region = region
        self.cpuConcise = cpuConcise
        self.cpuDetail = cpuDetail
        self.memConcise = memConcise
        self.memDetail = memDetail
        self.ifConcise = ifConcise
        self.ifDetail = ifDetail
        self.systemDiskConcise = systemDiskConcise
        self.systemDiskDetail = systemDiskDetail
        self.dataDiskConcise = dataDiskConcise
        self.dataDiskDetail = dataDiskDetail
        self.gpuConcise = gpuConcise
        self.gpuDetail = gpuDetail
