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


class CreateAlarmRequest(JDCloudRequest):
    """
    创建报警规则
    """

    def __init__(self, parameters, header=None, version="v2"):
        super(CreateAlarmRequest, self).__init__(
            '/groupAlarms', 'POST', header, version)
        self.parameters = parameters


class CreateAlarmParameters(object):

    def __init__(self, clientToken, product, resourceOption, ruleName, ruleOption, ):
        """
        :param clientToken: 幂等性校验参数,最长36位,若两个请求clientToken相等，则返回第一次创建的规则id，只创建一次规则
        :param product: 资源类型, 可用的资源类型列表请使用 describeProductsForAlarm接口查询。
        :param resourceOption: 
        :param ruleName: 规则名称，规则名称，最大长度42个字符，只允许中英文、数字、''-''和"_"
        :param ruleOption: 
        """

        self.autoScalingPolicyId = None
        self.baseContact = None
        self.clientToken = clientToken
        self.dataOwner = None
        self.dimension = None
        self.enabled = None
        self.multiWebHook = None
        self.noticeOption = None
        self.product = product
        self.resourceOption = resourceOption
        self.ruleName = ruleName
        self.ruleOption = ruleOption
        self.ruleType = None
        self.tags = None
        self.webHookOption = None

    def setAutoScalingPolicyId(self, autoScalingPolicyId):
        """
        :param autoScalingPolicyId: (Optional) 弹性伸缩组Id。注：仅ag\asg产品线内部使用
        """
        self.autoScalingPolicyId = autoScalingPolicyId

    def setBaseContact(self, baseContact):
        """
        :param baseContact: (Optional) 告警通知联系人
        """
        self.baseContact = baseContact

    def setDataOwner(self, dataOwner):
        """
        :param dataOwner: (Optional) 数据所有者，1云监控控制台; 2云鼎。默认为1
        """
        self.dataOwner = dataOwner

    def setDimension(self, dimension):
        """
        :param dimension: (Optional) 资源维度，可用的维度请使用 describeProductsForAlarm接口查询
        """
        self.dimension = dimension

    def setEnabled(self, enabled):
        """
        :param enabled: (Optional) 是否启用, 1表示启用规则，0表示禁用规则，默认为1
        """
        self.enabled = enabled

    def setMultiWebHook(self, multiWebHook):
        """
        :param multiWebHook: (Optional) url回调设置数组
        """
        self.multiWebHook = multiWebHook

    def setNoticeOption(self, noticeOption):
        """
        :param noticeOption: (Optional) 通知策略
        """
        self.noticeOption = noticeOption

    def setRuleType(self, ruleType):
        """
        :param ruleType: (Optional) 规则类型, 默认为resourceMonitor
        """
        self.ruleType = ruleType

    def setTags(self, tags):
        """
        :param tags: (Optional) 资源维度，指定监控数据实例的维度标签,如resourceId=id。(请确认资源的监控数据带有该标签，否则规则会报数据不足)
        """
        self.tags = tags

    def setWebHookOption(self, webHookOption):
        """
        :param webHookOption: (Optional) 
        """
        self.webHookOption = webHookOption

