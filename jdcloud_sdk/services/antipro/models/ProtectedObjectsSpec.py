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


class ProtectedObjectsSpec(object):

    def __init__(self, eip, cps, ccs, ):
        """
        :param eip:  是否防护弹性公网 IP
        :param cps:  是否防护云物理服务器公网 IP
        :param ccs:  是否防护托管区公网 IP
        """

        self.eip = eip
        self.cps = cps
        self.ccs = ccs
