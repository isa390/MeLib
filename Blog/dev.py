#!/usr/bin/env python
# --coding:utf-8--

from http.server import BaseHTTPRequestHandler, HTTPServer
from os import path
import json
from urllib import request, parse
import requests
import cgi
import os
import subprocess
from pip._internal import main
import datetime

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
paths = [
"buildthisworld",
"contact",
"zouze",
"piyue",
"onehour",
"feilong",
"outputk",
"topic_1",
"topic_2",
"topic_3",
"topic_4",
"topic_5",
"topic_6",
"topic_7",
"topic_8",
"topic_9",
"topic_10",
"topic_11",
"topic_12",
"topic_13",
"topic_14",
"topic_15",
"topic_16",
"topic_17",
"topic_18",
"topic_19",
"topic_20",
"topic_21",
"topic_22",
"topic_23",
"topic_24",
"topic_25",
"topic_26",
"topic_27",
"topic_28",
"topic_29",
"topic_30",
"topic_31",
"topic_32",
"topic_33",
"topic_34",
"topic_35",
"topic_36",
"topic_37",
"topic_38",
"topic_39",
"topic_40",
"topic_41",
"topic_42",
"topic_43",
"topic_44",
"people_01",
"people_02",
"people_03",
"people_04",
"people_05",
"people_06",
"people_07",
"people_08",
"thing_01",
"thing_02",
"thing_03",
"thing_04",
"thing_05",
"thing_06",
"thing_07",
"thing_08",
"thing_09",
"thing_10",
"factory_01",
"factory_02",
"factory_03",
"factory_04",
"factory_05",
"factory_06",
"factory_07",
"factory_08",
"factory_09",
"lifekiller_01",
"direction_01",
"direction_02",
"direction_03",
"direction_04",
"direction_05",
"direction_06",
"direction_07",
"direction_08",
"direction_09",
"direction_10",
"direction_11",
"developanel_01",
"developanel_02",
"developanel_03",
"developanel_04",
"developanel_05",
"developanel_06",
"developanel_07",
"developanel_08",
"developanel_09",
"developanel_10",
"developanel_11",
"developanel_12",
"developanel_13",
"developanel_14",
"daoyichun_01",
"daoyichun_02",
"daoyichun_03",
"daoyichun_04",
"daoyichun_05",
"daoyichun_06",
"daoyichun_07",
"daoyichun_08",
"log",
"thingcase_01",
"thingcase_02",
"thingcase_03",
"thingcase_04",
"thingcase_05",
"thingcase_06",
"thingcase_07",
"thingcase_08",
"thingcase_09",
"thingcase_10",
"thingcase_11",
"thingcase_12",
"templething_01",
"aroundview_01",
"government_02",
"government_03",
"government_04",
"government_05",
"government_06",
"government_07",
"government_08",
"government_09",
"government_10",
"government_11",
"government_12",
"government_13",
"government_14",
"government_15",
"government_16",
"viewtoview_01",
"viewtoview_02",
"viewtoview_03",
"viewtoview_04",
"viewtoview_05",
"viewtoview_06",
"viewtoview_07",
"viewtoview_08",
"viewtoview_09",
"viewtoview_10",
"viewtoview_11",
"viewtoview_12",
"viewtoview_13",
"viewtoview_14",
"debugtheworld_01",
"debugtheworld_02",
"debugtheworld_03",
"debugtheworld_04",
"debugtheworld_05",
"debugtheworld_06",
"debugtheworld_07",
"debugtheworld_08",
"debugtheworld_09",
"debugtheworld_10",
"cvtheworld_01",
"cvtheworld_02",
"kelermodel_01",
"kelermodel_02",
"kelermodel_03",
"kelermodel_04",
"kelermodel_05",
"kelermodel_06",
"kelermodel_07",
"kelermodel_08",
"kelermodel_09",
"techview_01",
"worldview_01",
"worldview_02",
"worldview_03",
"worldview_04",
"newtopics_01",
"newtopics_02",
"newtopics_03",
"newtopics_04",
"newtopics_05",
"newtopics_06",
"formulaCommunity_01",
"formulaCommunity_02",
"formulaCommunity_03",
"formulaCommunity_04",
"formulaCommunity_05",
"formulaCommunity_06",
"formulaCommunity_07",
"formulaCommunity_08",
"formulaCommunity_09",
"RevolutionaryArmy_01",
"RevolutionaryArmy_02",
"RevolutionaryArmy_03",
"RevolutionaryArmy_04",
"XueFuTang_01",
"XueFuTang_02",
"XueFuTang_03",
"XueFuTang_04",
"XueFuTang_05",
"XueFuTang_06",
"XueFuTang_07",
"XueFuTang_08",
"XueFuTang_09",
"XueFuTang_10",
"XueFuTang_11",
"XueFuTang_12",
"BalanceStatus_01",
"BalanceStatus_02",
"BalanceStatus_03",
"BalanceStatus_04",
"BalanceStatus_05",
"BalanceStatus_06",
"BalanceStatus_07",
"BalanceStatus_08",
"BalanceStatus_09",
"BalanceStatus_10",
"BalanceStatus_11",
"BalanceStatus_12",
"ReadTheModel_01",
"ReadTheModel_02",
"ReadTheModel_03",
"ReadTheModel_04",
"ReadTheModel_05",
"ReadTheModel_06",
"ReadTheModel_07",
"ReadTheModel_08",
"ReadTheModel_09",
"ReadTheModel_10",
"MakeItDie_01",
"MakeItDie_02",
"MakeItDie_03",
"MakeItDie_04",
"MakeItDie_05",
"MakeItDie_06",
"OneMinutes_01",
"OneMinutes_02",
"OneMinutes_03",
"OneMinutes_04",
"OneMinutes_05",
"OneMinutes_06",
"OneMinutes_07",
"OneMinutes_08",
"OneMinutes_09",
"TakeThePhoto_01",
"TakeThePhoto_02",
"TakeThePhoto_03",
"TakeThePhoto_04",
"TakeThePhoto_05",
"TakeThePhoto_06",
"TakeThePhoto_07",
"TakeThePhoto_08",
"TakeThePhoto_09",
"TakeThePhoto_10",
"TakeThePhoto_11",
"TakeThePhoto_12",
"TakeThePhoto_13",
"TakeThePhoto_14",
"TakeThePhoto_15",
"TwoWorldRun_01_01",
"TwoWorldRun_01_02",
"TwoWorldRun_01_03",
"TwoWorldRun_01_04",
"TwoWorldRun_01_05",
"TwoWorldRun_01_06",
"TwoWorldRun_01_07",
"TwoWorldRun_01_08",
"TwoWorldRun_02_01",
"TwoWorldRun_02_02",
"TwoWorldRun_02_03",
"TwoWorldRun_02_04",
"TwoWorldRun_02_05",
"TwoWorldRun_02_06",
"TwoWorldRun_02_07",
"TwoWorldRun_02_08",
"TwoWorldRun_03_01",
"TwoWorldRun_03_02",
"TwoWorldRun_03_03",
"TwoWorldRun_03_04",
"TwoWorldRun_03_05",
"TwoWorldRun_03_06",
"TwoWorldRun_03_07",
"TwoWorldRun_03_08",
"TwoWorldRun_04_01",
"TwoWorldRun_04_02",
"TwoWorldRun_04_03",
"TwoWorldRun_04_04",
"TwoWorldRun_04_05",
"TwoWorldRun_04_06",
"TwoWorldRun_04_07",
"TwoWorldRun_04_08",
"TwoWorldRun_05_01",
"TwoWorldRun_05_02",
"TwoWorldRun_05_03",
"TwoWorldRun_05_04",
"TwoWorldRun_05_05",
"TwoWorldRun_05_06",
"TwoWorldRun_05_07",
"TwoWorldRun_05_08",
"TwoWorldRun_06_01",
"TwoWorldRun_06_02",
"TwoWorldRun_06_03",
"TwoWorldRun_06_04",
"TwoWorldRun_06_05",
"TwoWorldRun_06_06",
"TwoWorldRun_06_07",
"TwoWorldRun_06_08",
"TwoWorldRun_07_01",
"TwoWorldRun_07_02",
"TwoWorldRun_07_03",
"TwoWorldRun_07_04",
"TwoWorldRun_07_05",
"TwoWorldRun_07_06",
"TwoWorldRun_07_07",
"TwoWorldRun_07_08",
"TwoWorldRun_08_01",
"TwoWorldRun_08_02",
"TwoWorldRun_08_03",
"TwoWorldRun_08_04",
"TwoWorldRun_08_05",
"TwoWorldRun_08_06",
"TwoWorldRun_08_07",
"TwoWorldRun_08_08",
"BadCaseYou_01",
"BadCaseYou_02",
"BadCaseYou_03",
"BadCaseYou_04",
"BadCaseYou_05",
"BadCaseYou_06",
"RecoveryWorld_01",
"RecoveryWorld_02",
"RecoveryWorld_03",
"RecoveryWorld_04",
"RecoveryWorld_05",
"RecoveryWorld_06",
"RecoveryWorld_07",
"RecoveryWorld_08",
"SkyWorld_01",
"SkyWorld_02",
"SkyWorld_03",
"SkyWorld_04",
"SkyWorld_05",
"SkyWorld_06",
"philosophicalView_01",
"philosophicalView_02",
"philosophicalView_03",
"philosophicalView_04",
"philosophicalView_05",
"philosophicalView_06",
"PersonalStyle_01",
"PersonalStyle_02",
"PersonalStyle_03",
"PersonalStyle_04",
"PersonalStyle_05",
"PersonalStyle_06",
"AnatomyRoom_01_01",
"AnatomyRoom_01_02",
"AnatomyRoom_02_01",
"AnatomyRoom_02_02",
"CompanyOperation_01_01",
"CompanyOperation_02_01",
"CompanyOperation_03_01",
"CompanyOperation_04_01",
"DigitalTribe_01_01",
"DigitalTribe_01_02",
"DigitalTribe_02_01",
"DigitalTribe_03_01",
"DigitalTribe_04_01",
"WindChaser_01",
"WindChaser_02",
"WindChaser_03",
"WindChaser_04",
"WindChaser_05",
"WindChaser_06",
"WindChaser_07",
"WindChaser_08",
"FromHere_01",
"FromHere_02_01",
"FromHere_02_02",
"FromHere_02_03",
"FromHere_02_04",
"FromHere_03",
"FromHere_04",
"MonitoringStatus_01",
"MonitoringStatus_02",
"MonitoringStatus_03",
"MonitoringStatus_04",
"FluidThinking_01",
"FluidThinking_02",
"FluidThinking_03",
"FluidThinking_04",
"SandTower_01",
"SandTower_02",
"SandTower_03",
"SandTower_04",
"accelerator_01",
"accelerator_02",
"OutAndIn_01",
"OutAndIn_02",
"TenStepLearningMethod_01",
"TenStepLearningMethod_02",
"TenStepLearningMethod_03",
"TenStepLearningMethod_04",
"TenStepLearningMethod_05",
"TenStepLearningMethod_06",
"TenStepLearningMethod_07",
"TenStepLearningMethod_08",
"TenStepLearningMethod_09",
"TenStepLearningMethod_10",
"ContinuousLearning_01",
"ContinuousLearning_02",
"ContinuousLearning_03",
"ContinuousLearning_04",
"CycleDay_01",
"CycleDay_02",
"CycleDay_03",
"CycleDay_04",
"CycleDay_05",
"CycleDay_06",
"CycleDay_07",
"CycleDay_08",
"CycleDay_09",
"CycleDay_10",
"Talk2Outside_01",
"Talk2Outside_02",
"When2How_01",
"RssMyData_01",
"See20Years_01",
"See20Years_02",
"See20Years_03",
"See20Years_04",
"See20Years_05",
"See20Years_06",
"StayLean_01",
"StayLean_02",
"StayLean_03",
"StayLean_04",
"StayLean_05",
"StayLean_06",
"InformationProcessingCenter_01",
"InformationProcessingCenter_02",
"InformationProcessingCenter_03",
"InformationProcessingCenter_04",
"ExpKnowledgeContainer_01",
"ExpKnowledgeContainer_02",
"ExpKnowledgeContainer_03",
"ExpKnowledgeContainer_04",
"ExpKnowledgeContainer_05",
"ExpKnowledgeContainer_06",
"ExpKnowledgeContainer_07",
"ExpKnowledgeContainer_08",
"SoulAsks_01",
"SoulAsks_02",
"SoulAsks_03",
"SoulAsks_04",
"SoulAsks_05",
"SoulAsks_06",
"SoulAsks_07",
"SoulAsks_08",
"SoulAsks_09",
"SoulAsks_10",
"ConsFight_01",
"ConsFight_02",
"ConsFight_03",
"ConsFight_04",
"DictionaryPhrase_01",
"DictionaryPhrase_02",
"DictionaryPhrase_03",
"DictionaryPhrase_04",
"DictionaryPhrase_05",
"DictionaryPhrase_06",
"techsource_01",
"RepublicRevolution_01",
"RepublicRevolution_02",
"RepublicRevolution_03",
"RepublicRevolution_04",
"RankLearner_01",
"RankLearner_02",
"RankLearner_03",
"RankLearner_04",
"RankLearner_05",
"RankLearner_06",
"RankLearner_07",
"RankLearner_08",
"RankLearner_09",
"RankLearner_10",
"RankLearner_11",
"RankLearner_12",
"RankLearner_13",
"RankLearner_14",
"LawTough_01",
"LawTough_02",
"LawTough_03",
"LawTough_04",
"LawTough_05",
"LawTough_06",
"EcoNatureTicle_01",
"EcoNatureTicle_02",
"EcoNatureTicle_03",
"EcoNatureTicle_04",
"EcoNatureTicle_05",
"EcoNatureTicle_06",
"SixHats",
"FishBone",
"SWOT",
"NewAndDif_01",
"NewAndDif_02",
"NewAndDif_03",
"NewAndDif_04",
"NewAndDif_05",
"NewAndDif_06",
"NewAndDif_07",
"NewAndDif_08",
"PhicalSchools_01",
"PhicalSchools_02",
"PhicalSchools_03",
"PhicalSchools_04",
"PhicalSchools_05",
"PhicalSchools_06",
"PhicalSchools_07",
"PhicalSchools_08",
"PhicalSchools_09",
"PhicalSchools_10",
"PhicalSchools_11",
"PhicalSchools_12",
"PhicalSchools_13",
"PhicalSchools_14",
"PhicalSchools_15",
"PhicalSchools_16",
"PhicalSchools_17",
"PhicalSchools_18",
"PhicalSchools_19",
"PhicalSchools_20",
"PhicalSchools_21",
"PhicalSchools_22",
"PhicalSchools_23",
"PhicalSchools_24",
"PhicalSchools_25",
"PhicalSchools_26",
"PhicalSchools_27",
"PhicalSchools_28",
"PhicalSchools_29",
"PhicalSchools_30",
"ArtSpaces_01",
"ArtSpaces_02",
"ArtSpaces_03",
"ArtSpaces_04",
"ArtSpaces_05",
"ArtSpaces_06",
"ArtSpaces_07",
"ArtSpaces_08",
"ArtSpaces_09",
"ArtSpaces_10",
"ArtSpaces_11",
"ArtSpaces_12",
"Reschedule_01",
"Reschedule_02",
"Reschedule_03",
"Reschedule_04",
"Reschedule_05",
"Reschedule_06",
"OKR",
"KPI",
"PowerD",
"TargetSystem",
"TargetSystem_01",
"TargetSystem_02",
"LifeMatrix_01",
"LifeMatrix_02",
"LifeMatrix_03",
"LifeMatrix_04",
"LifeMatrix_05",
"LifeMatrix_06",
"LifeMatrix_07",
"LifeMatrix_08",
"LifeMatrix_09",
"LifeMatrix_10",
"LifeMatrix_11",
"LifeMatrix_12",
"LifeMatrix_13",
"LifeMatrix_14",
"LifeMatrix_15",
"LifeMatrix_16",
"LifeMatrix_17",
"LifeMatrix_18",
"LifeMatrix_19",
"LifeMatrix_20",
"DeepWork_01",
"DeepWork_02",
"DeepWork_03",
"DeepWork_04",
"DeepWork_05",
"DeepWork_06",
"DeepWork_07",
"DeepWork_08",
"DeepWork_09",
"DeepWork_10",
"DeepWork_11",
"DeepWork_12",
"DeepWork_13",
"DeepWork_14",
"MakeItChange_01",
"MakeItChange_02",
"MakeItChange_03",
"MakeItChange_04",
"MakeItChange_05",
"MakeItChange_06",
"MakeItChange_07",
"MakeItChange_08",
"MakeItChange_09",
"MakeItChange_10",
"VirtualPolarization_01",
"VirtualPolarization_02",
"VirtualPolarization_03",
"VirtualPolarization_04",
"VirtualPolarization_05",
"VirtualPolarization_06",
"VirtualPolarization_07",
"VirtualPolarization_08",
"VirtualPolarization_09",
"VirtualPolarization_10",
"TransactionDelegation_01",
"TransactionDelegation_02",
"TransactionDelegation_03",
"TransactionDelegation_04",
"DecisionMakeNew_01",
"DecisionMakeNew_02",
"DecisionMakeNew_03",
"DecisionMakeNew_04",
"DecisionMakeNew_05",
"DecisionMakeNew_06",
"DecisionMakeNew_07",
"DecisionMakeNew_08",
"水水水水水水水",
"水水水水水水水",
]
class RequestHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        try:
            ctype, pdict = cgi.parse_header(self.headers['update'])
            print("ddd ")
            if ctype == 'cv':
                self.wfile.write("cv".encode())
                req_body = self.rfile.read(int(self.headers['content-length']))
                obj = req_body.decode("utf-8")
                print(obj)
                return
            if ctype == 'cache':
                self.wfile.write("cache".encode())
                print("ok")
                req_body = self.rfile.read(int(self.headers['content-length']))
                obj = req_body.decode("utf-8")
                print(obj)
                try:
                    #create__filea(os.getcwd()+"/blog/cv.txt",obj)
                    create__filea("/tmp/blog/blog/cv.txt",obj)
                except:
                    print("ok")
                #create__filea("/tmp/blog/blog/cv.txt",obj)
                return
            elif ctype == 'talk':
                self.wfile.write("talk".encode())
                print("ok")
                req_body = self.rfile.read(int(self.headers['content-length']))
                obj = req_body.decode("utf-8")
                print(obj)
                try:
                    #create__filea(os.getcwd()+"/blog/cv.txt",obj)
                    create__filea("/tmp/blog/blog/talk.txt",obj)
                except:
                    print("ok")
                #create__filea("/tmp/blog/blog/cv.txt",obj)
                #print(os.getcwd()+'\blog\cv.md')
                return
            elif ctype == 'gettalk':
                print("gettalk")
                f = open("/tmp/blog/blog/talk.txt","rb")
                #self.wfile.write(f.read())
                self.wfile.write(getNumStr(bytes2str(f),"<br>",40).encode())
                print("javascript")
                f.close()
                return
            elif ctype == 'beifen':
                self.wfile.write("beifen".encode())
                print("beifen")
                req_body = self.rfile.read(int(self.headers['content-length']))
                obj = req_body.decode("utf-8")
                print(obj)
                try:
                    #create__filea("E:\AmesomeCloud\Blog2Me"+"\\blog\\beifen.txt",obj)
                    create__filea("/tmp/blog/blog/save.txt",obj)
                except Exception as e:
                    print(str(e))
                return
            elif ctype == 'getbeifen':
                print("getbeifen")
                #f = open("E:\AmesomeCloud\Blog2Me"+"\\blog\\beifen.txt","rb")
                f = open("/tmp/blog/blog/save.txt","rb")
                self.wfile.write(f.read())
                #self.wfile.write(getNumStr(bytes2str(f),"<br>",40).encode())
                f.close()
                return
            elif ctype == 'buildme':
                self.wfile.write("buildme".encode())
                print("buildme")
                req_body = self.rfile.read(int(self.headers['content-length']))
                obj = req_body.decode("utf-8")
                print(obj)
                try:
                    #create__filea("E:\AmesomeCloud\Blog2Me"+"\\blog\\buildme.txt",obj)
                    create__filea("/tmp/blog/blog/buildthisman.txt",obj)
                except Exception as e:
                    print(str(e))
                return
            elif ctype == 'getbuildme':
                print("getbuildme")
                #f = open("E:\AmesomeCloud\Blog2Me"+"\\blog\\buildme.txt","rb")
                f = open("/tmp/blog/blog/buildthisman.txt","rb")
                self.wfile.write(f.read())
                #self.wfile.write(getNumStr(bytes2str(f),"<br>",40).encode())
                f.close()
                return
            # elif ctype == 'buildthisworld':
            #     self.wfile.write("buildthisworld".encode())
            #     print("buildthisworld")
            #     req_body = self.rfile.read(int(self.headers['content-length']))
            #     obj = req_body.decode("utf-8")
            #     print(obj)
            #     try:
            #         #create__filea("E:\AmesomeCloud\Blog2Me"+"\\blog\\buildme.txt",obj)
            #         create__filea("/tmp/blog/blog/buildthisworld.txt",obj)
            #     except Exception as e:
            #         print(str(e))
            #     return
            # elif ctype == 'get'+'buildthisworld':
            #     print("getbuildthisworld")
            #     #f = open("E:\AmesomeCloud\Blog2Me"+"\\blog\\buildme.txt","rb")
            #     f = open("/tmp/blog/blog/buildthisworld.txt","rb")
            #     self.wfile.write(f.read())
            #     #self.wfile.write(getNumStr(bytes2str(f),"<br>",40).encode())
            #     f.close()
            #     return
            elif ctype.split("/")[0] == 'update':
                self.wfile.write("update".encode())
                print(ctype.split("/")[1])
                main(['install', ctype.split("/")[1]])
                return
            else:
                if(dealPost(self,ctype)):
                    return
        except:
            print("update notok")
        try:
            ctype, pdict = cgi.parse_header(self.headers['x-github-event'])
            print(ctype.split("/")[0])
            
            self.wfile.write("x-github-event".encode())
            if ctype.split("/")[0] == 'ping':
                print("ping")
                return
        except:
            print("ok")
        
        self.wfile.write("somekey".encode())
        url = 'http://127.0.0.1:4457'
        myobj = {'somekey': 'somevalue'}
        x = requests.post(url, data = myobj)
        return
  
    def do_GET(self):
        filepath = self.path
        if( self.path.endswith(".html")):
            f = open(filepath[1:],"r",encoding='utf-8')
            html = f.read()
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.send_header('Set-Cookie', 'monster=1')
            self.end_headers()
            self.wfile.write(html.encode())
            f.close()
        elif self.path.endswith(".css"):
            print("enter css")
            f = open(filepath[1:],"rb")
            self.send_response(200)
            self.send_header('Content-type', 'text/css')
            self.end_headers()
            self.wfile.write(f.read())
            print("css")
            f.close()
        elif self.path.endswith(".js"):
            print("enter css")
            f = open(filepath[1:],"rb")
            self.send_response(200)
            self.send_header('Content-type', 'text/javascript')
            self.end_headers()
            self.wfile.write(f.read())
            print("javascript")
            f.close()
        elif self.path.endswith(".txt"):
            print("enter txt")
            f = open(filepath[1:],"rb")
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(f.read())
            print("javascript")
            f.close()
        else :
            print("enter picture")
            filename = self.path.split('/')[-1]
            (name, suffix) = filename.split('.')
            print(suffix)
            imgMime = ""
            if(suffix == "jpg" or suffix == "jpeg"):
                imgMime = 'image/jpeg'
            elif(suffix == "png"):
                imgMime = 'image/png'
            f = open(filepath[1:],"rb")
            self.send_response(200)
            self.send_header('Content-type', imgMime)
            self.end_headers()
            self.wfile.write(f.read())
            print("picture")
            f.close()
        # else:
        #     f = open(filepath[1:],"rb")
        #     html = f.read()
        #     self.wfile.write(html)
        #     f.close()
        #self.wfile.write(html.encode())
        return
def run():
    port = 4456
    server_address = ('', port)
    httpd = HTTPServer(server_address, RequestHandler)
    print("dev start.....")
    httpd.serve_forever()
#创建文件
#file_path：文件路径
#msg：即要写入的内容
def bytes2str(filebytes):
    str = filebytes.read().decode("utf-8")
    return str

def dealPost(self,ctype):
    for path in paths:
        if(ctype == path):
            self.wfile.write(path.encode())
            print(path)
            req_body = self.rfile.read(int(self.headers['content-length']))
            obj = req_body.decode("utf-8")
            print(obj)
            try:
                #create__filea("E:\AmesomeCloud\Blog2Me"+"\\blog\\buildme.txt",obj)
                create__filea("/tmp/blog/blog/"+path+".txt",obj)
            except Exception as e:
                print(str(e))
            return True
        elif(ctype == 'get'+path):
            print(ctype)
            #f = open("E:\AmesomeCloud\Blog2Me"+"\\blog\\buildme.txt","rb")
            f = open("/tmp/blog/blog/"+path+".txt","rb")
            self.wfile.write(f.read())
            #self.wfile.write(getNumStr(bytes2str(f),"<br>",40).encode())
            f.close()
            return True
    return False
def getNumStr(strcontent,flag,number):
    strs = strcontent.split(flag,number)
    print(len(strs))
    if(number <= len(strs)):
        temp =""
        for i,value in enumerate(strs):
            if(i < number):
                temp += value + "<br>";
            else:
                break
        return temp
    else:
        return strcontent

def create__file(file_path,msg):
    f=open(file_path,"w",encoding='utf-8')
    f.seek(0,0)
    f.write(msg)
    f.close()
def create__filea(file_path,msg):
    try:
        f=open(file_path,"r+",encoding='utf-8')
    except  Exception as e:
        print(str(e))
        f=open(file_path,"a+",encoding='utf-8')
    content = f.read()
    f.seek(0,0)
    f.write('<br>')
    f.write(msg)
    f.write(content)
    f.close()
    print("save ok")
if __name__ == '__main__':
    run()