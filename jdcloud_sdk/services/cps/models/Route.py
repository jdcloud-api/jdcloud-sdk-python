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


class Route(object):

    def __init__(self, destinationCidr=None, nextHopType=None, nextHop=None):
        """
        :param destinationCidr: (Optional) 目标网段
        :param nextHopType: (Optional) 下一跳类型
        :param nextHop: (Optional) 下一跳
        """

        self.destinationCidr = destinationCidr
        self.nextHopType = nextHopType
        self.nextHop = nextHop
