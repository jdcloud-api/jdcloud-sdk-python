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


class DeviceDataRiskOverview(object):

    def __init__(self, allDevice=None, allDevicePercent=None, normal=None, normalPercent=None, tuoJiGua=None, tuoJiGuaPercent=None, forgery=None, forgeryPercent=None, cloudPhone=None, cloudPhonePercent=None, root=None, rootPercent=None, hook=None, hookPercent=None, duoKai=None, duoKaiPercent=None, moNi=None, moNiPercent=None):
        """
        :param allDevice: (Optional) 设备总量
        :param allDevicePercent: (Optional) 设备总量环比百分率
        :param normal: (Optional) 正常
        :param normalPercent: (Optional) 正常设备环比百分率
        :param tuoJiGua: (Optional) 脱机挂
        :param tuoJiGuaPercent: (Optional) 脱机挂设备环比百分率
        :param forgery: (Optional) 伪造
        :param forgeryPercent: (Optional) 伪造设备环比百分率
        :param cloudPhone: (Optional) 云手机
        :param cloudPhonePercent: (Optional) 云手机设备环比百分率
        :param root: (Optional) root/越狱
        :param rootPercent: (Optional) root/越狱设备环比百分率
        :param hook: (Optional) hook
        :param hookPercent: (Optional) hook设备环比百分率
        :param duoKai: (Optional) 多开
        :param duoKaiPercent: (Optional) 多开设备环比百分率
        :param moNi: (Optional) 模拟器
        :param moNiPercent: (Optional) 模拟器设备环比百分率
        """

        self.allDevice = allDevice
        self.allDevicePercent = allDevicePercent
        self.normal = normal
        self.normalPercent = normalPercent
        self.tuoJiGua = tuoJiGua
        self.tuoJiGuaPercent = tuoJiGuaPercent
        self.forgery = forgery
        self.forgeryPercent = forgeryPercent
        self.cloudPhone = cloudPhone
        self.cloudPhonePercent = cloudPhonePercent
        self.root = root
        self.rootPercent = rootPercent
        self.hook = hook
        self.hookPercent = hookPercent
        self.duoKai = duoKai
        self.duoKaiPercent = duoKaiPercent
        self.moNi = moNi
        self.moNiPercent = moNiPercent
