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


class Driver(object):

    def __init__(self, gpuDriverId=None, gpuModel=None, osName=None, cudaVersion=None, driverVersion=None):
        """
        :param gpuDriverId: (Optional) GPU驱动id
        :param gpuModel: (Optional) GPU卡型号。
        :param osName: (Optional) 操作系统。
        :param cudaVersion: (Optional) cuda版本。
        :param driverVersion: (Optional) 驱动版本。
        """

        self.gpuDriverId = gpuDriverId
        self.gpuModel = gpuModel
        self.osName = osName
        self.cudaVersion = cudaVersion
        self.driverVersion = driverVersion
