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


class SearchLogContextSpec(object):

    def __init__(self, anchor, id, lineSize, time, direction=None):
        """
        :param anchor:  查询anchor,基于该值偏移进行上下文检索
        :param direction: (Optional) 搜索方向,默认both,可取值:up,down,both
        :param id:  日志记录ID
        :param lineSize:  查看上下文行数大小，最大支持200
        :param time:  查询日志时返回的时间戳
        """

        self.anchor = anchor
        self.direction = direction
        self.id = id
        self.lineSize = lineSize
        self.time = time
