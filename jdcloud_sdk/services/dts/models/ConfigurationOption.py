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


class ConfigurationOption(object):

    def __init__(self, taskOption=None, transmissionMode=None, options=None, transmissionObjectOption=None, customOptions=None):
        """
        :param taskOption: (Optional) 任务配置属性（废弃）
        :param transmissionMode: (Optional) 数据传输初始化类型
        :param options: (Optional) 任务设置项
        :param transmissionObjectOption: (Optional) 传输对象配置支持的属性
        :param customOptions: (Optional) 任务自定义设置项
        """

        self.taskOption = taskOption
        self.transmissionMode = transmissionMode
        self.options = options
        self.transmissionObjectOption = transmissionObjectOption
        self.customOptions = customOptions
