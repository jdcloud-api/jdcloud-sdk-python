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


class SubmitTranscodeJobRequestInfo(object):

    def __init__(self, accessKey, secretKey, endpoint, bucket, objectKey, templateIds, outputConfig, title=None):
        """
        :param accessKey:  输入对象存储 accessKey，必须参数
        :param secretKey:  输入对象存储 accessKey，必须参数
        :param endpoint:  输入对象存储 endpoint。必须参数，内网域名，如 s3-internal.cn-north-1.jcloudcs.com
        :param bucket:  输入对象存储 bucket，必须参数
        :param objectKey:  输入对象存储 objectKey，必须参数
        :param title: (Optional) 输入视频标题，可选参数，默认会从 objectKey 中截取
        :param templateIds:  转码模板ID集合，必须参数，非空集合
        :param outputConfig:  输出配置，必须参数
        """

        self.accessKey = accessKey
        self.secretKey = secretKey
        self.endpoint = endpoint
        self.bucket = bucket
        self.objectKey = objectKey
        self.title = title
        self.templateIds = templateIds
        self.outputConfig = outputConfig
