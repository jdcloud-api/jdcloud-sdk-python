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


class AlarmDimension(object):

    def __init__(self, id=None, categoryId=None, dimension=None, dimensionNameCH=None, dimensionNameEN=None, tagServiceCode=None, webCode=None, dashboard=None, hasSubNode=None, groupCodes=None, tags=None, column=None, dir=None, number=None, size=None):
        """
        :param id: (Optional) 自增id
        :param categoryId: (Optional) 类型id
        :param dimension: (Optional) 代码
        :param dimensionNameCH: (Optional) 中文名称
        :param dimensionNameEN: (Optional) 英文名称
        :param tagServiceCode: (Optional) 标签服务处注册的serviceCode
        :param webCode: (Optional) 前端控制台链接的serviceCode
        :param dashboard: (Optional) dashboard是否可用
        :param hasSubNode: (Optional) 是否有子节点，一般认为，当下方配置的tags不为空时，即有子节点
        :param groupCodes: (Optional) 当有维度时，此处可空，无时需要设置
        :param tags: (Optional) 除资源tag外，其他需要重点关注的tag，当报警规则运行时，会附加该tag去查询数据，当有维度(dimension)时，此处可空
        :param column: (Optional) 排序字段
        :param dir: (Optional) 排序方式
        :param number: (Optional) 页码
        :param size: (Optional) 查询条数
        """

        self.id = id
        self.categoryId = categoryId
        self.dimension = dimension
        self.dimensionNameCH = dimensionNameCH
        self.dimensionNameEN = dimensionNameEN
        self.tagServiceCode = tagServiceCode
        self.webCode = webCode
        self.dashboard = dashboard
        self.hasSubNode = hasSubNode
        self.groupCodes = groupCodes
        self.tags = tags
        self.column = column
        self.dir = dir
        self.number = number
        self.size = size