# -*- coding: UTF-8 -*-

import os
import configparser


#解决ConfigParser大小写字符自动转换
#类继承重写optionxform函数
#optionxform函数自动转换为小写字母，所以需要对optionxform函数进行重写
class MyConfig(configparser.ConfigParser):
    def __init__(self,defaults=None):
        configparser.ConfigParser.__init__(self,defaults=None)
    def optionxform(self, optionstr):
        return optionstr




def fun_get_configuration(v_section):
    try:
        base_dir = os.path.dirname(__file__)
        file_path = os.path.join(base_dir, 'hadoop_conf.ini')
        #print('配置文件路径：', file_path)

        #config = configparser.ConfigParser()
        config = MyConfig() #类继承重写optionxform函数 解决ConfigParser大小写字符自动转换
        config.read(file_path, encoding='UTF-8')  #不触发异常

        if v_section in config:  ## 判断配置文件中是否存在
            list_configuration = config.items(v_section)   #会将配置文件的大写字母转换为小写字母   键不区分大小写
            return list_configuration
        else:
            print('未找到配置文件或配置文件中不存在')

    except Exception as err:
        print(err)


if __name__ == '__main__':
    print(fun_get_configuration('core-site'))