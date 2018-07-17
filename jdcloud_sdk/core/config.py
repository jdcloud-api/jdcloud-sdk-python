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

from jdcloud_sdk.core.const import SCHEME_HTTPS


class Config(object):

    def __init__(self, endpoint='www.jdcloud-api.com', scheme=SCHEME_HTTPS, timeout=10):
        self.endpoint = endpoint
        self.scheme = scheme
        self.timeout = timeout

    def __getitem__(self, key):
        return getattr(self, key)
