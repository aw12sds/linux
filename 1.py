#!/usr/bin/env python
import os


    
def judge():
    print("1.statue")
    print("2.install")
    print("3.end")
    
    b=input("please input:")
    a=str(b)
    if(a=="1"):
      print("a=1")
      statue()
    elif(a=='2'):
      install()
    else:
      print("end")    
    
def install():
    print("1.git")
    os.system("git")
    print("2.shadowsock")
    print("3.serverSpeeder")
    print("4.git config") 
    install=str(input("please input:"))
    if(install=="1"):
      os.system("sudo yum install git")
    elif(install=='2'):
      print("a=2")
    elif(install=='3'):  
      print("a=3")
    elif(install=='4'):
      os.system("git config--global user,name 'aw12sds'")

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
      os.system("java -V")
      os.system("gcc")
      print("*"*40)
      pyversion=input("reinstall py?y/n:")
    elif(statue=='4'):
      judge()


if __name__ == "__main__":

    judge()

