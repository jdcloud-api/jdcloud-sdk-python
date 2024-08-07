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


class CoProductVo(object):

    def __init__(self, cooperationId=None, productName=None, companyName=None, name=None, contractInfos=None, productType=None, productTypeName=None, productMode=None, productModeName=None, broker=None, settlementMode=None, settlementModeName=None, settlementCyle=None, settlementCyleName=None, productStatus=None, productStatusName=None, cooperationCompanys=None):
        """
        :param cooperationId: (Optional) 合作id
        :param productName: (Optional) 合作产品名称
        :param companyName: (Optional) 合作公司名称
        :param name: (Optional) 合作名称
        :param contractInfos: (Optional) 合同信息列表
        :param productType: (Optional) 产品类型
        :param productTypeName: (Optional) 产品类型名称
        :param productMode: (Optional) 产品模式
        :param productModeName: (Optional) 产品模式显示名称
        :param broker: (Optional) 合作对接人(原合作BD)
        :param settlementMode: (Optional) 结算方式 1固定金额结算，2实际售价固定比例结算，3实际售价浮动比例结算
        :param settlementModeName: (Optional) 结算方式显示名称
        :param settlementCyle: (Optional) 结算周期 1周结后付款、2月结后付款、3季结后付款、4年结后付款，5 PO预付款
        :param settlementCyleName: (Optional) 结算周期显示名称
        :param productStatus: (Optional) 产品状态  1联合开发中；2实施部署中；3测试验证中；4可商用售卖；5可PO下单；6需重新采购；7合作暂停
        :param productStatusName: (Optional) 产品状态显示名称
        :param cooperationCompanys: (Optional) 合作公司
        """

        self.cooperationId = cooperationId
        self.productName = productName
        self.companyName = companyName
        self.name = name
        self.contractInfos = contractInfos
        self.productType = productType
        self.productTypeName = productTypeName
        self.productMode = productMode
        self.productModeName = productModeName
        self.broker = broker
        self.settlementMode = settlementMode
        self.settlementModeName = settlementModeName
        self.settlementCyle = settlementCyle
        self.settlementCyleName = settlementCyleName
        self.productStatus = productStatus
        self.productStatusName = productStatusName
        self.cooperationCompanys = cooperationCompanys
