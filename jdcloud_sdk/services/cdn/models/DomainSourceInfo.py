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


class DomainSourceInfo(object):

    def __init__(self, priority=None, sourceHost=None, domain=None):
        """
        :param priority: (Optional) 优先级（1-10）
        :param sourceHost: (Optional) 自定义回源host，仅中国境内加速域名可配置
        :param domain: (Optional) 回源域名
        """

        self.priority = priority
        self.sourceHost = sourceHost
        self.domain = domain
