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


class CreateInstancesRequest(JDCloudRequest):
    """
    
创建一台或多台指定配置的云主机实例。

实例有三种创建方式，不同方式下传参详见下方的请求[参数说明](createInstance#requestparameters)，也可参考请求[示例](createInstance#examples)。

1、自定义创建：按配置要求逐一指定参数创建；
2、使用实例模板创建：[实例模板](https://docs.jdcloud.com/virtual-machines/instance-template-overview)是实例配置信息的预配置，通过实例模板可快速创建实例，省去逐一配置参数的步骤。指定实例模板创建时，如不额外指定模板包含的参数将以模板为准创建实例，模板中未包含的参数，如可用区、内网IPv4地址、名称等仍需指定；
3、基于高可用组创建：[高可用组](https://docs.jdcloud.com/availability-group/product-overview)是一种高可用部署解决方案，提供了组内实例在数据中心内横跨多个故障域均衡部署的机制。高可用组须搭配实例模板使用，基于高可用组创建的实例将在其指定的可用区内以实例模板配置按一定分散机制创建实例。此创建方式下，实例创建参数除内网IPv4地址、名称等外均以实例模板为准且不支持再次指定。

详细操作说明请参考帮助文档：[创建实例](https://docs.jdcloud.com/cn/virtual-machines/create-instance)

## 接口说明
- 创建实例前，请参考 [创建前准备](https://docs.jdcloud.com/virtual-machines/account-preparation-linux) 完成实名认证、支付方式确认、计费类型选择等准备工作。
- 创建实例的配置说明和选择指导，请参考 [配置项说明](https://docs.jdcloud.com/cn/virtual-machines/select-configuration-linux)。
- 各地域下实例及关联资源（云硬盘、弹性公网IP）的可创建数量受配额限制，创建前请通过 [DescribeQuotas](https://docs.jdcloud.com/cn/virtual-machines/api/describequotas?content=API) 确认配额，如须提升请[提交工单](https://ticket.jdcloud.com/applyorder/submit)或联系京东云客服。
- 不同地域及可用区下售卖的实例规格有差异，可通过 [DescribeInstanceTypes](https://docs.jdcloud.com/virtual-machines/api/describeinstancetypes?content=API) 查询在售规格及规格详细信息。
- 通过本接口创建包年包月实例时将自动从账户扣款（代金券优先），如需使用第三方支付方式请通过控制台创建。
- 单次请求最多支持创建 `100` 台实例。
- 本接口为异步接口，请求下发成功后会返回RequestId和实例ID，此时实例处于 `Pending`（创建中）状态。如创建成功则实例自动变为 `Running`（运行中）状态；如创建失败则短暂处于 `Error`（错误）状态，随后将自动删除（创建失败的实例不会收费且会自动释放占用的配额）。实例状态可以通过 [describeInstanceStatus](https://docs.jdcloud.com/virtual-machines/api/describeinstancestatus?content=API) 接口查询。
- 批量创建多台实例时系统将尽可能完成目标创建数量，但受底层资源、配额等因素影响，可能存在部分成功部分失败的情况，还请关注最终完成数量，如有失败情况请尝试重新申请或联系客服。

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(CreateInstancesRequest, self).__init__(
            '/regions/{regionId}/instances', 'POST', header, version)
        self.parameters = parameters


class CreateInstancesParameters(object):

    def __init__(self,regionId, instanceSpec, ):
        """
        :param regionId: 地域ID。
        :param instanceSpec: 实例配置。

        """

        self.regionId = regionId
        self.instanceSpec = instanceSpec
        self.maxCount = None
        self.clientToken = None

    def setMaxCount(self, maxCount):
        """
        :param maxCount: (Optional) 创建实例的数量，不能超过用户配额。
取值范围：[1,100]；默认值：1。

        """
        self.maxCount = maxCount

    def setClientToken(self, clientToken):
        """
        :param clientToken: (Optional) 用于保证请求的幂等性。由客户端生成，并确保不同请求中该参数唯一，长度不能超过64个字符。

        """
        self.clientToken = clientToken

