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


class DatasourceDetail(object):

    def __init__(self, datasourceId=None, isDefault=None, name=None, opentsdbExtend=None, orgId=None, pluginType=None, url=None):
        """
        :param datasourceId: (Optional) 数据源id
        :param isDefault: (Optional) 是否是默认数据源
        :param name: (Optional) 数据源名称
        :param opentsdbExtend: (Optional) 
        :param orgId: (Optional) orgId
        :param pluginType: (Optional) 插件类型
        :param url: (Optional) 数据源地址
        """

        self.datasourceId = datasourceId
        self.isDefault = isDefault
        self.name = name
        self.opentsdbExtend = opentsdbExtend
        self.orgId = orgId
        self.pluginType = pluginType
        self.url = url
