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


class UserReportLogVo(object):

    def __init__(self, id=None, pin=None, updateTime=None, operator=None, remark=None):
        """
        :param id: (Optional) id
        :param pin: (Optional) pin
        :param updateTime: (Optional) 历史版本
        :param operator: (Optional) 操作人
        :param remark: (Optional) 备注
        """

        self.id = id
        self.pin = pin
        self.updateTime = updateTime
        self.operator = operator
        self.remark = remark
