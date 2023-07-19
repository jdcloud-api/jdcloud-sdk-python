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


class UpdateAsCronRequest(JDCloudRequest):
    """
    修改定时任务
- 所有参数取值为字符串类型的都严格区分大小写
- 定时任务换绑高可用组，如果目前伸缩方式是执行简单规则，那么需要重新从新的高可用组中选择一个简单规则
- 伸缩功能开启或者关闭的情况下，都支持调用此接口

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(UpdateAsCronRequest, self).__init__(
            '/regions/{regionId}/asCrons/{asCronId}', 'POST', header, version)
        self.parameters = parameters


class UpdateAsCronParameters(object):

    def __init__(self,regionId, asCronId, ):
        """
        :param regionId: 地域ID
        :param asCronId: 定时任务ID
        """

        self.regionId = regionId
        self.asCronId = asCronId
        self.agId = None
        self.name = None
        self.description = None
        self.asRuleId = None
        self.minSize = None
        self.maxSize = None
        self.desiredCapacity = None
        self.launchTime = None
        self.repeatType = None
        self.repeatValue = None
        self.repeatEndTime = None
        self.launchExpirationTime = None

    def setAgId(self, agId):
        """
        :param agId: (Optional) 高可用组ID
        """
        self.agId = agId

    def setName(self, name):
        """
        :param name: (Optional) 名称，长度为1~32个字符，只允许中文、数字、大小写字母、英文下划线（_）、连字符（-）
        """
        self.name = name

    def setDescription(self, description):
        """
        :param description: (Optional) 描述，最大长度为256个字符
        """
        self.description = description

    def setAsRuleId(self, asRuleId):
        """
        :param asRuleId: (Optional) 可以为定时任务绑定伸缩规则，目前只支持简单规则，即 `asRuleType` 为 `Simple` 的伸缩规则
- 如果指定了参数`asRuleId`，则不允许指定参数`minSize`,`maxSize`,`desiredCapacity`
- 如果指定了参数`asRuleId`，并且当前伸缩方式为执行简单规则，那么表示更换定时任务关联的伸缩规则
- 如果指定了参数`asRuleId`，但是当前伸缩方式为修改伸缩组属性[`minSize`,`maxSize`,`desiredCapacity`]，那么将会清空`minSize`,`maxSize`,`desiredCapacity`的值，同时设置`asRuleId`的值

        """
        self.asRuleId = asRuleId

    def setMinSize(self, minSize):
        """
        :param minSize: (Optional) 设置伸缩组最小实例数，必须大于等于0，如果没有设置此参数，则此参数将会保存为 -1
- 如果指定了参数`minSize`,`maxSize`,`desiredCapacity`三者任意一个或多个，则不允许指定参数`asRuleId`
- 如果指定了参数`minSize`,`maxSize`,`desiredCapacity`三者任意一个或多个，并且当前伸缩方式为修改伸缩组属性[`minSize`,`maxSize`,`desiredCapacity`]，那么将会更新`minSize`,`maxSize`,`desiredCapacity`指定的参数值
- 如果指定了参数`minSize`,`maxSize`,`desiredCapacity`三者任意一个或多个，但是当前伸缩方式为执行简单规则，那么将会清空`asRuleId`的值，同时设置`minSize`,`maxSize`,`desiredCapacity`指定的参数值

        """
        self.minSize = minSize

    def setMaxSize(self, maxSize):
        """
        :param maxSize: (Optional) 设置伸缩组最大实例数，必须大于等于0，如果没有设置此参数，则此参数将会保存为 -1
- 如果指定了参数`minSize`,`maxSize`,`desiredCapacity`三者任意一个或多个，则不允许指定参数`asRuleId`
- 如果指定了参数`minSize`,`maxSize`,`desiredCapacity`三者任意一个或多个，并且当前伸缩方式为修改伸缩组属性[`minSize`,`maxSize`,`desiredCapacity`]，那么将会更新`minSize`,`maxSize`,`desiredCapacity`指定的参数值
- 如果指定了参数`minSize`,`maxSize`,`desiredCapacity`三者任意一个或多个，但是当前伸缩方式为执行简单规则，那么将会清空`asRuleId`的值，同时设置`minSize`,`maxSize`,`desiredCapacity`指定的参数值

        """
        self.maxSize = maxSize

    def setDesiredCapacity(self, desiredCapacity):
        """
        :param desiredCapacity: (Optional) 设置伸缩组期望实例数，必须大于等于0，如果没有设置此参数，则此参数将会保存为 -1
- 如果指定了参数`minSize`,`maxSize`,`desiredCapacity`三者任意一个或多个，则不允许指定参数`asRuleId`
- 如果指定了参数`minSize`,`maxSize`,`desiredCapacity`三者任意一个或多个，并且当前伸缩方式为修改伸缩组属性[`minSize`,`maxSize`,`desiredCapacity`]，那么将会更新`minSize`,`maxSize`,`desiredCapacity`指定的参数值
- 如果指定了参数`minSize`,`maxSize`,`desiredCapacity`三者任意一个或多个，但是当前伸缩方式为执行简单规则，那么将会清空`asRuleId`的值，同时设置`minSize`,`maxSize`,`desiredCapacity`指定的参数值

        """
        self.desiredCapacity = desiredCapacity

    def setLaunchTime(self, launchTime):
        """
        :param launchTime: (Optional) 定时任务触发的时间点
时间格式：`2023-05-10 10:10:00`，目前只支持到分钟，秒数会被忽略，但是需要严格按照此时间格式填写
- 如果未指定`repeatType`，则按指定的日期和时间执行一次
- 如果指定了`repeatType`，则此属性指定的时间点，表示从这个时间之后开始按照重复周期执行定时任务
时间限制如下：
- 时间必须大于当前时间
- 不能填写当前时间起30日后的时间
- 时间必须小于`repeatEndTime`

        """
        self.launchTime = launchTime

    def setRepeatType(self, repeatType):
        """
        :param repeatType: (Optional) 重复执行定时任务的类型，如果指定了`repeatType`，则`repeatValue`必填
取值范围：[`Daily`,`Weekly`,`Monthly`,`Cron`]
- Daily：每多少天重复执行一次定时任务
- Weekly：每周指定几天重复执行一次定时任务
- Monthly：每月内指定几天重复执行一次定时任务
- Cron：按照指定的Cron表达式执行定时任务

        """
        self.repeatType = repeatType

    def setRepeatValue(self, repeatValue):
        """
        :param repeatValue: (Optional) 重复执行定时任务的数值，如果指定了`repeatType`，则`repeatValue`必填
- `repeatType`取值为`Daily`时，只能填一个值，取值范围：[ `1` ~ `31` ]，表示：每几天执行
- `repeatType`取值为`Weekly`时，可以填入多个值，填多个值时使用半角逗号（,）分隔。取值范围：[`0`,`1`,`2`,`3`,`4`,`5`,`6`]，分别对应：周日、周一、周二、周三、周四、周五、周六，表示：每周几执行
- `repeatType`取值为`Monthly`时，格式为A-B。A、B的取值范围：[ `1` ~ `31` ]，并且B必须大于等于A，表示：每个月的几号到几号执行
- `repeatType`取值为`Cron`时，必须填写Cron表达式，不支持秒，最小单位为分钟

支持的Cron格式如下：
*    *    *    *    *   从左到右依次表示：`[分] [小时] [日] [月] [周]`

- 分，取值范围：[`0` ~ `59`]，允许的连接符号取值范围：[`*` `/` `,` `-`]
- 小时，取值范围：[`0` ~ `23`]，允许的连接符号取值范围：[`*` `/` `,` `-`]
- 日，取值范围：[`1` ~ `31`]，允许的连接符号取值范围：[`*` `/` `,` `-` `?`]
- 月，取值范围：[`1` ~ `12`]，允许的连接符号取值范围：[`*` `/` `,` `-`]
- 周，取值范围：[`0` ~ `6`]，允许的连接符号取值范围：[`*` `/` `,` `-` `?`]

符号解析：`*`表示任意值，`/`表示步长，`,`表示多个值，`-`表示范围，`?`表示不指定值

示例：0 10 * * *  表示：每天10点执行

        """
        self.repeatValue = repeatValue

    def setRepeatEndTime(self, repeatEndTime):
        """
        :param repeatEndTime: (Optional) 重复执行定时任务的结束时间
默认为空，表示不限制结束时间，一直重复执行
时间格式：`2023-05-10 10:10:00`，目前只支持到分钟，秒数会被忽略，但是需要严格按照此时间格式填写
时间限制如下：
- 时间必须大于`launchTime`

        """
        self.repeatEndTime = repeatEndTime

    def setLaunchExpirationTime(self, launchExpirationTime):
        """
        :param launchExpirationTime: (Optional) 定时任务触发操作失败后，在此时间内重试，单位为秒，取值范围：[`0` ~ `1800`]
        """
        self.launchExpirationTime = launchExpirationTime
