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


class RouteTable(object):

    def __init__(self, routeTableId=None, routeTableName=None, routeTableType=None, associateType=None, description=None, vpcId=None, routeTableRules=None, routePropagations=None, subnetIds=None, azType=None, az=None, createdTime=None):
        """
        :param routeTableId: (Optional) 路由表ID
        :param routeTableName: (Optional) 路由表名称，只允许输入中文、数字、大小写字母、英文下划线“_”及中划线“-”，不允许为空且不超过32字符。
        :param routeTableType: (Optional) 路由表类型，default：默认路由表，custom：自定义路由表
        :param associateType: (Optional) 绑定资源类型，取值：subnet，gateway
        :param description: (Optional) 路由表描述信息，允许输入UTF-8编码下的全部字符，不超过256字符。
        :param vpcId: (Optional) 私有网络ID
        :param routeTableRules: (Optional) 路由表规则信息
        :param routePropagations: (Optional) 路由传播列表
        :param subnetIds: (Optional) 路由表绑定的子网列表
        :param azType: (Optional) 路由表az类型，取值：standard(标准路由表)，edge(边缘路由表)
        :param az: (Optional) 路由表可用区
        :param createdTime: (Optional) 路由表创建时间
        """

        self.routeTableId = routeTableId
        self.routeTableName = routeTableName
        self.routeTableType = routeTableType
        self.associateType = associateType
        self.description = description
        self.vpcId = vpcId
        self.routeTableRules = routeTableRules
        self.routePropagations = routePropagations
        self.subnetIds = subnetIds
        self.azType = azType
        self.az = az
        self.createdTime = createdTime
