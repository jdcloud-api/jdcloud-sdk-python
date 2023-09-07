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


class DescribeAuditOptionsRequest(JDCloudRequest):
    """
    获取当前系统所支持的各种数据库版本的审计选项及相应的推荐选项<br>- 仅支持SQL Server
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeAuditOptionsRequest, self).__init__(
            '/regions/{regionId}/instances/{instanceId}/audit:describeAuditOptions', 'GET', header, version)
        self.parameters = parameters


class DescribeAuditOptionsParameters(object):

    def __init__(self,regionId, instanceId, name):
        """
        :param regionId: 地域代码，取值范围参见[《各地域及可用区对照表》](../Enum-Definitions/Regions-AZ.md)
        :param instanceId: RDS 实例ID，唯一标识一个RDS实例
        :param name: 审计选项类别，**大小写敏感**，目前支持两种类型：<br>（1）AuditOptions开头：在disalbed参数中返回SQL Server各个版本支持的所有选项，支持的名称为<br>AuditOptions2008R2<br>AuditOptions2012<br>AuditOptions2014<br>AuditOptions2016<br>例如输入参数为"AuditOptions2016"，则在disabled字段中返回SQL Server 2016 版本所支持的所有的审计选项<br>（2）AuditDefault开头：京东云建议的默认选项,在enabled参数中返回建议开启的选项，在disabled参数中返回不开启的选项，支持的名称为：<br>AuditDefault2008R2<br>AuditDefault2012<br>AuditDefault2014<br>AuditDefault2016<br>例如输入参数为"AuditDefault2016"，则在enabled字段返回SQL Server 2016 版本中京东云建议开启的审计选项，在disabled字段中返回建议不开启的选项
        """

        self.regionId = regionId
        self.instanceId = instanceId
        self.name = name

