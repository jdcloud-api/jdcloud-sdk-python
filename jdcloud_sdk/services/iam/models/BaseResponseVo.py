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


class BaseResponseVo(object):

    def __init__(self, isSuccess=None, message=None, errorCode=None, data=None, errStrSet=None, requestId=None):
        """
        :param isSuccess: (Optional) 
        :param message: (Optional) 
        :param errorCode: (Optional) 
        :param data: (Optional) 
        :param errStrSet: (Optional) 
        :param requestId: (Optional) 
        """

        self.isSuccess = isSuccess
        self.message = message
        self.errorCode = errorCode
        self.data = data
        self.errStrSet = errStrSet
        self.requestId = requestId
