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


class GetChartReq(object):

    def __init__(self, start, end, wafInstanceId=None, domain=None, isSum=None):
        """
        :param wafInstanceId: (Optional) 实例id，代表要查询的WAF实例，为空时表示当前用户下的所有实例
        :param domain: (Optional) 域名，为空时表示当前实例下的所有域名
        :param start:  开始时间戳，单位毫秒，时间间隔要求大于5分钟，小于30天。
        :param end:  结束时间戳，单位毫秒，时间间隔要求大于5分钟，小于30天。
        :param isSum: (Optional) true表示和值图，false表示均值图，仅getBpsData， getQpsData时有效。
        """

        self.wafInstanceId = wafInstanceId
        self.domain = domain
        self.start = start
        self.end = end
        self.isSum = isSum
