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

JDCLOUD2 = 'JDCLOUD2'
JDCLOUD3 = 'JDCLOUD3'
JDCLOUD_ALGORITHM = 'JDCLOUD2-HMAC-SHA256'
JDCLOUD3_ALGORITHM = 'JDCLOUD3-HMAC-SHA256'
JDCLOUD_REQUEST = 'jdcloud2_request'
JDCLOUD3_REQUEST = 'jdcloud3_request'

JDCLOUD_DATE = 'x-jdcloud-date'
JDCLOUD_SECURITY_TOKEN = 'x-jdcloud-security-token'
JDCLOUD_CONTENT_SHA256 = 'x-jdcloud-content-sha256'
JDCLOUD_NONCE = 'x-jdcloud-nonce'
JDCLOUD_AUTH = 'Authorization'

METHOD_GET = 'GET'
METHOD_PUT = 'PUT'
METHOD_POST = 'POST'
METHOD_PATCH = 'PATCH'
METHOD_DELETE = 'DELETE'
METHOD_HEAD = 'HEAD'

SCHEME_HTTP = 'http'
SCHEME_HTTPS = 'https'

HEADER_REQUESTID = 'x-jdcloud-request-id'
HEADER_CONTENT_LEN = 'Content-Length'
HEADER_JCLOUD_PREFIX = 'x-jcloud'
HEADER_JDCLOUD_PREFIX = 'x-jdcloud'
HEADER_ERROR = ('x-jcloud-pin', 'x-jcloud-erp', 'x-jcloud-security-token')
HEADER_BASE64 = ('x-jdcloud-pin', 'x-jdcloud-erp', 'x-jdcloud-security-token')
