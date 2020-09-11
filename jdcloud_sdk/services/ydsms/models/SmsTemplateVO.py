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


class SmsTemplateVO(object):

    def __init__(self, appId=None, applyStatus=None, createTime=None, pin=None, status=None, templateContent=None, templateId=None, templateName=None, templateType=None, updateTime=None):
        """
        :param appId: (Optional) 应用id
        :param applyStatus: (Optional) 申请状态 1申请中,2拒绝,3通过
        :param createTime: (Optional) 创建时间
        :param pin: (Optional) 用户pin
        :param status: (Optional) 模板状态 0 未启用  1 启用
        :param templateContent: (Optional) 模板内容
        :param templateId: (Optional) 模板id
        :param templateName: (Optional) 模板名称
        :param templateType: (Optional) 模板类型，0 验证码短信,1 通知短信,2 推广短信
        :param updateTime: (Optional) 
        """

        self.appId = appId
        self.applyStatus = applyStatus
        self.createTime = createTime
        self.pin = pin
        self.status = status
        self.templateContent = templateContent
        self.templateId = templateId
        self.templateName = templateName
        self.templateType = templateType
        self.updateTime = updateTime
