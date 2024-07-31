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


class AutoUserReportResVo(object):

    def __init__(self, totalCount=None, successCount=None, failureVos=None):
        """
        :param totalCount: (Optional) 总记录数
        :param successCount: (Optional) 新增成功的个数
        :param failureVos: (Optional) 记录新增失败的实体和原因
        """

        self.totalCount = totalCount
        self.successCount = successCount
        self.failureVos = failureVos
