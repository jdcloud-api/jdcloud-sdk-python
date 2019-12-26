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


class DistributorDTO(object):

    def __init__(self, distributorId=None, distributorName=None, pin=None, contractNo=None, businessLicense=None, legalRepresentative=None, businessLicensePic=None, businessDesc=None, workAddress=None, contracter=None, tel=None, email=None, region=None, settleTime=None, status=None, reason=None, distributorLevel=None, distributorType=None, parentDistributorId=None, bankCompanyName=None, bankCardNo=None, bankBranchName=None, bankBranchNo=None, contractSubject=None, dept=None, returnFlag=None, returnPolicyId=None, distributorProductList=None, circleType=None, returnMode=None, subFlag=None, subReturnFlag=None, subReturnPolicyId=None, subCircleType=None, subReturnMode=None, erp=None):
        """
        :param distributorId: (Optional) 渠道商ID
        :param distributorName: (Optional) 渠道商名称
        :param pin: (Optional) pin
        :param contractNo: (Optional) 合同编号
        :param businessLicense: (Optional) 营业执照号
        :param legalRepresentative: (Optional) 法定代表人
        :param businessLicensePic: (Optional) 营业执照图片
        :param businessDesc: (Optional) 主营业务描述
        :param workAddress: (Optional) 办公地址
        :param contracter: (Optional) 联系人姓名
        :param tel: (Optional) 联系人电话
        :param email: (Optional) 邮箱
        :param region: (Optional) 所属地域
        :param settleTime: (Optional) 入驻日期(一级渠道商手工录入、二级渠道商审批通过日期)
        :param status: (Optional) 状态(0 审批中、2驳回、1 已入驻、3已停止合作)
        :param reason: (Optional) 驳回原因
        :param distributorLevel: (Optional) 级次(0一级、1 二级)
        :param distributorType: (Optional) 渠道商类型(0合作伙伴、1 渠道代理)
        :param parentDistributorId: (Optional) 上级渠道商ID
        :param bankCompanyName: (Optional) 银行开户名
        :param bankCardNo: (Optional) 银行账户
        :param bankBranchName: (Optional) 开户行支行名称
        :param bankBranchNo: (Optional) 开户行支行联行号
        :param contractSubject: (Optional) 合同主体
        :param dept: (Optional) 所属部门(0企业线、1政府线)
        :param returnFlag: (Optional) 是否需要返还（0需要1不需要）
        :param returnPolicyId: (Optional) 返还政策ID
        :param distributorProductList: (Optional) 
        :param circleType: (Optional) 结算周期类型（1月、2季度、3年、4天、5周）
        :param returnMode: (Optional) 服务商返还方式（1现金2代金券）
        :param subFlag: (Optional) 是否有下级服务商（0有1不没有）
        :param subReturnFlag: (Optional) 下级服务商是否需要返还（0需要1不需要）
        :param subReturnPolicyId: (Optional) 下级服务商返还政策ID
        :param subCircleType: (Optional) 结算周期类型（1月、2季度、3年、4天、5周）
        :param subReturnMode: (Optional) 下级服务商返还方式（1现金2代金券）
        :param erp: (Optional) 京东云负责人(京东云人员erp或名称)
        """

        self.distributorId = distributorId
        self.distributorName = distributorName
        self.pin = pin
        self.contractNo = contractNo
        self.businessLicense = businessLicense
        self.legalRepresentative = legalRepresentative
        self.businessLicensePic = businessLicensePic
        self.businessDesc = businessDesc
        self.workAddress = workAddress
        self.contracter = contracter
        self.tel = tel
        self.email = email
        self.region = region
        self.settleTime = settleTime
        self.status = status
        self.reason = reason
        self.distributorLevel = distributorLevel
        self.distributorType = distributorType
        self.parentDistributorId = parentDistributorId
        self.bankCompanyName = bankCompanyName
        self.bankCardNo = bankCardNo
        self.bankBranchName = bankBranchName
        self.bankBranchNo = bankBranchNo
        self.contractSubject = contractSubject
        self.dept = dept
        self.returnFlag = returnFlag
        self.returnPolicyId = returnPolicyId
        self.distributorProductList = distributorProductList
        self.circleType = circleType
        self.returnMode = returnMode
        self.subFlag = subFlag
        self.subReturnFlag = subReturnFlag
        self.subReturnPolicyId = subReturnPolicyId
        self.subCircleType = subCircleType
        self.subReturnMode = subReturnMode
        self.erp = erp
