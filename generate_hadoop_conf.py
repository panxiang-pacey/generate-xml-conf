# -*- coding: UTF-8 -*-

import os
from ini_to_xml import fun_generate_xml
from parse_ini_conf import fun_get_configuration


def fun_edit_sync(v_user_name,v_file_name,v_conf_dir):
    #LOCAL_CONF_DIR='E:\MyProjects\Python\generate-xml-conf\local_conf'
    base_dir = os.path.dirname(__file__)

    #修改yarn-site.xml配置文件
    file_path = os.path.join(base_dir,'local_conf',v_file_name)
    #print(file_path)
    fun_generate_xml(file_path)

    #分发配置文件
    list_hosts = fun_get_configuration('cluster_hosts')
    #print(list_hosts)
    for host in list_hosts:
        #os.system(cmd)返回值是脚本的退出状态码0(成功)
        #cmd = 'scp -r {0} {1}:/{2}'.format(file_path,'hadoop@192.168.127.11',HADOOP_CONF_DIR)
        cmd = 'scp -r {0} {1}@{2}:{3}'.format(file_path, v_user_name,host[1], v_conf_dir)
        #print(cmd)
        exit_code = os.system(cmd)
        #print(exit_code)
        if exit_code==0:
            print('分发{0}配置文件到{1}成功！'.format(v_file_name,host[1]))
        else:
            print('分发{0}配置文件到{1}出现错误！')


if __name__ == '__main__':

    #scp -r /opt/hadoop-2.5.1/etc/hadoop/* hadoop@node2:/opt/hadoop-2.5.1/etc/hadoop/

    list_user_conf_file = fun_get_configuration('user_conf_file')
    for conf_file in list_user_conf_file:
        list_user_file_path = conf_file[1].split(':')
        user = list_user_file_path[0]
        (filepath, filename) = os.path.split(list_user_file_path[1])
        fun_edit_sync(user, filename, filepath)




