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

from jdcloud_sdk.core.jdcloudrequest import JDCloudRequest


class CreateLoadBalancerRequest(JDCloudRequest):
    """
    创建负载均衡
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(CreateLoadBalancerRequest, self).__init__(
            '/regions/{regionId}/loadBalancers/', 'POST', header, version)
        self.parameters = parameters


class CreateLoadBalancerParameters(object):

    def __init__(self, regionId,loadBalancerName, subnetId, ):
        """
        :param regionId: Region ID
        :param loadBalancerName: LoadBalancer的名称,只允许输入中文、数字、大小写字母、英文下划线“_”及中划线“-”，不允许为空且不超过32字符
        :param subnetId: LoadBalancer所属子网的Id
        """

        self.regionId = regionId
        self.loadBalancerName = loadBalancerName
        self.subnetId = subnetId
        self.type = None
        self.azs = None
        self.chargeSpec = None
        self.elasticIp = None
        self.privateIpAddress = None
        self.securityGroupIds = None
        self.description = None
        self.domainEnable = None
        self.deleteProtection = None
        self.userTags = None

    def setType(self, type):
        """
        :param type: (Optional) LoadBalancer的类型，取值：alb、nlb、dnlb，默认为alb
        """
        self.type = type

    def setAzs(self, azs):
        """
        :param azs: (Optional) 【alb，nlb】LoadBalancer所属availability Zone列表,对于alb,nlb是必选参数，可用区个数不能超过2个 <br>【dnlb】全可用区可用，不必传该参数
        """
        self.azs = azs

    def setChargeSpec(self, chargeSpec):
        """
        :param chargeSpec: (Optional) 【alb】支持按用量计费，默认为按用量。【nlb】支持按用量计费。【dnlb】支持按配置计费
        """
        self.chargeSpec = chargeSpec

    def setElasticIp(self, elasticIp):
        """
        :param elasticIp: (Optional) 负载均衡关联的弹性IP规格
        """
        self.elasticIp = elasticIp

    def setPrivateIpAddress(self, privateIpAddress):
        """
        :param privateIpAddress: (Optional) 指定LoadBalancer的VIP(内网IPv4地址)，需要属于指定的子网并且未被占用
        """
        self.privateIpAddress = privateIpAddress

    def setSecurityGroupIds(self, securityGroupIds):
        """
        :param securityGroupIds: (Optional) 【alb】 安全组 ID列表
        """
        self.securityGroupIds = securityGroupIds

    def setDescription(self, description):
        """
        :param description: (Optional) LoadBalancer的描述信息,允许输入UTF-8编码下的全部字符，不超过256字符
        """
        self.description = description

    def setDomainEnable(self, domainEnable):
        """
        :param domainEnable: (Optional) 是否绑定域名，包括外网和内网，缺省为False(关闭)
        """
        self.domainEnable = domainEnable

    def setDeleteProtection(self, deleteProtection):
        """
        :param deleteProtection: (Optional) 删除保护，取值为True(开启)或False(关闭)，默认为False
        """
        self.deleteProtection = deleteProtection

    def setUserTags(self, userTags):
        """
        :param userTags: (Optional) 用户tag 信息
        """
        self.userTags = userTags

