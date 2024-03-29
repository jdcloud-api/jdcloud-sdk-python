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


class UpdateWatermarkRequest(JDCloudRequest):
    """
    修改水印
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(UpdateWatermarkRequest, self).__init__(
            '/watermarks/{watermarkId}', 'PUT', header, version)
        self.parameters = parameters


class UpdateWatermarkParameters(object):

    def __init__(self, watermarkId,):
        """
        :param watermarkId: 水印ID
        """

        self.watermarkId = watermarkId
        self.name = None
        self.imgUrl = None
        self.width = None
        self.height = None
        self.sizeUnit = None
        self.widthRef = None
        self.heightRef = None
        self.position = None
        self.offsetX = None
        self.offsetY = None
        self.offsetUnit = None

    def setName(self, name):
        """
        :param name: (Optional) 水印名称。只支持中英文、数字。长度不超过128个字符。UTF-8编码。

        """
        self.name = name

    def setImgUrl(self, imgUrl):
        """
        :param imgUrl: (Optional) 图片地址
        """
        self.imgUrl = imgUrl

    def setWidth(self, width):
        """
        :param width: (Optional) 水印宽度。
当 sizeUnit = pixel 时，取值范围为 [8, 4096] 整数
当 sizeUnit = percent 时，取值范围为 [0, 100] 小数

        """
        self.width = width

    def setHeight(self, height):
        """
        :param height: (Optional) 水印高度。
当 sizeUnit = pixel 时，取值范围为 [8, 4096] 整数
当 sizeUnit = percent 时，取值范围为 [0, 100] 小数

        """
        self.height = height

    def setSizeUnit(self, sizeUnit):
        """
        :param sizeUnit: (Optional) 尺寸单位。取值范围：
  pixel - 像素
  percent - 百分比
默认值为 pixel

        """
        self.sizeUnit = sizeUnit

    def setWidthRef(self, widthRef):
        """
        :param widthRef: (Optional) 
        """
        self.widthRef = widthRef

    def setHeightRef(self, heightRef):
        """
        :param heightRef: (Optional) 高度参考，仅当 siteUnit = percent 时生效。
取值说明：
  w: 输出水印高度 = height * 水印原图高度
  v: 等同于 vh
  vw: 输出水印高度 = height * 输出视频宽度
  vh: 输出水印高度 = height * 输出视频高度
  vls: 输出水印高度 = height * 输出视频长边
  vss: 输出水印高度 = height * 输出视频短边

        """
        self.heightRef = heightRef

    def setPosition(self, position):
        """
        :param position: (Optional) 水印位置。取值范围：
  LT - 左上
  RT - 右上
  LB - 左下
  RB - 右下

        """
        self.position = position

    def setOffsetX(self, offsetX):
        """
        :param offsetX: (Optional) 水平偏移。
当 offsetUnit = pixel 时，取值范围为 [8, 4088] 整数
当 offsetUnit = percent 时，取值范围为 [0, 100] 小数

        """
        self.offsetX = offsetX

    def setOffsetY(self, offsetY):
        """
        :param offsetY: (Optional) 竖直偏移。
当 offsetUnit = pixel 时，取值范围为 [8, 4088] 整数
当 offsetUnit = percent 时，取值范围为 [0, 100] 小数

        """
        self.offsetY = offsetY

    def setOffsetUnit(self, offsetUnit):
        """
        :param offsetUnit: (Optional) 偏移单位。取值范围：
  pixel - 像素
  percent - 百分比
默认值为 pixel

        """
        self.offsetUnit = offsetUnit

