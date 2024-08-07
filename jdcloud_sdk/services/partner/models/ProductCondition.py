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


class ProductCondition(object):

    def __init__(self, appCode=None, productType=None, productId=None, productNameLike=None, productStatus=None, salesModel=None, chargeSubject=None, chargeMode=None, salesModelName=None, chargeSubjectName=None, chargeModeName=None, pageIndex=None, pageSize=None, offset=None):
        """
        :param appCode: (Optional) 业务线
        :param productType: (Optional) 产品类型
        :param productId: (Optional) 产品ID
        :param productNameLike: (Optional) 产品名称(模糊查询)
        :param productStatus: (Optional) 状态
        :param salesModel: (Optional) 售卖模式
        :param chargeSubject: (Optional) 收费主体
        :param chargeMode: (Optional) 计费方式
        :param salesModelName: (Optional) 售卖模式
        :param chargeSubjectName: (Optional) 收费主体
        :param chargeModeName: (Optional) 计费方式
        :param pageIndex: (Optional) 当前页序号
        :param pageSize: (Optional) 每页结果数量
        :param offset: (Optional) 
        """

        self.appCode = appCode
        self.productType = productType
        self.productId = productId
        self.productNameLike = productNameLike
        self.productStatus = productStatus
        self.salesModel = salesModel
        self.chargeSubject = chargeSubject
        self.chargeMode = chargeMode
        self.salesModelName = salesModelName
        self.chargeSubjectName = chargeSubjectName
        self.chargeModeName = chargeModeName
        self.pageIndex = pageIndex
        self.pageSize = pageSize
        self.offset = offset
