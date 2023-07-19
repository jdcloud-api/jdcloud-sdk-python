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


class AsCronInfoByAsRule(object):

    def __init__(self, asCronId=None, name=None, description=None, launchTime=None, repeatType=None, repeatValue=None, repeatEndTime=None, launchExpirationTime=None, createTime=None, updateTime=None, displayState=None):
        """
        :param asCronId: (Optional) 定时任务ID
        :param name: (Optional) 定时任务名称
        :param description: (Optional) 定时任务描述
        :param launchTime: (Optional) 定时任务触发的时间点
时间格式：`2023-05-10 10:10:00`，目前只支持到分钟，秒数会被忽略，但是需要严格按照此时间格式填写
- 如果未指定`repeatType`，则按指定的日期和时间执行一次
- 如果指定了`repeatType`，则此属性指定的时间点，表示从这个时间之后开始按照重复周期执行定时任务

        :param repeatType: (Optional) 重复执行定时任务的类型，如果`repeatType`有值，则`repeatValue`也会有值
取值范围：[`Daily`,`Weekly`,`Monthly`,`Cron`]
- Daily：每多少天重复执行一次定时任务
- Weekly：每周指定几天重复执行一次定时任务
- Monthly：每月内指定几天重复执行一次定时任务
- Cron：按照指定的Cron表达式执行定时任务

        :param repeatValue: (Optional) 重复执行定时任务的数值，如果`repeatType`有值，则`repeatValue`也会有值
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

        :param repeatEndTime: (Optional) 重复执行定时任务的结束时间，若为空，表示不限制结束时间，一直重复执行
        :param launchExpirationTime: (Optional) 定时任务触发操作失败后，在此时间内重试，单位为秒
        :param createTime: (Optional) 创建时间
        :param updateTime: (Optional) 更新时间
        :param displayState: (Optional) 定时任务状态，取值范围如下：
  - `Disabled`：已禁用
  - `Enabled`：已启用

        """

        self.asCronId = asCronId
        self.name = name
        self.description = description
        self.launchTime = launchTime
        self.repeatType = repeatType
        self.repeatValue = repeatValue
        self.repeatEndTime = repeatEndTime
        self.launchExpirationTime = launchExpirationTime
        self.createTime = createTime
        self.updateTime = updateTime
        self.displayState = displayState