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


class AddonConfig(object):

    def __init__(self, name=None, version=None, enabled=None, state=None, params=None, parameters=None, addonDetail=None):
        """
        :param name: (Optional) 组件名称
        :param version: (Optional) 组件版本，非必须，未安装时填充为默认版本号
        :param enabled: (Optional) 组件是否开启
        :param state: (Optional) 组件安装状态 not_installed,installed,installing,uninstalling,error_installed
        :param params: (Optional) 组件的额外参数(deprecated)
        :param parameters: (Optional) 组件的额外参数（新）
        :param addonDetail: (Optional) 可安装的addons
        """

        self.name = name
        self.version = version
        self.enabled = enabled
        self.state = state
        self.params = params
        self.parameters = parameters
        self.addonDetail = addonDetail
