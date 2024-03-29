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


class HitLocationInfos(object):

    def __init__(self, hitInfo=None, x1=None, y1=None, x2=None, y2=None):
        """
        :param hitInfo: (Optional) 命中详情
        :param x1: (Optional) 位置信息，对应目标矩形左上角横坐标相对坐标
        :param y1: (Optional) 位置信息，对应目标矩形左上角纵坐标相对坐标
        :param x2: (Optional) 位置信息，对应目标矩形右下角横坐标相对坐标
        :param y2: (Optional) 置信息，对应目标矩形右下角纵坐标相对坐标
        """

        self.hitInfo = hitInfo
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
