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


class MigrateConfig(object):

    def __init__(self, srcType, srcUrl, srcPwd, tgtType, tgtUrl, tgtPwd, name=None, srcVersion=None, srcTopo=None, exExpTimeInMin=None, proxyNum=None):
        """
        :param name: (Optional) 迁移任务名
        :param srcType:  源端类型，可选：jimdb表示jimdb；jcloud表示京东云redis；native_standalone表示原生redis standalone；native_cluster表示原生redis cluster
        :param srcUrl:  源端统一访问地址，jimdb形如jim://234234234423/3423；京东云redis、原生redis形如host:port，port默认为6379
        :param srcVersion: (Optional) 源端版本，可选：2.8、3.0、3.2、4.0、5.0、6.0、6.2，目前只支持2.8、3.0、4.0
        :param srcTopo: (Optional) 源端拓扑，原生cluster必须输入，其他类型不需要
        :param srcPwd:  源端连接密码
        :param tgtType:  目的端类型，暂不支持jimdb，可选：jcloud，native_standalone
        :param tgtUrl:  目的端统一访问地址，形如host:port，port默认为6379
        :param tgtPwd:  目的端连接密码
        :param exExpTimeInMin: (Optional) 过期时间（单位分钟），可选，0表示默认值
        :param proxyNum: (Optional) 代理个数，可选，默认的1分片为2个，n分片为n个
        """

        self.name = name
        self.srcType = srcType
        self.srcUrl = srcUrl
        self.srcVersion = srcVersion
        self.srcTopo = srcTopo
        self.srcPwd = srcPwd
        self.tgtType = tgtType
        self.tgtUrl = tgtUrl
        self.tgtPwd = tgtPwd
        self.exExpTimeInMin = exExpTimeInMin
        self.proxyNum = proxyNum
