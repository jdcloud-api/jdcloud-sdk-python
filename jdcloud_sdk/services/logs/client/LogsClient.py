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

from jdcloud_sdk.core.jdcloudclient import JDCloudClient
from jdcloud_sdk.core.config import Config


class LogsClient(JDCloudClient):

    def __init__(self, credential, config=None, logger=None):
        if config is None:
            config = Config('logs.jdcloud-api.com')

        super(LogsClient, self).__init__(credential, config, 'logs', '1.2.12', logger)
