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

import sys
import base64

if sys.version_info.major == 2:
    from urllib import quote
elif sys.version_info.major == 3:
    from urllib.parse import quote


# base64 encode
def base64encode(value):
    if sys.version_info.major == 2:
        return base64.b64encode(value)
    elif sys.version_info.major == 3:
        encoded_value = base64.b64encode(value.encode('utf-8'))
        return str(encoded_value, 'utf-8')


# byte to string
def byte_to_str(string):
    if sys.version_info.major == 2:
        return string
    elif sys.version_info.major == 3:
        return str(string, 'utf-8')
