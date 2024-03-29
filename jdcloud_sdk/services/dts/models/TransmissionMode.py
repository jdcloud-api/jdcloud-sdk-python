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


class TransmissionMode(object):

    def __init__(self, dataInitialization=None, dataSynchronization=None, structureInitialization=None):
        """
        :param dataInitialization: (Optional) 是否执行全量数据传输，取值：true：是，为默认值，false：否
        :param dataSynchronization: (Optional) 是否执行增量数据传输，取值：false：否，为默认值，false：是
        :param structureInitialization: (Optional) 是否执行库表结构初始化，取值：true：是，false：否
        """

        self.dataInitialization = dataInitialization
        self.dataSynchronization = dataSynchronization
        self.structureInitialization = structureInitialization
