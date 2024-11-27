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


class ImageCharge(object):

    def __init__(self, chargeInfo=None, chargeConfig=None):
        """
        :param chargeInfo: (Optional) 云主机使用镜像的计费配置。
        :param chargeConfig: (Optional) 云主机使用镜像的计费信息。
        """

        self.chargeInfo = chargeInfo
        self.chargeConfig = chargeConfig
