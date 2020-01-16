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


class DescribeTemplateSpec(object):

    def __init__(self, filters=None, pageNumber=None, pageSize=None, templateType=None):
        """
        :param filters: (Optional) 模板uid列表或数据源类型
templateUids-模板uids，精确匹配，支持多个;
datasourceType-数据源类型，精确匹配，支持多个（云监控:cloudmonitor，hawkeye:hawkeye，deeplog:deeplog）
        :param pageNumber: (Optional) 当前所在页，默认为1
in: query
        :param pageSize: (Optional) 页面大小，默认为20；取值范围[1, 100]
in: query
        :param templateType: (Optional) 模板类型，0表示系统、1表示自定义，默认为0
        """

        self.filters = filters
        self.pageNumber = pageNumber
        self.pageSize = pageSize
        self.templateType = templateType