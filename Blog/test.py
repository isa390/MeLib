
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
from git.repo import Repo
import eventlet
import datetime
import logging
#srcdir = "/tmp/update/book"
#dstdir = "/tmp/blog"
pulldir = "/tmp/blog"

APP_ID = "cli_a15bebebc5b8d00b"
APP_SECRET = "pMJXu20Pn2L2fmFIvwSrZcPmZbRnmotd"
APP_VERIFICATION_TOKEN = "hxaTTQZc9re73RE4bsKaEcCvLxLr1NIY"
ret_card = {
    "version": "1.0",
    "body": [{
        "tag": "text",
        "text": "Select"
    }]
}

def killport(port):
	command='''kill -9 $(netstat -nlp | grep :'''+str(port)+''' | awk '{print $7}' | awk -F"/" '{ print $1 }')'''
	os.system(command)


class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write("ok".encode())
        eventlet.monkey_patch()#必须加这条代码
        with eventlet.Timeout(60,False):#设置超时时间为60秒
          try: 
              repo = Repo(pulldir)  
              repo.git.pull()
          except: 
              create__filea("/tmp/blog/blog/log.txt",e)
              print(e) 
          else:
              create__filea("/tmp/blog/blog/log.txt","pull successfully")
              print("pull successfully") 
              killport(4456)
              print("ok")
          # try:
          #     shutil.rmtree(dstdir)
          # except OSError as e:
          #     print(e)
          # else:
          #     print("The directory is deleted successfully")

          # shutil.move(srcdir, dstdir)
          print("启动新的进程")
          print('没有跳过这条输出')
        print('跳过了输出')
        os.chdir("/tmp/blog/blog")
        subprocess.Popen(['python3', '/tmp/blog/blog/dev.py'])
        return


    def handle_request_url_verify(self, post_obj):
        # 原样返回 challenge 字段内容
        challenge = post_obj.get("challenge", "")
        rsp = {'challenge': challenge}
        self.response(json.dumps(rsp))
        return

    def handle_message(self, event):
        # 此处只处理 text 类型消息，其他类型消息忽略
        msg_type = event.get("msg_type", "")
        if msg_type != "text":
            print("unknown msg_type =", msg_type)
            self.response("")
            return

        # 调用发消息 API 之前，先要获取 API 调用凭证：tenant_access_token
        access_token = self.get_tenant_access_token()
        if access_token == "":
            self.response("")
            return

        # 机器人 echo 收到的消息
        self.send_message(access_token, event.get("open_chat_id"), event.get("text"))
        #self.response("")
        
        self.response(json.dumps(ret_card))
        return

    def response(self, body):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(body.encode())

    def get_tenant_access_token(self):
        url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal/"
        headers = {
            "Content-Type" : "application/json"
        }
        req_body = {
            "app_id": APP_ID,
            "app_secret": APP_SECRET
        }

        data = bytes(json.dumps(req_body), encoding='utf8')
        req = request.Request(url=url, data=data, headers=headers, method='POST')
        try:
            response = request.urlopen(req)
        except Exception as e:
            print(e.read().decode())
            return ""

        rsp_body = response.read().decode('utf-8')
        rsp_dict = json.loads(rsp_body)
        code = rsp_dict.get("code", -1)
        if code != 0:
            print("get tenant_access_token error, code =", code)
            return ""
        return rsp_dict.get("tenant_access_token", "")

    def send_message(self, token, open_id, text):
        url = "https://open.feishu.cn/open-apis/message/v4/send/"

        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + token
        }
        req_body = {
            "chat_id": open_id,
            "msg_type":"interactive",
              "card":{
                "header":{
                  "title":{
                    "tag":"plain_text",
                    "content":"iPad Air 3"
                  }
                },
                "elements":[
                  {
                    "tag":"img",
                    "img_key":"img_2098a60d-8267-4d4c-91a8-d94b2baf90dg",
                    "alt":{
                      "tag":"plain_text",
                      "content":"iPad Air 3"
                    }
                  },
                  {
                    "tag":"div",
                    "text":{
                      "tag":"lark_md",
                      "content":"活动描述：**Apple 出品**\n开奖时间：**2019-12-11 18:00**"
                    }
                  },
                  {
                    "tag":"action",
                    "actions":[
                      {
                        "tag":"button",
                        "text":{
                          "tag":"plain_text",
                          "content":"参加抽奖"
                        },
                        "type":"default"
                      }
                    ]
                  }
                ]
              }
        }

        data = bytes(json.dumps(req_body), encoding='utf8')
        req = request.Request(url=url, data=data, headers=headers, method='POST')
        try:
            response = request.urlopen(req)
        except Exception as e:
            print(e.read().decode())
            return

        rsp_body = response.read().decode('utf-8')
        rsp_dict = json.loads(rsp_body)
        code = rsp_dict.get("code", -1)
        if code != 0:   
            print("send message error, code = ", code, ", msg =", rsp_dict.get("msg", ""))
def create__filea(file_path,msg):
    now = datetime.datetime.now()
    try:
        f=open(file_path,"r+",encoding='utf-8')
    except  Exception as e:
        print(str(e))
        f=open(file_path,"a+",encoding='utf-8')
    content = f.read()
    f.seek(0,0)
    f.write('<br>')
    f.write(""+now.strftime("%Y-%m-%d %H:%M:%S")+":"+msg)
    f.write(content)
    f.close()
    print("save ok")

def run():
    port = 4457
    server_address = ('', port)
    httpd = HTTPServer(server_address, RequestHandler)
    print("test start.....")
    httpd.serve_forever()

if __name__ == '__main__':
    run() 