#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2
import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')


if __name__ == "__main__":
    tids = ""
    for tid in range(10000, 10014):
        tids += str(tid)+","
    for tid in range(10019, 10027):
        tids += str(tid)+","
    for tid in range(562, 572):
        tids += str(tid)+","
    tids += "763,847,762,862,753,860,579,848,578,849,577,851,320,850,840,852,841,863,724,858,723,857,722,855,721,854,720,853,842,864,843,865,844,866,845,867,846,868"
         
    myurl = "http://k1256.mzhen.cn:8079/v1/crowd/info?tids="+tids
    result = dict()
    result["status"] = dict()
    result["data"] = list()
    try:
        response = urllib2.urlopen(myurl)
        code = response.getcode()
        if code == 200:
            result["status"]["code"] = code
            result["status"]["msg"] = "success"

        des = response.read()
        des_dict = json.loads(des)
        for key,value in des_dict.items():
            del value['defineType']
            del value['modelType']
            tid_des = dict()
            tid_des["tid"] = des_dict[key]["tid"]
            tid_des["tname"] = des_dict[key]["tname"]
            tid_des["desc"] = des_dict[key]["desc"]
            result["data"].append(tid_des)
        
        print(result["data"][0]["tname"])
        
        fp = open("test.json", "w")
        fp.write("{")
        fp.write('\n\t"status":')
        #fp.write(str(result["status"])+",\n")
        fp.write("{")
        fp.write('"msg":\"'+result["status"]["msg"]+'\", "code":'+str(result["status"]["code"]))
        fp.write("}\n")
        fp.write('\t"data":[\n')
        data_items = result["data"]
        for i in range(len(data_items)):
            fp.write("\t\t{")
            fp.write('"tid": '+str(result["data"][i]["tid"])+",")
            fp.write('"tname": \"' + result["data"][i]["tname"]+"\",")
            fp.write('"desc": \"'+result["data"][i]["desc"])
            fp.write("\"}")
            if i!= len(data_items)-1:
                fp.write(",\n")
        fp.write("]")
        fp.write("\n}")
        fp.close()
    except Exception as e:
        print(str(e))
