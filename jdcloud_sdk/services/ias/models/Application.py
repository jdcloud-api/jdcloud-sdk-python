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


class Application(object):

    def __init__(self, clientName=None, tokenEndpointAuthMethod=None, grantTypes=None, redirectUris=None, clientUri=None, logoUri=None, tosUri=None, policyUri=None, scope=None, jwksUri=None, jwks=None, contacts=None, extension=None, accessTokenValiditySeconds=None, refreshTokenValiditySeconds=None, multiTenant=None, secret=None, userType=None):
        """
        :param clientName: (Optional) 应用名
        :param tokenEndpointAuthMethod: (Optional) 客户端认证方式<br> - none：不设置客户端密码（不推荐）<br> - client_secret_post：客户端必须设置密码，且该密码需要在OAuth2 Token Endpoint提供于请求的body<br> - client_secret_basic：客户端必须设置密码，且该密码需要在OAuth2 Token Endpoint提供于请求的header<br> 支持以下值：<br> （1）none<br> （2）client_secret_post<br> （3）client_secret_basic
        :param grantTypes: (Optional) 支持的OAuth类型：<br> - authorization_code：OAuth2授权码模式<br> - implicit：OAuth2隐式授权模式<br> - refresh_token：启用刷新令牌 支持以下值：<br> （1）authorization_code<br> （2）authorization_code,refresh_token<br> （3）authorization_code,implicit<br> （4）authorization_code,implicit,refresh_token<br> （5）implicit<br> 注：如果grantTypes指定了refresh_token，应用将可以使用刷新令牌；如果在创建应用时未指定，则应用不能使用刷新令牌；任何时候应用都可以调用“更新应用”接口更改grantTypes设置
        :param redirectUris: (Optional) 回调地址，最多4个，多个url之间用逗号,分隔，每个url长度不超过1000，url不支持#符号
        :param clientUri: (Optional) 应用介绍地址，url不支持#符号
        :param logoUri: (Optional) 应用logo地址，url不支持#符号
        :param tosUri: (Optional) 应用服务协议地址，url不支持#符号
        :param policyUri: (Optional) 应用隐私政策地址，url不支持#符号
        :param scope: (Optional) OAuth scope范围，支持的值为：<br/> （1）openid：用OpenID Connect协议进行身份认证<br/> 指定scope为openid，并在Authorization Endpoint请求该scope，京东云将返回用户的OpenID令牌；如果在创建应用时未指明该值，则应用不能请求OpenID令牌；任何时候应用都可以调用“更新应用”更改该设置
        :param jwksUri: (Optional) JWKS地址，url不支持#符号<br/>jwksUri和jwks传一个即可
        :param jwks: (Optional) JWKS
        :param contacts: (Optional) 应用联系信息
        :param extension: (Optional) 应用扩展信息
        :param accessTokenValiditySeconds: (Optional) 访问令牌有效期，值的范围为 600 秒到 6x3600=21,600 秒，即10分钟-6小时
        :param refreshTokenValiditySeconds: (Optional) 刷新令牌有效期，值的范围为 30x24x3600=2,592,000 秒到 365x24x3600=31,536,000 秒，即30天-365天<br/><br/> 注：当 GrantTypes 包含 refresh_token 时，refreshTokenValiditySeconds 为必传参数
        :param multiTenant: (Optional) 是否为多租户应用<br/> "false"：该应用仅支持当前创建应用的租户访问，其他京东云租户无法访问<br/>        "true"：该应用支持其他京东云租户访问，但当前创建应用的租户不能访问
        :param secret: (Optional) 应用的密码，支持8-255位长度的ASCII可打印字符，建议使用足够复杂的密码策略<br/><br/>        注：当TokenEndpointAuthMethod不等于none时，secret为必传参数；反之，当指定了secret时，TokenEndpointAuthMethod不能等于none<br/>京东云将不可逆加密secret，因此您无法再次从京东云查看该密码，但您可以随时通过更新应用重新设置secret
        :param userType: (Optional) 能访问应用的账号类型，支持以下值：<br/> （1）root：支持主账号访问，子用户无法访问<br/> （2）sub：子用户账号，使用主账号不能访问<br/><br/> 注：multiTenant和userType的组合指定了应用的用户人群，典型的应用场景如：<br/> （1）应用向当前租户下的子用户开放（2）应用向京东云其他租户主账号开放
        """

        self.clientName = clientName
        self.tokenEndpointAuthMethod = tokenEndpointAuthMethod
        self.grantTypes = grantTypes
        self.redirectUris = redirectUris
        self.clientUri = clientUri
        self.logoUri = logoUri
        self.tosUri = tosUri
        self.policyUri = policyUri
        self.scope = scope
        self.jwksUri = jwksUri
        self.jwks = jwks
        self.contacts = contacts
        self.extension = extension
        self.accessTokenValiditySeconds = accessTokenValiditySeconds
        self.refreshTokenValiditySeconds = refreshTokenValiditySeconds
        self.multiTenant = multiTenant
        self.secret = secret
        self.userType = userType
