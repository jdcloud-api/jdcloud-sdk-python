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


class Erpinstance(object):

    def __init__(self, userPin=None, instanceId=None, instanceName=None, instanceVersion=None, instanceRegion=None, instanceStatus=None, instanceFlavor=None, azId=None, vpcId=None, subnetId=None, exposedDomain=None, replica=None, cloudstorage=None, serviceConfig=None, createTime=None, gw_dev_id=None, gw_dev_num=None, chargeType=None, chargeExpired=None, is_deleted=None):
        """
        :param userPin: (Optional) 用户Pin
        :param instanceId: (Optional) 实例ID
        :param instanceName: (Optional) 实例名称
        :param instanceVersion: (Optional) 实例版本
        :param instanceRegion: (Optional) 所在地域
        :param instanceStatus: (Optional) 实例状态，running：运行，error：错误，creating：创建中，changing：变配中
        :param instanceFlavor: (Optional) 实例硬件配置规格 例如:2C4G20G
        :param azId: (Optional) az信息
        :param vpcId: (Optional) 所属VPC的ID
        :param subnetId: (Optional) 所属子网的ID
        :param exposedDomain: (Optional) 下行控制管理域名和设备上行链接的外网域名
        :param replica: (Optional) 节点个数
        :param cloudstorage: (Optional) 云硬盘大小
        :param serviceConfig: (Optional) 实例服务配置
        :param createTime: (Optional) 创建时间
        :param gw_dev_id: (Optional) 网关设备ID
        :param gw_dev_num: (Optional) 网关子设备数
        :param chargeType: (Optional) 计费类型
        :param chargeExpired: (Optional) 计费过期时间
        :param is_deleted: (Optional) 是否已经软删除
        """

        self.userPin = userPin
        self.instanceId = instanceId
        self.instanceName = instanceName
        self.instanceVersion = instanceVersion
        self.instanceRegion = instanceRegion
        self.instanceStatus = instanceStatus
        self.instanceFlavor = instanceFlavor
        self.azId = azId
        self.vpcId = vpcId
        self.subnetId = subnetId
        self.exposedDomain = exposedDomain
        self.replica = replica
        self.cloudstorage = cloudstorage
        self.serviceConfig = serviceConfig
        self.createTime = createTime
        self.gw_dev_id = gw_dev_id
        self.gw_dev_num = gw_dev_num
        self.chargeType = chargeType
        self.chargeExpired = chargeExpired
        self.is_deleted = is_deleted
