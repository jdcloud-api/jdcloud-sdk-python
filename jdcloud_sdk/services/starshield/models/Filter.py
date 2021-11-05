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


class Filter(object):

    def __init__(self, id=None, expression=None, paused=None, description=None, ref=None):
        """
        :param id: (Optional) Filter identifier
        :param expression: (Optional) The filter expression to be used
        :param paused: (Optional) Whether this filter is currently paused
        :param description: (Optional) A note that you can use to describe the purpose of the filter
        :param ref: (Optional) Short reference tag to quickly select related rules.
        """

        self.id = id
        self.expression = expression
        self.paused = paused
        self.description = description
        self.ref = ref
