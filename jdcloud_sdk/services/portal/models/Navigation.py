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


class Navigation(object):

    def __init__(self, id=None, name=None, description=None, iconUrl=None, iconClass=None, webUrl=None, url=None, productStatus=None, sort=None, createTime=None, parentId=None, updateTime=None, level=None, label=None, helpUrl=None, selfRun=None, lang=None, extChildren=None):
        """
        :param id: (Optional) 主键id
        :param name: (Optional) 名称
        :param description: (Optional) 描述
        :param iconUrl: (Optional) 图标地址
        :param iconClass: (Optional) ICON 样式
        :param webUrl: (Optional) 链接地址
        :param url: (Optional) url：用于查询产品详情
        :param productStatus: (Optional) 是否为京东云产品；0:是京东云产品；1:不是京东云产品
        :param sort: (Optional) 排序
        :param createTime: (Optional) 修改时间
        :param parentId: (Optional) 父ID
        :param updateTime: (Optional) 修改时间
        :param level: (Optional) 导航层级
        :param label: (Optional) 标签
        :param helpUrl: (Optional) 帮助文档地址
        :param selfRun: (Optional) 自营标签
        :param lang: (Optional) 语言：中文cn；英文en
        :param extChildren: (Optional) 子结构
        """

        self.id = id
        self.name = name
        self.description = description
        self.iconUrl = iconUrl
        self.iconClass = iconClass
        self.webUrl = webUrl
        self.url = url
        self.productStatus = productStatus
        self.sort = sort
        self.createTime = createTime
        self.parentId = parentId
        self.updateTime = updateTime
        self.level = level
        self.label = label
        self.helpUrl = helpUrl
        self.selfRun = selfRun
        self.lang = lang
        self.extChildren = extChildren
