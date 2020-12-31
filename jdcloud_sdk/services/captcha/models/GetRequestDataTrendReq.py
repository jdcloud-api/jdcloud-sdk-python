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


class GetRequestDataTrendReq(object):

    def __init__(self, start, end, requestType=None, appIds=None, sceneIds=None):
        """
        :param start:  开始时间戳，单位毫秒，时间间隔要求大于5分钟，小于30天
        :param end:  结束时间戳，单位毫秒，时间间隔要求大于5分钟，小于30天
        :param requestType: (Optional) 查询QPS的类型，默认all, 可选: all(总体请求量趋势), silent(静默验证请求量趋势), captcha(验证码请求量趋势)
        :param appIds: (Optional) 应用id
        :param sceneIds: (Optional) 场景id
        """

        self.start = start
        self.end = end
        self.requestType = requestType
        self.appIds = appIds
        self.sceneIds = sceneIds
