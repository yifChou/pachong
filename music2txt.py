import requests
import json
import time
import re
import random
import moduelsinger
import models
from deractor_py import *
from moduelsinger import session
import mytime
import threading


comment_url = "http://music.163.com/api/v1/resource/comments/R_SO_4_"
name_url = "https://music.163.com/song?id="
singer_url = "https://music.163.com/artist?id="
singer_male_cn = "https://music.163.com/discover/artist/cat?id="
user_agent_list = [
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36", ]
lock = threading.Lock()
http_ip_list = []
https_ip_list = []
with open("httpsip.txt", "r") as f:
    for line in f:
        https_ip_list.append(line.strip())
with open("httpip.txt", "r") as f:
    for line in f:
        http_ip_list.append(line.strip())
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
    "Referer": "http://music.163.com/",
    "Content-Type": "application/json",
    "Cookie": "_ntes_nuid=53217f47402813274594dae64e623016; _ntes_nnid=4ca50713dec84cc1a4ec17f57643d0c4,1522972580146; vjuids=13aa187821.16430119ba5.0.42b2671e2b68d; vinfo_n_f_l_n3=b4a902be04ab5bfe.1.4.1522972580162.1529848612564.1534686000373; vjlast=1529814818.1544264256.22; hb_MA-BFF5-63705950A31C_source=www.baidu.com; _iuqxldmzr_=32; WM_TID=zN%2FsvAxdNJ9AQVUEUEIofu26i1Vl6dpO; __utmz=94650624.1545926550.3.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; WM_NI=fvQzsrLWNDp2lL3MoFUO02xXlcn2YegAI%2FTNDHQJiIlFWIRncvB%2FqA%2FhvHOslkQvfNiSHgg%2F0H6m1uqHb7hy6CWOnxn4aecotAjOCE3NzhSevy6ZU1TS30NV9Z%2F5DHtXMU0%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeb3d74088b7a383c24491bc8fb6d15e839f8bafee6ee9ebff91f25aac8ea2b9fc2af0fea7c3b92aa6aa9f9bf27a908982a5f33ab094fdaeee4e979100d3fb54b0bda2d3dc6fa59f87d0d74688989fabec43b09a99aad166a1aa8ed0f44bedb8baa9ce79b0b59f97e546ab8d8888e625f498fa8eb47fb398aed8eb73f69d99b0ed74aeecaf86e265b89fa6b0c24ff192b689d26fb6a7fabbd83b988dfdd1cd5efb86e1d6c744b88883b6b337e2a3; JSESSIONID-WYYY=7%5ChrE4v19URKJjb1ic5boJPTl4NFwcx%2Byj35v50d4GWcd19l0WDaEcz%2Fs3X%2FGNEVlz0naNW1Fz%2BgX7Nh6%5CrdG%2BAvMtniUFwGPg7f%2F%2FhkDQ%5CKjdSjvV%2FXkdmgKhDxOikgS07QDRgrGxK5K4McKv4ROfIuW%5CfJvSvnw81FiKdpVtCA2xbT%3A1546011578068; __utma=94650624.1134177321.1545914571.1546001073.1546010852.5" \
    }

def get_singer_music( id,proxy=None):
    try:
        html = get(url=singer_url + str(id), proxy=proxy)
        music = re.findall(r'song\?id=(\d+)">(.*?)</a>', html.content.decode("utf-8"), re.S)
        print(music, len(music))
        if music is None:
            return None
        else:
            return music
    except:
        return None

def get( url, proxy=None, timeout=3):
    print("正在请求", url)
    ishttp = url[0:5]
    UA = random.choice(user_agent_list)
    header["User-Agent"] = UA
    if proxy == 1:
        print("使用本机ip")
        rz = requests.get(url, headers=header, timeout=timeout).content.decode("utf-8")
        if "很抱歉，服务器开小差了，请稍后再试" not in rz:
            return requests.get(url, headers=header, timeout=timeout)
        else:
            print("IP被封")
            if ishttp == "http:":
                IP = "".join(random.choice(http_ip_list)).strip()
                proxy = {"http": IP}
            elif ishttp == "https":
                IP = "".join(random.choice(https_ip_list)).strip()
                proxy = {"https": IP}
            print("正在更换代理")
            print("当前代理：", proxy)
            return get(url, proxy=proxy, timeout=timeout)
    else:
        print("使用代理ip")
        if ishttp == "http:":
            IP = "".join(random.choice(http_ip_list)).strip()
            proxy = {"http": IP}
        elif ishttp == "https":
            IP = "".join(random.choice(https_ip_list)).strip()
            proxy = {"https": IP}
        print("正在更换代理")
        print("当前代理：", proxy)
        try:
            rz = requests.get(url, headers=header, proxies=proxy, timeout=timeout).content.decode("utf-8")
            if "很抱歉，服务器开小差了，请稍后再试" not in rz:
                return requests.get(url, headers=header, proxies=proxy, timeout=timeout)
            else:
                print("IP被封")
                if ishttp == "http:":
                    # http_ip_list.remove(IP)
                    IP = "".join(random.choice(http_ip_list)).strip()
                    proxy = {"http": IP}
                elif ishttp == "https":
                    IP = "".join(random.choice(https_ip_list)).strip()
                    proxy = {"https": IP}
                print("正在更换代理")
                print("当前代理：", proxy)
                return get(url, proxy=proxy)
        except Exception as e:
            print("代理无效")
            if ishttp == "http:":
                # http_ip_list.remove(IP)
                IP = "".join(random.choice(http_ip_list)).strip()
                proxy = {"http": IP}
            elif ishttp == "https":
                IP = "".join(random.choice(https_ip_list)).strip()
                proxy = {"https": IP}
            print("正在更换代理")
            print("当前代理：", proxy)
            return get(url, proxy=proxy)

def get_name( musicid, proxy=None):
    try:
        html = get(url=name_url + str(musicid), proxy=proxy)
        music = re.findall(r'json">(.*?)</script>', html.content.decode("utf-8"), re.S)
        if music is not None:
            music = eval(music[0])
        # print(music,type(music))
        return music
    except:
        return None

def get_comment( musicid, proxy=None):
    try:
        comment = get(url=comment_url + str(musicid), proxy=proxy)
        # print(comment.text)
        cms = json.loads(comment.text)["total"]
        return cms
    except:
        return None
@run_time()
def music2txt( id,singerid):
    comments = get_comment(id)
    if comments != 0 or comments is not None:
        mus = get_name(id)
        print(mus, comments)
        if mus is not None:
            #desc = mus["description"]
            #singer = desc[desc.find("歌手：") + 3:desc.find("所属专辑")]
            #album = desc[desc.find("所属专辑：") + 5:]
            # print(singer,album)
            mus["comment"] = comments
            mus["singerid"] = singerid
            lock.acquire()
            try:
                with open("music2txt.txt","a+") as f:
                    f.writelines(str(mus) + "\n")
                    print(mus["title"] + "写入txt成功:id=", id)
            finally:
                lock.release()
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

    type_list =[1001,1002,1003,2001,2002,2003,6001,6002,6003,7001,7002,7003,4001,4002,4003]
    for tl in type_list:

        try:
            for i in range(65, 90):
                pc.singer2db(i, sleep=2)
            pc.singer2db(0)
        except Exception as e:
            print(e)'''
    lock = threading.Lock()


    def get_music(start, end):
        try:
            singerid = session.query(moduelsinger.Singer.singerid, moduelsinger.Singer.singer).filter(
                moduelsinger.Singer.type == 1001).all()
            #print(singerid)
            # singerid = [('1876', '阿杜')]
            print(start, end)
            for sid in range(start, end):
                musicid = singerid[sid][0]
                musics = get_singer_music(musicid)
                # print("歌手",singerid[sid][1])
                if musics is not None:
                    print("第" + str(sid + 1) + "位歌手", singerid[sid][1])
                    for music in musics:
                        try:
                            music2txt(music[0],singerid[sid][0])
                        except Exception as e:
                            print(e)
                            continue
                else:
                    print("页面无数据")
        except Exception as e:
            print(e)

    '''pc = pachong(1876)
    pc.get_singer_music()'''
    threads = []
    start_time = time.time()
    for i in range(0,20,2):
        step = 2
        print(i, i + step)
        threads.append(threading.Thread(target=get_music, args=(i, i + step)))
    for t in threads:
        t.start()
    print('主线程结束了！', threading.current_thread().name)
    print('一共用时：', time.time() - start_time)
    # get_music(400)




