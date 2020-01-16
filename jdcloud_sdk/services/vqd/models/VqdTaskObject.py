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


class VqdTaskObject(object):

    def __init__(self, taskId=None, templateId=None, mediaName=None, threshold=None, detections=None, status=None, createTime=None, updateTime=None):
        """
        :param taskId: (Optional) 任务ID
        :param templateId: (Optional) 模板ID
        :param mediaName: (Optional) 媒体名称
        :param threshold: (Optional) 缺陷判定时间阈值
        :param detections: (Optional) 检测项列表
        :param status: (Optional) 任务状态。
- READY
- CANCELLED
- RUNNING
- FINISHED_SUCCESS
- FINISHED_FAILURE

        :param createTime: (Optional) 创建时间
        :param updateTime: (Optional) 更新时间
        """

        self.taskId = taskId
        self.templateId = templateId
        self.mediaName = mediaName
        self.threshold = threshold
        self.detections = detections
        self.status = status
        self.createTime = createTime
        self.updateTime = updateTime