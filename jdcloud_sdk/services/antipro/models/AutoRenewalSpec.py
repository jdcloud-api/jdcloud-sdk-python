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


class AutoRenewalSpec(object):

    def __init__(self, autoRenewalEnable, timeSpan=None, timeUnit=None):
        """
        :param autoRenewalEnable:  是否开通自动续费, true: 开通自动续费, false: 不开通自动续费
        :param timeSpan: (Optional) 购买防护包时长, 开通自动续费时必传. <br>- timeUnit 为 3 时, 可取值 1-9<br>- timeUnit 为 4 时, 可取值 1-3
        :param timeUnit: (Optional) 自动续费时长类型, 开通自动续费时必传. <br>- 3: 月<br>- 4: 年
        """

        self.autoRenewalEnable = autoRenewalEnable
        self.timeSpan = timeSpan
        self.timeUnit = timeUnit
