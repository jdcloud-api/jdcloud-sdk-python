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


class ImageSampleConfig(object):

    def __init__(self, startTime=None, intervalTime=None, frameType=None, format=None, number=None, width=None, height=None, fillType=None):
        """
        :param startTime: (Optional) 截图起始时间，取值范围单位为秒，缺省值为 0

        :param intervalTime: (Optional) 截图时间间隔。单位为毫秒
若未设置，则对于普通截图，按照截图张数做平均截图；对于雪碧图，则按照行列数乘积做平均截图

        :param frameType: (Optional) 截图帧类型。取值范围：
  any - 任意帧
  intra - 关键帧
缺省值为 any

        :param format: (Optional) 截图格式。取值范围：jpg、png
        :param number: (Optional) 截图数量，缺省值为 10
        :param width: (Optional) 截图宽度，取值范围：[8, 4096]
若宽度和高度同时设置，则按照设置的宽高截图；
若宽度和高度均未设置，则截图保持与源视频相同的宽高值；
若宽度和高度其中一项未设置，则截图保持与源视频相同的宽高比；

        :param height: (Optional) 截图高度，取值范围：[8, 4096]
若宽度和高度同时设置，则按照设置的宽高截图；
若宽度和高度均未设置，则截图保持与源视频相同的宽高值；
若宽度和高度其中一项未设置，则截图保持与源视频相同的宽高比；

        :param fillType: (Optional) 填充方式，当视频宽高与截图宽高指定值不能匹配时的填充处理方式。取值范围：
  stretch - 伸缩
  black - 留黑
  white - 留白
  gauss - 高斯模糊
缺省值为 black

        """

        self.startTime = startTime
        self.intervalTime = intervalTime
        self.frameType = frameType
        self.format = format
        self.number = number
        self.width = width
        self.height = height
        self.fillType = fillType
