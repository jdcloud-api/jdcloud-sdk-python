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


class DescribeBillsCondition(object):

    def __init__(self, pin, startTime, endTime, appCode=None, serviceCode=None, dataSource=None, billingType=None, region=None, resourceIdList=None, pageIndex=None, pageSize=None):
        """
        :param appCode: (Optional) 业务线
        :param serviceCode: (Optional) 产品
        :param dataSource: (Optional) 数据来源：1-统一计费, 2-自计费, 10-物联网, 11-视频云, 12-CDN, 13-PCDN, 14-IDC, 15-通信云
        :param pin:  用户pin
        :param startTime:  开始时间（按出账时间查询，开始结束时间必须在同一个月内）
        :param endTime:  结束时间（按出账时间查询，开始结束时间必须在同一个月内）
        :param billingType: (Optional) 计费类型： 1、按配置 2、按用量 3、包年包月 4、按次（一次性）
        :param region: (Optional) 地域
        :param resourceIdList: (Optional) 资源ID列表
        :param pageIndex: (Optional) 页码,默认为1
        :param pageSize: (Optional) 分页大小
        """

        self.appCode = appCode
        self.serviceCode = serviceCode
        self.dataSource = dataSource
        self.pin = pin
        self.startTime = startTime
        self.endTime = endTime
        self.billingType = billingType
        self.region = region
        self.resourceIdList = resourceIdList
        self.pageIndex = pageIndex
        self.pageSize = pageSize
