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


class DiskView(object):

    def __init__(self, totalSize=None, usedSize=None, dayIncrease=None, dayRatio=None, message=None):
        """
        :param totalSize: (Optional) 总空间
        :param usedSize: (Optional) 已用空间
        :param dayIncrease: (Optional) 日增空间
        :param dayRatio: (Optional) 空间日增率
        :param message: (Optional) 扣分说明
        """

        self.totalSize = totalSize
        self.usedSize = usedSize
        self.dayIncrease = dayIncrease
        self.dayRatio = dayRatio
        self.message = message
