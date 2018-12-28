import requests
import json
import time
import re
import random
import models
from models import session
import mytime
comment_url ="http://music.163.com/api/v1/resource/comments/R_SO_4_520458203"
Mname_url = "https://music.163.com/song?id="
proxy_list =[]
header = {
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
"Referer":"http://music.163.com/",
"Content-Type":"application/json",
"Cookie":"_iuqxldmzr_=32; _ntes_nnid=fa970a3e6429f7a1128f6c59fc6dbce6,1545818838892; _ntes_nuid=fa970a3e6429f7a1128f6c59fc6dbce6; __utmc=94650624; WM_NI=AQ9phYuIqUvp85AXUQ%2FCvxu4ctr0ZcLY%2B2KdUmEF07k3mG1JOMC8Mywp8epPFb8ZorRoqwylJP%2BTMaxMLK9WMzSQxGbzmPR%2Fdpp%2F0IMuJMRNHUwc%2BIwFRj0VRKyGO0%2B%2BNkw%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eea4d13caeecfdd8b76bf5ef8eb7d45f969e9aaeb76bedee9cccbc21aaa9988bbc2af0fea7c3b92a838ff791eb53b797bfb6f57cfceb8fb9d85bed9dba99f840a1acbed1d9699087e5d3ca7097b38ba7b33da9eda3a8b4428d938dd9d073b5b0f886f35c86bef8bbee7a92b1bf98fc688a90e5b5d06bbc9384acbc5d8fa69db2fb4da2a6a3b1d125a8b0c0d0b3438fab86aed1468c8bb984aa43b59a9e8bb35e9295b7a8ce3ce9f5828cf637e2a3; WM_TID=0NWFfPd%2BjlRBABEURAc8Lv2S64ui1Gz5; playerid=21689604; __utma=94650624.709259473.1545818839.1545818839.1545873192.2; __utmz=94650624.1545873192.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __remember_me=true; MUSIC_U=72f4c91e0ab8ecfda87a2b70901378d9e338b367896ff5d684ed54d73262c65007d1acd73dfe625fd1452e28c74353fb77749c2dda21047b; __csrf=fa90670026159953729812e679ccddbc; JSESSIONID-WYYY=vioHGttWfvG8UTqoXOrYDZKakoY%2F2YI0%2FHkKRJMFaqJ%5CiVKIpB1jvh%2FIsyODVE2c%2FVawRQ1cHVwJnb%5C7rMWnRMHCsyFMpTFSb8GQhixPbQxYKPvaq%2BHW1uin%5Cr6mI%2BkGvek20DtkzX8sGnW1R14geGPjmvMyfMorf6hej0UpXi588QS1%3A1545878473103",
}
class pachong():
    def __init__(self):
        self.comment_url = "http://music.163.com/api/v1/resource/comments/R_SO_4_"
        self.name_url = "https://music.163.com/song?id="
        self.user_agent_list = [
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
            "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16",
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",]


        self.http_ip_list =[]
        self.https_ip_list = []
        with open("httpsip.txt", "r") as f:
            for line in f:
                self.https_ip_list.append(line.strip())
        with open("httpip.txt", "r") as f:
            for line in f:
                self.http_ip_list.append(line.strip())
        self.header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
            "Referer": "http://music.163.com/",
            "Content-Type": "application/json",
            "Cookie": "_iuqxldmzr_=32; _ntes_nnid=fa970a3e6429f7a1128f6c59fc6dbce6,1545818838892; _ntes_nuid=fa970a3e6429f7a1128f6c59fc6dbce6; __utmc=94650624; WM_NI=AQ9phYuIqUvp85AXUQ%2FCvxu4ctr0ZcLY%2B2KdUmEF07k3mG1JOMC8Mywp8epPFb8ZorRoqwylJP%2BTMaxMLK9WMzSQxGbzmPR%2Fdpp%2F0IMuJMRNHUwc%2BIwFRj0VRKyGO0%2B%2BNkw%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eea4d13caeecfdd8b76bf5ef8eb7d45f969e9aaeb76bedee9cccbc21aaa9988bbc2af0fea7c3b92a838ff791eb53b797bfb6f57cfceb8fb9d85bed9dba99f840a1acbed1d9699087e5d3ca7097b38ba7b33da9eda3a8b4428d938dd9d073b5b0f886f35c86bef8bbee7a92b1bf98fc688a90e5b5d06bbc9384acbc5d8fa69db2fb4da2a6a3b1d125a8b0c0d0b3438fab86aed1468c8bb984aa43b59a9e8bb35e9295b7a8ce3ce9f5828cf637e2a3; WM_TID=0NWFfPd%2BjlRBABEURAc8Lv2S64ui1Gz5; playerid=21689604; __utma=94650624.709259473.1545818839.1545818839.1545873192.2; __utmz=94650624.1545873192.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __remember_me=true; MUSIC_U=72f4c91e0ab8ecfda87a2b70901378d9e338b367896ff5d684ed54d73262c65007d1acd73dfe625fd1452e28c74353fb77749c2dda21047b; __csrf=fa90670026159953729812e679ccddbc; JSESSIONID-WYYY=vioHGttWfvG8UTqoXOrYDZKakoY%2F2YI0%2FHkKRJMFaqJ%5CiVKIpB1jvh%2FIsyODVE2c%2FVawRQ1cHVwJnb%5C7rMWnRMHCsyFMpTFSb8GQhixPbQxYKPvaq%2BHW1uin%5Cr6mI%2BkGvek20DtkzX8sGnW1R14geGPjmvMyfMorf6hej0UpXi588QS1%3A1545878473103",
        }
    def get_name(self,id,proxy = None):
        try:
            html = self.get(url=self.name_url + str(id),proxy=proxy)
            music = re.findall(r'json">(.*?)</script>',html.text,re.S)
            if music is not None:
                music = eval(music[0])
            #print(music,type(music))
            return music
        except:
            return None
    def get_comment(self,id,proxy=None):
        try :
            comment = self.get(url=self.comment_url + str(id), proxy=proxy)
            cms = json.loads(comment.text)["total"]
            return cms
        except:
            return None


    def get(self,url,proxy = None,timeout = 20,num = 500,sleep = 2):
        print("正在请求",url)
        ishttp = url[0:5]
        UA = random.choice(self.user_agent_list)
        self.header["User-Agent"]=UA
        if proxy == None:
            try:
                return requests.get(url,headers = self.header,timeout = timeout)
            except:
                if num>1:
                    time.sleep(sleep)
                    return self.get(url,num = num - 1)
                else:
                    time.sleep(sleep)
                    if ishttp == "http:":
                        IP = "".join(random.choice(self.http_ip_list)).strip()
                        proxy = {"http":IP}
                    elif ishttp == "https":
                        IP = "".join(random.choice(self.https_ip_list)).strip()
                        proxy = {"https": IP}
                    return self.get(url,proxy=proxy,timeout = timeout)
        else:
            try:
                if ishttp == "http:":
                    print("https")
                    IP = "".join(random.choice(self.http_ip_list)).strip()
                    proxy = {"http": IP}
                elif ishttp == "https":
                    print("https")
                    IP = "".join(random.choice(self.https_ip_list)).strip()
                    proxy = {"https": IP}
                return requests.get(url,headers = self.header,proxies = proxy,timeout = timeout)
            except:

                if num >0:
                    time.sleep(sleep)
                    if ishttp == "http:":
                        #self.http_ip_list.remove(IP)
                        IP = "".join(random.choice(self.http_ip_list)).strip()
                        proxy = {"http": IP}
                        print("正在更换代理")
                        print("当前代理：", proxy, IP)
                    elif ishttp == "https":
                        print("https")
                        IP = "".join(random.choice(self.https_ip_list)).strip()
                        proxy = {"https": IP}
                        print("正在更换代理")
                        print("当前代理：", proxy, IP)
                    return self.get(url,proxy = proxy,num = num - 1)
    def music2db(self,id,t = 15):
        comments = self.get_comment(id)
        if comments != 0 or comments is not None:
            mus = self.get_name(id)
            print(mus, comments)
            if mus is not  None:
                desc = mus["description"]
                singer = desc[desc.find("歌手：")+3:desc.find("所属专辑")]
                album = desc[desc.find("所属专辑：")+5:]
                #print(singer,album)
                session.add(
                    models.Music(musicid=mus["@id"], title=mus["title"], image=mus["images"], singer=singer,album = album,
                                 pubdate=mus["pubDate"], comments=comments,creattime = mytime.get_now(),updatetime = mytime.get_now()))
                session.commit()
                print(mus["title"] + "入库成功:id=" ,id)
                time.sleep(t)
                return 1
        else:
            print(id,":评论数为空")
            time.sleep(t-1)
            return 0

if __name__ == "__main__":
    for i in range(100322,999999):
        #id = random.randint(100000,999999)
        pc = pachong()
        isdata = pc.music2db(i,t = 3)
    #html = requests.get(url = "https://music.163.com/song?id=536099160",proxies = {"https":"123.127.93.188:44399"})