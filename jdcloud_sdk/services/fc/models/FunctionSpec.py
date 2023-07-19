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


class FunctionSpec(object):

    def __init__(self, functionName, code, runtime, handler, timeout=None, description=None, envs=None, cpu=None, memorySize=None, diskSize=None):
        """
        :param functionName:  服务名称，不可为空，只支持中文、数字、大小写字母、英文下划线“_”及中划线“-”，且不能超过32字符
        :param code:  函数代码
        :param timeout: (Optional) 函数运行的超时时间，单位为秒，默认为60，取值范围为1-900；。函数超过这个时间后会被终止执行。
        :param runtime:  函数运行的语言环境，目前支持nodejs16。
        :param handler:  函数执行的入口，具体格式和语言相关。
        :param description: (Optional) 描述信息，默认为空；允许输入UTF-8编码下的全部字符，不超过256字符。
        :param envs: (Optional) 容器执行的环境变量；如果和使用中的环境变量Key相同，会覆镜像, 不能和镜像环境变量的key相同；</br> 最大50对
        :param cpu: (Optional) vCPU：单位为核，默认选中1，支持选择0.15、0.75、1
        :param memorySize: (Optional) 内存：单位为MB，默认选中1024，与vCPU联动：vCPU选择0.15时，内存仅支持选择0.25* 1024，vCPU选择0.75时，内存仅支持选择1*1024｜
        :param diskSize: (Optional) 硬盘：单位为MB，默认选中0.5*1024，支持选择0.5 * 1024
        """

        self.functionName = functionName
        self.code = code
        self.timeout = timeout
        self.runtime = runtime
        self.handler = handler
        self.description = description
        self.envs = envs
        self.cpu = cpu
        self.memorySize = memorySize
        self.diskSize = diskSize