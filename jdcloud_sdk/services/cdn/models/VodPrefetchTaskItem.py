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


class VodPrefetchTaskItem(object):

    def __init__(self, url=None, region=None, isp=None, copyNum=None):
        """
        :param url: (Optional) url
        :param region: (Optional) 地区[huabei huadong dongbei huazhong huanan xinan xibei gangaotai]中的一个
        :param isp: (Optional) 运营商[ct uni cm]中的一个,分别代表电信 联通 移动
        :param copyNum: (Optional) 副本数
        """

        self.url = url
        self.region = region
        self.isp = isp
        self.copyNum = copyNum
