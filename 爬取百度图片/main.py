from urllib import parse
import os
import requests
import time

def get_html(url,headers,parmes):
    t = session.get()
    return t.json()

def pro_html():
    pass

def download_html():
    pass



if __name__ == "__main__":
    keyname = "阴阳师"
    HEADER={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36",
        "Referer":"https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1611502391929\
                   _R&pv=&ic=0&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&sid=&word={}".format(parse.quote(keyname)),
        "Cookie":"BIDUPSID=0A1AE6BADBEBEDABBAA168AD22EE0206;PSTM=1598009450;BAIDUID=0A1AE6BADBEBEDABBBEC6662EF333420:FG=1;MCITY=-179%3A;\
                 __yjs_duid=1_925459582d6e9af6e5f7e37e9fff99d91609601515116;BAIDUID_BFESS=6E042F1A94F14B958E05ED17B3FAD98B:FG=1;\
                 BDRCVFR[PaHiFN6tims]=9xWipS8B-FspA7EnHc1QhPEUf;delPer=0;PSINO=5;H_PS_PSSID=;BA_HECTOR=010g01842la5a10hdj1g0r4kg0r;\
                 BDORZ=B490B5EBF6F3CD402E515D22BCDA1598;BDRCVFR[X_XKQks0S63]=mk3SLVN4HKm;userFrom=www.baidu.com;firstShowTip=1;\
                 cleanHistoryStatus=0;BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm;BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm;\
                 ab_sr=1.0.0_MTFmOGJhOWZjZmU1ZGU4MDFmMjczNDRmMDY2MGMxZDk4ZmVjNmEwMTVkYTlkMDVlOTc1MjMwYmU0OWEyNmE2MmRhOGI2NTk3ZjhlMjEwZjNjYzEyZTMyZTcyNzRkNjM1;\
                 indexPageSugList=%5B%22%E9%98%B4%E9%98%B3%E5%B8%88%E6%8F%92%E7%94%BB%204k%22%2C%22%E5%A3%81%E7%BA%B8%22%5D"
    }
    session= requests.session()
    session.headers = HEADER

    URL =