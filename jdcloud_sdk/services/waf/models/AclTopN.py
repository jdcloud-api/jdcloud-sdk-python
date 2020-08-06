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


class AclTopN(object):

    def __init__(self, addr_top10=None, rulename_top10=None):
        """
        :param addr_top10: (Optional) 来源ip的top10
        :param rulename_top10: (Optional) acl规则匹配top10
        """

        self.addr_top10 = addr_top10
        self.rulename_top10 = rulename_top10
