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

from jdcloud_sdk.core.jdcloudrequest import JDCloudRequest


class DescribeLiveStreamTranslateConfigRequest(JDCloudRequest):
    """
    查询翻译模板配置
- 翻译模板配置按照 域名,应用,流 3级配置添加,以最小的粒度配置生效原则
- 域名、应用、流 依次粒度递减 即: 域名>应用>流
- 该查询旨在查询域名、应用、流最终生效的翻译模板配置,并非各级的模板绑定情况

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeLiveStreamTranslateConfigRequest, self).__init__(
            '/translates:config', 'GET', header, version)
        self.parameters = parameters


class DescribeLiveStreamTranslateConfigParameters(object):

    def __init__(self, ):
        """
        """

        self.pageNum = None
        self.pageSize = None
        self.filters = None

    def setPageNum(self, pageNum):
        """
        :param pageNum: (Optional) 页码
- 取值范围 [1, 100000]

        """
        self.pageNum = pageNum

    def setPageSize(self, pageSize):
        """
        :param pageSize: (Optional) 分页大小
- 取值范围[10, 100]

        """
        self.pageSize = pageSize

    def setFilters(self, filters):
        """
        :param filters: (Optional) 模板配置查询过滤条件:
  - name:   publishDomain 必填(推流域名)
  - value:  参数
  - name:   appName 必填(应用名称)
  - value:  参数
  - name:   streamName 非必填(流名称)
  - value:  参数

        """
        self.filters = filters
