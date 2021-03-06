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


class AuditRange(object):

    def __init__(self, pass=None, review=None, block=None):
        """
        :param pass: (Optional) 正常数据是否入审，true-入审，false-不入审，缺省为 false
        :param review: (Optional) 疑似数据是否入审，true-入审，false-不入审，缺省为 false
        :param block: (Optional) 确认违规数据是否入审，true-入审，false-不入审，缺省为 false
        """

        self.pass = pass
        self.review = review
        self.block = block
