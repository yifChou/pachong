from test12 import modeltest
from test12.modeltest import  session
from deractor_py import run_time,thread_run_time
import time
import threading
@thread_run_time()
def intodb():
    for i in range(200):
        #session.add(modeltest.Test(musicid = str(i),title = threading.current_thread().name ))
        #session.commit()
        #print(i,threading.current_thread().name)
        with open("text.txt","a+") as f:
            f.writelines(str(i) + threading.current_thread().name + "\n")

def thread2db():
    threads = []
    for i in range(10):
        threads.append(threading.Thread(target=intodb))
    for t in threads:
        t.start()
def for2db():
    for i in range(10):
        intodb()

thread2db()
#for2db()

