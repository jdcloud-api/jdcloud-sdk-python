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


class Qps(object):

    def __init__(self, qpsTotal=None, wafAnti=None, botAnti=None, ccAnti=None, aclAnti=None, cacheTotal=None):
        """
        :param qpsTotal: (Optional) qps统计数据
        :param wafAnti: (Optional) waf防护统计数据
        :param botAnti: (Optional) bot防护统计数据
        :param ccAnti: (Optional) cc防护统计数据
        :param aclAnti: (Optional) 精准访问控制防护统计数据
        :param cacheTotal: (Optional) 网站合规异常统计数据
        """

        self.qpsTotal = qpsTotal
        self.wafAnti = wafAnti
        self.botAnti = botAnti
        self.ccAnti = ccAnti
        self.aclAnti = aclAnti
        self.cacheTotal = cacheTotal
