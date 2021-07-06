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


class FaceContentItem(object):

    def __init__(self, name=None, gender=None, age=None, type=None, category=None, x1=None, y1=None, x2=None, y2=None):
        """
        :param name: (Optional) 人脸名字，不可识别则为空
        :param gender: (Optional) 人脸性别，值为男（male）、女（female）；不可识别则为空
        :param age: (Optional) 人脸年龄，值为具体年龄（age）；不可识别则为空
        :param type: (Optional) 人脸类型，包含卡通脸（cartoon）、普通（normal）
        :param category: (Optional) 人物分类，包含名人（star）、普通（normal）
        :param x1: (Optional) 人脸位置信息，对应人脸矩形左上角横坐标相对坐标
        :param y1: (Optional) 人脸位置信息，对应人脸矩形左上角纵坐标相对坐标
        :param x2: (Optional) 人脸位置信息，对应人脸矩形右下角横坐标相对坐标
        :param y2: (Optional) 人脸位置信息，对应人脸矩形右下角纵坐标相对坐标
        """

        self.name = name
        self.gender = gender
        self.age = age
        self.type = type
        self.category = category
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2