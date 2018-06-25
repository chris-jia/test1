###360搜索
import requests
def so360(key):
    path = 'https://www.so.com/s?ie=utf-8&fr=none&src=360sou_newhome&q='
    url  = path+key
    try:
        r = requests.get(url)
        r.raise_for_status()
        return r.text[:1000]
    except:
        return '网络爬虫错误'

print(so360('123'))
    
        
