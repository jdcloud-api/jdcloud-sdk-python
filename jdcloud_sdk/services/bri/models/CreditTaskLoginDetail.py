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


class CreditTaskLoginDetail(object):

    def __init__(self, phone=None, loginIp=None, loginType=None, loginName=None, channel=None, deviceName=None, deviceVersion=None, deviceOS=None, deviceOSVersion=None, loginTime=None, elapsedTime=None, loginResult=None, loginEmail=None, macAddress=None, imei=None, idfa=None, regIp=None, eid=None, regTime=None, bizType=None, authType=None, appId=None, mobileBrand=None, appVersion=None, mouseClickCount=None, keyboardClickCount=None, referer=None, jumpUrl=None, userAgent=None, xForwardedFor=None):
        """
        :param phone: (Optional) 注册手机号，国内手机：11位手机号;海外手机：以+号开头，4位国家代码+5-11位手机号扩展位；手机注册，必填
        :param loginIp: (Optional) 登录IP，用户登录IP，IPV4 或 IPV6
        :param loginType: (Optional) 登录认证方式，1：手动帐号密码输入；2：动态短信密码登录；3：二维码扫描登录；0其他
        :param loginName: (Optional) 登录账号名pin，用户登录使用名称
        :param channel: (Optional) 注册渠道或注册终端，1：PC端web浏览器注册 PC-Brower；2：PC客户端注册 PC-Client；3：移动设备各种APP注册 Mobile-APP；4 ：移动设备浏览器登录，移动端M页注册 Mobile-Brower；5：移动设备微信客户端中购物入口的注册操作 Mobile-WX；6： 移动设备QQ客户端中购物入口的注册操作 Mobile-QQ；7： 移动设备微信客户端中微信小程序注册操作- Mobile-WX；0：其他
        :param deviceName: (Optional) 应用设备名称，PC 端：如果为浏览器说明浏览器名称 IE、firefox、chrome等;移动APP端：请说明移动APP名称
        :param deviceVersion: (Optional) 应用设备版本，跟deviceName关联，说明deviceName对应的版本
        :param deviceOS: (Optional) 设备操作系统，说明设备的操作系统，如windows ，openSUSE、debian、ubuntu，unix, android, ios 等。
        :param deviceOSVersion: (Optional) 设备操作系统版本，说明设备的操作系统版本，跟deviceOs 字段关联，例如deviceOs为android，此处可以为 3.0，4.0，4.2，5.0 等。
        :param loginTime: (Optional) 登录时间，用户登录完成时间，UNIX时间戳
        :param elapsedTime: (Optional) 登录占用时长，从出登录页到登录提交之间的时间差（出登录视图埋点，提交时计算时间差），如果为免密码登录方式，可以在换取认证token时生成时间戳，验证token时计算时间差，单位ms
        :param loginResult: (Optional) 登录结果，1：登录成功；2： 用户不存在，无法登录；3 ：密码错误，无法登录；4： 密码错误，账号被锁定；5： 账号未通过审核，无法登录；6：账号审核中，无法登录；7：账号锁定，无法登录；8： 账号已注销，无法登录；9：短信验证码错误，无法登录；10：风险账号，无法登录；11：验证码错误，无法登录；0：其他；
        :param loginEmail: (Optional) 登录邮箱，用户登录邮箱，可选参数
        :param macAddress: (Optional) MAC地址，MAC 地址或设备唯一标识。
        :param imei: (Optional) 手机设备号，Android：imei，IOS：idfa
        :param idfa: (Optional) 手机设备号，Android：imei，IOS：idfa
        :param regIp: (Optional) 注册ip，用户注册IP，IPV4 或 IPV
        :param eid: (Optional) 设备ID，设备指纹编码
        :param regTime: (Optional) 注册时间，用户注册完成时间，UNIX时间戳
        :param bizType: (Optional) 业务类型，1、个人；2、商家；3、企业；4、其他
        :param authType: (Optional) 认证方式，1 - PC 用户名/登录名+密码登录；2 - PC 关联手机号+密码登录；3 - PC 邮箱+密码登录；5 - 手机APP扫码授权登录其他终端（PC、TV、PAD、冰箱等）；6-（APP & M & WX & QQ、微信小程序、快应用）账号+密码登录；15-刷脸登录；
        :param appId: (Optional) 接入登录应用Id，仅APP登录时提供，说明接入京东登录的应用标识
        :param mobileBrand: (Optional) 手机品牌，如果手机注册，请带上此信息
        :param appVersion: (Optional) App 客户端版本
        :param mouseClickCount: (Optional) 用户操作过程中鼠标单击次数
        :param keyboardClickCount: (Optional) 用户操作过程中键盘单击次数
        :param referer: (Optional) 用户 HTTP 请求的 referer 值
        :param jumpUrl: (Optional) 登录成功后跳转页面
        :param userAgent: (Optional) 用户 HTTP 请求的 userAgent
        :param xForwardedFor: (Optional) 用户 HTTP 请求中的 x_forward_for
        """

        self.phone = phone
        self.loginIp = loginIp
        self.loginType = loginType
        self.loginName = loginName
        self.channel = channel
        self.deviceName = deviceName
        self.deviceVersion = deviceVersion
        self.deviceOS = deviceOS
        self.deviceOSVersion = deviceOSVersion
        self.loginTime = loginTime
        self.elapsedTime = elapsedTime
        self.loginResult = loginResult
        self.loginEmail = loginEmail
        self.macAddress = macAddress
        self.imei = imei
        self.idfa = idfa
        self.regIp = regIp
        self.eid = eid
        self.regTime = regTime
        self.bizType = bizType
        self.authType = authType
        self.appId = appId
        self.mobileBrand = mobileBrand
        self.appVersion = appVersion
        self.mouseClickCount = mouseClickCount
        self.keyboardClickCount = keyboardClickCount
        self.referer = referer
        self.jumpUrl = jumpUrl
        self.userAgent = userAgent
        self.xForwardedFor = xForwardedFor
