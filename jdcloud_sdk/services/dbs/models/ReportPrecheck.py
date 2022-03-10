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


class ReportPrecheck(object):

    def __init__(self, plan, checkItem, success, startTime, endTime, errorMessages=None):
        """
        :param plan:  
        :param checkItem:  预检查任务项
        :param success:  是否成功
        :param errorMessages: (Optional) 错误信息，仅sucess为false时返回
        :param startTime:  
        :param endTime:  
        """

        self.plan = plan
        self.checkItem = checkItem
        self.success = success
        self.errorMessages = errorMessages
        self.startTime = startTime
        self.endTime = endTime
