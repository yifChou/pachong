from moduelsinger import  session
import moduelsinger
import mytime
with open("music2txt.txt","r") as f :
    i = 0
    j = 0
    for line in f:
        try:
            mus = eval(line)
            print(mus)
            desc = mus["description"]
            singer = desc[desc.find("歌手：") + 3:desc.find("所属专辑")]
            album = desc[desc.find("所属专辑：") + 5:]
            i += 1
            print(i)
            session.add(
                moduelsinger.Music(musicid=mus["@id"], singerid=self.mukuai, title=mus["title"], image=mus["images"],
                                   singer=singer,
                                   album=album,
                                   pubdate=mus["pubDate"], comments=mus["comment"], creattime=mytime.get_now(),
                                   updatetime=mytime.get_now()))
            session.commit()
        except Exception as e:
            j += 1
            print(e,j)