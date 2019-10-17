# 简介 #

[![Build Status](https://travis-ci.com/jdcloud-api/jdcloud-sdk-python.svg?branch=master)](https://travis-ci.com/jdcloud-api/jdcloud-sdk-python)
[![Documentation Status](https://readthedocs.org/projects/jdcloud-sdk-python/badge/?version=latest)](https://jdcloud-sdk-python.readthedocs.io/en/latest/?badge=latest)

欢迎使用京东云开发者Python工具套件（Python SDK）。使用京东云Python SDK，您无需复杂编程就可以访问京东云提供的各种服务。

为了方便您理解SDK中的一些概念和参数的含义，使用SDK前建议您先查看OpenAPI使用入门。要了解每个API的具体参数和含义，请参考程序注释或参考OpenAPI&SDK下具体产品线的API文档。

# 环境准备 #

1. 京东云Python SDK适用于Python 2.7.* 和 3.* 版本。
2. 在开始调用京东云Open API之前，需提前在京东云用户中心账户管理下的AccessKey管理页面申请accesskey和secretKey密钥对（简称AK/SK）。AK/SK信息请妥善保管，如果遗失可能会造成非法用户使用此信息操作您在云上的资源，给你造成数据和财产损失。

# SDK使用方法 #
建议使用pip安装京东云Python SDK，如下所示：

	pip install -U jdcloud_sdk
您还可以下载sdk源代码自行使用。

使用源码安装您可以如下方式执行：

	python setup.py install

SDK使用中的任何问题，欢迎您在[SDK使用问题反馈页面](https://github.com/jdcloud-api/jdcloud-sdk-python/issues)交流。

**注意：京东云并没有提供其他下载方式，请务必使用上述官方下载方式！**

调用SDK
Python SDK的调用主要分为4步：

1. 设置accessKey和secretKey
2. 创建Client（每支云产品都有自己的Client，当调用该产品API时，需使用该产品的Client。例如：使用云主机的VmClient只能调用云主机（Vm）的接口；使用高可用组的AgClient只能调用高可用组（Ag）的接口。）
3. 设置请求参数
4. 执行请求得到响应

以下是查询云主机实例类型的调用示例

```python
# coding=utf-8
from jdcloud_sdk.core.credential import Credential
from jdcloud_sdk.services.vm.client.VmClient import VmClient
from jdcloud_sdk.services.vm.apis.DescribeInstanceTypesRequest \
    import DescribeInstanceTypesParameters, DescribeInstanceTypesRequest

access_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
secret_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
credential = Credential(access_key, secret_key)
client = VmClient(credential)

try:
    parameters = DescribeInstanceTypesParameters('cn-north-1')
    request = DescribeInstanceTypesRequest(parameters)
    resp = client.send(request)
    if resp.error is not None:
        print(resp.error.code, resp.error.message)
    print(resp.result)
except Exception as e:
    print(e)
    # 错误处理
```

如果需要设置额外的header，例如要调用开启了MFA操作保护的接口，需要传递x-jdcloud-security-token，则按照如下方式：
```python
parameters = DeleteInstanceParameters('cn-north-1', 'i-xxx')
header = {'x-jdcloud-security-token': 'xxx'}
request = DeleteInstanceRequest(parameters, header)
```

如果需要设置访问点，配置超时等，请参考如下更复杂的例子：
```
from jdcloud_sdk.core.credential import Credential
from jdcloud_sdk.core.const import SCHEME_HTTP
from jdcloud_sdk.core.config import Config
from jdcloud_sdk.core.logger import Logger
from jdcloud_sdk.services.vm.client.VmClient import VmClient
```
```
credential = Credential(access_key, secret_key)
# 指定使用http方式访问vpc专用域名，超时为20s
config = Config('vm.internal.cn-north-1.jdcloud-api.com', SCHEME_HTTP, 20)
logger = Logger(3) # FATAL = 0 ERROR = 1 WARN = 2 INFO = 3；如果不想输出日志，可将日志级别设置为0（FATAL）；不设置logger，则默认为INFO
client = VmClient(credential, config, logger)
```
更多调用示例参考  [SDK使用Demo](https://github.com/jdcloud-api/jdcloud-sdk-python/tree/master/demo)

# 生成文档

```sh
pip3 install -U sphinx
cd docs && make apidoc && make html
```
