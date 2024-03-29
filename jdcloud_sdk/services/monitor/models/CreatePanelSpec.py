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


class CreatePanelSpec(object):

    def __init__(self, dashboardUid, panelMetrics, panelType, product, dimension=None, panelName=None, panelResources=None, panelTagResources=None, panelTopNum=None, tags=None):
        """
        :param dashboardUid:  该panel所属dashboard的uid
        :param dimension: (Optional) 该panel所属维度
        :param panelMetrics:  该panel包含的metric
        :param panelName: (Optional) 该panel的名字
        :param panelResources: (Optional) 资源id列表,与标签服务互斥,且资源id列表与标签服务列表至少传一个
        :param panelTagResources: (Optional) 标签服务列表,与资源id列表互斥,且资源id列表与标签服务列表至少传一个
        :param panelTopNum: (Optional) topN的数量，图表类型为3(topN表格)时必填
        :param panelType:  该panel的类型，1-折线图(明细);2-折线图(汇总);3-topN表格
        :param product:  该panel所属产品
        :param tags: (Optional) 依据tag过滤(维度)
        """

        self.dashboardUid = dashboardUid
        self.dimension = dimension
        self.panelMetrics = panelMetrics
        self.panelName = panelName
        self.panelResources = panelResources
        self.panelTagResources = panelTagResources
        self.panelTopNum = panelTopNum
        self.panelType = panelType
        self.product = product
        self.tags = tags
