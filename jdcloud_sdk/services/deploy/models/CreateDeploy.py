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


class CreateDeploy(object):

    def __init__(self, groupId, deploySource, desc=None, deployCmd=None, cmdSource=None, cmdType=None, productType=None, downloadUrl=None, md5=None, compileProject=None, compileSeries=None, ossSpace=None, ossDir=None, fileType=None):
        """
        :param groupId:  部署组ID，部署组的唯一标识
        :param desc: (Optional) 描述
        :param deploySource:  部署来源：1url，2云编译，3云存储
        :param deployCmd: (Optional) 部署操作
        :param cmdSource: (Optional) 1使用输入的操作，2使用程序自带操作
        :param cmdType: (Optional) 部署操作展示格式：1form,2ymal
        :param productType: (Optional) 项目类型 1tomcat,2
        :param downloadUrl: (Optional) 下载url
        :param md5: (Optional) md5
        :param compileProject: (Optional) 云编译项目名
        :param compileSeries: (Optional) 云编译构建序号
        :param ossSpace: (Optional) 云存储空间
        :param ossDir: (Optional) 云存储目录
        :param fileType: (Optional) 文件类型：1.tar，2.zip,3.tar.gz
        """

        self.groupId = groupId
        self.desc = desc
        self.deploySource = deploySource
        self.deployCmd = deployCmd
        self.cmdSource = cmdSource
        self.cmdType = cmdType
        self.productType = productType
        self.downloadUrl = downloadUrl
        self.md5 = md5
        self.compileProject = compileProject
        self.compileSeries = compileSeries
        self.ossSpace = ossSpace
        self.ossDir = ossDir
        self.fileType = fileType
