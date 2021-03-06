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


class FieldDesc(object):

    def __init__(self, fieldName=None, fieldType=None, fieldLength=None, fieldAttr=None, fieldComment=None, encryptField=None, indexField=None, keepPlainText=None, fieldTag=None, fieldLevel=None):
        """
        :param fieldName: (Optional) 字段名称
        :param fieldType: (Optional) 字段类型，如 varchar
        :param fieldLength: (Optional) 字段长度，如 11
        :param fieldAttr: (Optional) 字段属性
        :param fieldComment: (Optional) 字段描述
        :param encryptField: (Optional) 加密字段
        :param indexField: (Optional) 索引字段
        :param keepPlainText: (Optional) 是否保留明文字段
        :param fieldTag: (Optional) 敏感数据标记
        :param fieldLevel: (Optional) 敏感数据等级
        """

        self.fieldName = fieldName
        self.fieldType = fieldType
        self.fieldLength = fieldLength
        self.fieldAttr = fieldAttr
        self.fieldComment = fieldComment
        self.encryptField = encryptField
        self.indexField = indexField
        self.keepPlainText = keepPlainText
        self.fieldTag = fieldTag
        self.fieldLevel = fieldLevel
