#!/usr/bin/env python
import os
import time


def judge():
    print("1.wordpress istall")
    os.system("wget https://wordpress.org/latest.tar.gz")
    os.system("tar -xzvf latest.tar.gz wordpress")
    os.system("rm -rf latest.tar.gz")
    print("wordpress download complete")
#先建立config,贴上数据库
#插件设置 
#if ( !defined('ABSPATH') )
#define('ABSPATH', dirname(__FILE__) . '/');
#设置格式 apache用户  ps -ef | grep httpd
#将wordpress用户改为daemon
if __name__ == "__main__":

    judge()
