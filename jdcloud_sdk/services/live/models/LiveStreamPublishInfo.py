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


class LiveStreamPublishInfo(object):

    def __init__(self, startTime=None, appName=None, streamName=None, bitrate=None, framerate=None):
        """
        :param startTime: (Optional) 流起始时间
        :param appName: (Optional) 应用名称
        :param streamName: (Optional) 流名称
        :param bitrate: (Optional) 码率
        :param framerate: (Optional) 帧率
        """

        self.startTime = startTime
        self.appName = appName
        self.streamName = streamName
        self.bitrate = bitrate
        self.framerate = framerate
