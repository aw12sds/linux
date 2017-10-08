#!/usr/bin/env python
import os
import time

    
def judge():
    print("1.statue")
    print("2.install")
    print("3.end")
    print("4.chang page")
    print("5.restart xmapp")
    
    b=input("please input:")
    a=str(b)
    if(a=="1"):
      print("a=1")
      statue()
    elif(a=='2'):
      install()
    elif(a=='4'):
      changpage()
    elif(a=='5'):
      os.system("/opt/lampp/lampp restart")
    else:
      print("end")    
    
def changpage():
    print("1.discuz")
    print("2.php")
    page=input("please input:")
    page1=str(page)
    path=0
    if(page1=="1"):
      path='DocumentRoot "/opt/lampp/htdocs/rd/upload"'
    elif(page1=="2"):
      path='DocumentRoot "/opt/lampp/htdocs"'
    rewrite(path)

def rewrite(path):
    
    f=open('/opt/lampp/etc/httpd.conf','r+')
    flist=f.readlines()
    flist[228]=path+'\n'
    print(path)
    f=open('/opt/lampp/etc/httpd.conf','w+')
    f.writelines(flist)



def install():
    print("1.git")
    os.system("git")
    print("2.shadowsock")
    print("3.serverSpeeder")
    
    print("4.git config")
    print("5.php")
 
    install=str(input("please input:"))
    if(install=="1"):
      os.system("sudo yum install git")
    elif(install=='2'):
      print("a=2")
    elif(install=='3'):  
      print("a=3")
    elif(install=='4'):
      os.system("git config--global user,name 'aw12sds'")
    elif(install=='5'):
      os.system("wget 'https://www.apachefriends.org/xampp-files/7.1.9/xampp-linux-x64-7.1.9-0-installer.run'")
      print("chmod a+x")
      print("run script")
      print("vi /opt/lampp/etc/extra/httpd-xampp.conf")
      print("/opt/lampp/lampp status")

    else:
      print("end")

def shadowsock():
    print("shadowsock")
    
def serverSpeeder():
    print("serverSpeeder")
    
def statue():
    print("*"*40)
    print("1.cpu")
    print("2.firewall")
    print("3.software")
    print("4.return")
    statue=str(input("please input:"))
    if(statue=='1'):
      print("disk-M")
      os.system("df -m")
      print("memory-M")
      os.system("free -m")
      print("cpu number")
      os.system("cat /proc/cpuinfo | grep 'physical id' | uniq | wc -l")
      os.system("cat /proc/cpuinfo | grep 'cpu cores' | uniq")
      os.system("cat /proc/cpuinfo | grep 'model name' |uniq")


    elif(statue=='2'):
      os.system("firewall-cmd --state")
      os.system("/usr/sbin/sestatus -v ")
      
    elif(statue=='3'):
      print("*"*40)
      os.system("python -V")
      os.system("java -version")
      os.system("gcc --version")
      print("*"*40)
      pyversion=input("reinstall py?y/n:")
    elif(statue=='4'):
      judge()


if __name__ == "__main__":

    judge()

