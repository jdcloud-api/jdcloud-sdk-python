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


class Overrides(object):

    def __init__(self, action=None, enabled=None, categories=None, rules=None):
        """
        :param action: (Optional) 规则集操作。
针对Managed Ruleset来说，有效值是managed_challenge（托管质询）/block（阻止）/js_challenge（JS质询）/log（记录）/challenge（交互式质询）/（默认）。
针对OWASP Ruleset来说，有效值是managed_challenge（托管质询）/block（阻止）/js_challenge（JS质询）/log（记录）/challenge（交互式质询）。

        :param enabled: (Optional) 规则集状态。
针对Managed Ruleset来说，有效值是true（已启用）/false（已禁用）/（默认）。
针对OWASP Ruleset来说，没有该字段。

        :param categories: (Optional) 
        :param rules: (Optional) 
        """

        self.action = action
        self.enabled = enabled
        self.categories = categories
        self.rules = rules
