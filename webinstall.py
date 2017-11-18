#!/usr/bin/env python
import os
import time


def judge():
    print("1.wordpress istall")
    os.system("wget https://wordpress.org/latest.tar.gz")
    os.system("tar -xzvf latest.tar.gz wordpress")
    os.system("rm -rf latest.tar.gz")
    print("wordpress download complete")

if __name__ == "__main__":

    judge()
