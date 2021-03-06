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


class DataDiskAttachment(object):

    def __init__(self, autoDelete=None, dataDisk=None, deviceName=None, diskCategory=None):
        """
        :param autoDelete: (Optional) 是否随云主机一起删除,true：自动；false：非自动
        :param dataDisk: (Optional) 
        :param deviceName: (Optional) 数据盘逻辑挂载点
        :param diskCategory: (Optional) 磁盘分类,取值为本地盘(local)或者数据盘(cloud)
        """

        self.autoDelete = autoDelete
        self.dataDisk = dataDisk
        self.deviceName = deviceName
        self.diskCategory = diskCategory
