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


class Pagination(object):

    def __init__(self, currPageNo=None, numberPages=None, numberRecords=None, pageSize=None, startIndex=None):
        """
        :param currPageNo: (Optional) 当前页(默认:1)
        :param numberPages: (Optional) 总页数
        :param numberRecords: (Optional) 总记录数
        :param pageSize: (Optional) 每页记录数(默认每页:10)
        :param startIndex: (Optional) 起始页
        """

        self.currPageNo = currPageNo
        self.numberPages = numberPages
        self.numberRecords = numberRecords
        self.pageSize = pageSize
        self.startIndex = startIndex