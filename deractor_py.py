import functools
import time
import threading
def cal_run_time(text,index = 0):
    def deracoter(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            print(text,":共",len(args[index]),"首歌")
            start = time.time()
            a = func(*args,**kwargs)
            end = time.time()
            print(func.__name__,"耗时:", end - start)
            return a
        return wrapper
    return deracoter
def run_time():
    def deracoter(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            start = time.time()
            a = func(*args,**kwargs)
            end = time.time()
            print(threading.current_thread().name,func.__name__,"耗时:", end - start)
            return a
        return wrapper
    return deracoter
def thread_run_time():
    def deracoter(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            start = time.time()
            a = func(*args,**kwargs)
            end = time.time()
            print(func.__name__,"耗时:", end - start)
            return a
        return wrapper
    return deracoter
@cal_run_time(text = "计时开始")
def test(sleep):
    time.sleep(sleep)

