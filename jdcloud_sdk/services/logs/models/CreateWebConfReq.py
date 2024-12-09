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


class CreateWebConfReq(object):

    def __init__(self, confType, data, logsetUID=None, logtopicUID=None, region=None):
        """
        :param confType:  ConfType 配置类型，前端自定义
        :param data:  Data 配置内容
        :param logsetUID: (Optional) LogsetUID 日志集维度。如果要控制该配置文件在日志集级别生效，则传LogsetUID，不传LogtopicUID
        :param logtopicUID: (Optional) LogtopicUID 日志主题维度。如果要控制该配置文件在日志主题级别生效，则传LogtopicUID，不传LogsetUID
        :param region: (Optional) Region 地域维度. 如果要控制该配置文件在地域级别生效，则传入该参数。
        """

        self.confType = confType
        self.data = data
        self.logsetUID = logsetUID
        self.logtopicUID = logtopicUID
        self.region = region
