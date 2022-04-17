#!/usr/bin/env python
# --coding:utf-8--
import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')
from http.server import BaseHTTPRequestHandler, HTTPServer
from os import path
import json
from urllib import request, parse
import os
import re
import time
import subprocess
import shutil
import datetime
srcdir = ".\\book\\blog"
tempdst = "..\\temp"
pathTest = r"E:\AmesomeCloud\Blog2Me\blog\book"


#dstdir = ".\\yy"
if __name__ == '__main__':
    

    time = datetime.datetime.strftime(datetime.datetime.now(),'%Y-%m-%d %H:%M:%S')
    print(time)
    # shutil.move(srcdir, tempdst)
    # try:
    #     shutil.rmtree(pathTest)
    # except OSError as e:
    #     print(e)
    # else:
    #     print("The directory is deleted successfully")

    # shutil.move(tempdst, srcdir)
    #shutil.copytree(tempdst, dstdir)