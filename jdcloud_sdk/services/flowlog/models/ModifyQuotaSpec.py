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


class ModifyQuotaSpec(object):

    def __init__(self, type, maxLimit, parentResourceId=None):
        """
        :param type:  资源类型，取值范围：flowLog、flowLogResource
        :param parentResourceId: (Optional) type为flowLog不设置
flowLogResource设置为flowLogId

        :param maxLimit:  配额大小
        """

        self.type = type
        self.parentResourceId = parentResourceId
        self.maxLimit = maxLimit
