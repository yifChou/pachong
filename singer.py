import requests
import json
import time
import re
import random
import moduelsinger
import models
import deractor_py
from moduelsinger import session
import mytime
import threading
import uuid

comment_url = "http://music.163.com/api/v1/resource/comments/R_SO_4_520458203"
Mname_url = "https://music.163.com/song?id="
proxy_list = []
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
    "Referer": "http://music.163.com/",
    "Content-Type": "application/json",
    "Cookie": "_iuqxldmzr_=32; _ntes_nnid=fa970a3e6429f7a1128f6c59fc6dbce6,1545818838892; _ntes_nuid=fa970a3e6429f7a1128f6c59fc6dbce6; __utmc=94650624; WM_NI=AQ9phYuIqUvp85AXUQ%2FCvxu4ctr0ZcLY%2B2KdUmEF07k3mG1JOMC8Mywp8epPFb8ZorRoqwylJP%2BTMaxMLK9WMzSQxGbzmPR%2Fdpp%2F0IMuJMRNHUwc%2BIwFRj0VRKyGO0%2B%2BNkw%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eea4d13caeecfdd8b76bf5ef8eb7d45f969e9aaeb76bedee9cccbc21aaa9988bbc2af0fea7c3b92a838ff791eb53b797bfb6f57cfceb8fb9d85bed9dba99f840a1acbed1d9699087e5d3ca7097b38ba7b33da9eda3a8b4428d938dd9d073b5b0f886f35c86bef8bbee7a92b1bf98fc688a90e5b5d06bbc9384acbc5d8fa69db2fb4da2a6a3b1d125a8b0c0d0b3438fab86aed1468c8bb984aa43b59a9e8bb35e9295b7a8ce3ce9f5828cf637e2a3; WM_TID=0NWFfPd%2BjlRBABEURAc8Lv2S64ui1Gz5; playerid=21689604; __utma=94650624.709259473.1545818839.1545818839.1545873192.2; __utmz=94650624.1545873192.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __remember_me=true; MUSIC_U=72f4c91e0ab8ecfda87a2b70901378d9e338b367896ff5d684ed54d73262c65007d1acd73dfe625fd1452e28c74353fb77749c2dda21047b; __csrf=fa90670026159953729812e679ccddbc; JSESSIONID-WYYY=vioHGttWfvG8UTqoXOrYDZKakoY%2F2YI0%2FHkKRJMFaqJ%5CiVKIpB1jvh%2FIsyODVE2c%2FVawRQ1cHVwJnb%5C7rMWnRMHCsyFMpTFSb8GQhixPbQxYKPvaq%2BHW1uin%5Cr6mI%2BkGvek20DtkzX8sGnW1R14geGPjmvMyfMorf6hej0UpXi588QS1%3A1545878473103",
}


class pachong():
    def __init__(self,mukuai):
        self.mukuai = str(mukuai)
        self.comment_url = "http://music.163.com/api/v1/resource/comments/R_SO_4_"
        self.name_url = "https://music.163.com/song?id="
        self.singer_url = "https://music.163.com/artist?id=" + self.mukuai
        self.singer_male_cn = "https://music.163.com/discover/artist/cat?id="+self.mukuai+"&initial="
        self.user_agent_list = [
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36", ]

        self.http_ip_list = []
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
            "Cookie": "_ntes_nuid=53217f47402813274594dae64e623016; _ntes_nnid=4ca50713dec84cc1a4ec17f57643d0c4,1522972580146; vjuids=13aa187821.16430119ba5.0.42b2671e2b68d; vinfo_n_f_l_n3=b4a902be04ab5bfe.1.4.1522972580162.1529848612564.1534686000373; vjlast=1529814818.1544264256.22; hb_MA-BFF5-63705950A31C_source=www.baidu.com; _iuqxldmzr_=32; WM_TID=zN%2FsvAxdNJ9AQVUEUEIofu26i1Vl6dpO; __utmz=94650624.1545926550.3.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; WM_NI=fvQzsrLWNDp2lL3MoFUO02xXlcn2YegAI%2FTNDHQJiIlFWIRncvB%2FqA%2FhvHOslkQvfNiSHgg%2F0H6m1uqHb7hy6CWOnxn4aecotAjOCE3NzhSevy6ZU1TS30NV9Z%2F5DHtXMU0%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeb3d74088b7a383c24491bc8fb6d15e839f8bafee6ee9ebff91f25aac8ea2b9fc2af0fea7c3b92aa6aa9f9bf27a908982a5f33ab094fdaeee4e979100d3fb54b0bda2d3dc6fa59f87d0d74688989fabec43b09a99aad166a1aa8ed0f44bedb8baa9ce79b0b59f97e546ab8d8888e625f498fa8eb47fb398aed8eb73f69d99b0ed74aeecaf86e265b89fa6b0c24ff192b689d26fb6a7fabbd83b988dfdd1cd5efb86e1d6c744b88883b6b337e2a3; JSESSIONID-WYYY=7%5ChrE4v19URKJjb1ic5boJPTl4NFwcx%2Byj35v50d4GWcd19l0WDaEcz%2Fs3X%2FGNEVlz0naNW1Fz%2BgX7Nh6%5CrdG%2BAvMtniUFwGPg7f%2F%2FhkDQ%5CKjdSjvV%2FXkdmgKhDxOikgS07QDRgrGxK5K4McKv4ROfIuW%5CfJvSvnw81FiKdpVtCA2xbT%3A1546011578068; __utma=94650624.1134177321.1545914571.1546001073.1546010852.5" \
            }
    def get_singer_music(self,proxy=None):
        try:
            html = self.get(url=self.singer_url , proxy=proxy)
            music = re.findall(r'song\?id=(\d+)">(.*?)</a>', html.content.decode("utf-8"), re.S)
            print(music,len(music))
            if music is None:
                return None
            else:
                return music
        except:
            return None
    def get(self, url, proxy=None, timeout=3):
        print("正在请求", url)
        ishttp = url[0:5]
        UA = random.choice(self.user_agent_list)
        self.header["User-Agent"] = UA
        if proxy == None:
            rz = requests.get(url, headers=self.header, timeout=timeout).content.decode("utf-8")
            if "很抱歉，服务器开小差了，请稍后再试" not in rz:
                return requests.get(url, headers=self.header, timeout=timeout)
            else:
                print("IP被封")
                if ishttp == "http:":
                    IP = "".join(random.choice(self.http_ip_list)).strip()
                    proxy = {"http": IP}
                elif ishttp == "https":
                    IP = "".join(random.choice(self.https_ip_list)).strip()
                    proxy = {"https": IP}
                print("正在更换代理")
                print("当前代理：", proxy)
                return self.get(url, proxy=proxy, timeout=timeout)
        else:
            try:
                rz = requests.get(url, headers=self.header, proxies=proxy, timeout=timeout).content.decode("utf-8")
                if "很抱歉，服务器开小差了，请稍后再试" not in rz:
                    return requests.get(url, headers=self.header, proxies=proxy, timeout=timeout)
                else:
                    print("IP被封")
                    if ishttp == "http:":
                        # self.http_ip_list.remove(IP)
                        IP = "".join(random.choice(self.http_ip_list)).strip()
                        proxy = {"http": IP}
                    elif ishttp == "https":
                        IP = "".join(random.choice(self.https_ip_list)).strip()
                        proxy = {"https": IP}
                    print("正在更换代理")
                    print("当前代理：", proxy)
                    return self.get(url, proxy=proxy)
            except Exception as e:
                print("代理无效")
                if ishttp == "http:":
                    # self.http_ip_list.remove(IP)
                    IP = "".join(random.choice(self.http_ip_list)).strip()
                    proxy = {"http": IP}
                elif ishttp == "https":
                    IP = "".join(random.choice(self.https_ip_list)).strip()
                    proxy = {"https": IP}
                print("正在更换代理")
                print("当前代理：", proxy)
                return self.get(url, proxy=proxy)
    def singer(self, id, proxy=None):
        try:
            html = self.get(url=self.singer_male_cn + str(id) , proxy=proxy)
            music = re.findall(r'artist\?id=(\d+).*?的音乐">(.*?)</a>', html.text, re.S)
            # print(music,type(music))
            if music is not None:
                return music
            else:
                return None
        except:
            return None

    def singer2db(self, id, sleep=1):
        singers = self.singer(id)
        if singers is not None:
            for singer in singers:
                print(singer)
                session.add(moduelsinger.Singer(singer=singer[1], singerid=singer[0],type = self.mukuai, creattime=mytime.get_now()))
                session.commit()
        time.sleep(sleep)

    def get_name(self, musicid, proxy=None):
        try:
            html = self.get(url=self.name_url + str(musicid), proxy=proxy)
            music = re.findall(r'json">(.*?)</script>', html.content.decode("utf-8"), re.S)
            if music is not None:
                music = eval(music[0])
            # print(music,type(music))
            return music
        except:
            return None

    def get_comment(self, musicid, proxy=None):
        try:
            comment = self.get(url=self.comment_url + str(musicid), proxy=proxy)
            # print(comment.text)
            cms = json.loads(comment.text)["total"]
            return cms
        except:
            return None

    def music2db(self, id, t=5):
        comments = self.get_comment(id)
        if comments != 0 or comments is not None:
            mus = self.get_name(id)
            print(mus, comments)
            if mus is not None:
                desc = mus["description"]
                singer = desc[desc.find("歌手：") + 3:desc.find("所属专辑")]
                album = desc[desc.find("所属专辑：") + 5:]
                # print(singer,album)
                session.add(
                    moduelsinger.Music(id = uuid.uuid3(uuid.uuid4(),"1"),musicid=mus["@id"],singerid = self.mukuai, title=mus["title"], image=mus["images"], singer=singer,
                                 album=album,
                                 pubdate=mus["pubDate"], comments=comments, creattime=mytime.get_now(),
                                 updatetime=mytime.get_now()))

                session.commit()

                print(mus["title"] + "入库成功:id=", id)
                time.sleep(t)
                return 1
        else:
            print(id, ":评论数为空")
            return 0


if __name__ == "__main__":

    '''
    for i in range(127615,300000):
        #id = random.randint(100000,999999)

        isdata = pc.music2db(i,t = 1)
    #html = requests.get(url = "https://music.163.com/song?id=536099160",proxies = {"https":"123.127.93.188:44399"})
    '''
    type_list =[1001,1002,1003,2001,2002,2003,6001,6002,6003,7001,7002,7003,4001,4002,4003]
    for tl in type_list:
        pc = pachong(tl)
        try:
            pc.singer2db(90, sleep=0)
        except Exception as e:
            print(e)
            '''
    lock = threading.Lock()

    def get_music(start,end):
        singerid = session.query(moduelsinger.Singer.singerid,moduelsinger.Singer.singer).filter(moduelsinger.Singer.type == 1001).all()
        #singerid = [('1876', '阿杜')]
        for sid in range(start,end):
            pc = pachong(singerid[sid][0])
            musics = pc.get_singer_music()
            #print("歌手",singerid[sid][1])
            if musics is not  None:
                print("第" + str(sid+1) + "位歌手", singerid[sid][1])
                for music in musics:
                    try:
                        pc.music2db(music[0], t=0)
                    except Exception as e:
                        print(e)
                        continue
            else:
                print("页面无数据")

    pc = pachong(1876)
    pc.get_singer_music()
    threads = []
    start_time = time.time()
    for i in range(0,8,2):
        step = 2
        print(i,i+step)
        threads.append(threading.Thread(target=get_music,args=(i,i+step)))
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print('主线程结束了！', threading.current_thread().name)
    print('一共用时：', time.time() - start_time)
    #get_music(400)'''




