import requests
def pachong(url = "https://www.baidu.com"):#//正斜杠
    try:
        r = requests.get(url)
        r.raise_for_status()###如果不是200，则报错
        list1 = [r.status_code,r.encoding,r.apparent_encoding,r.content[:10]]
        r.encoding = r.apparent_encoding
        print(list1)
        print(r.text[:1000])
        print(r.request.headers)
    except:
        print('网页爬取失败')
pachong('https://s.taobao.com/search?q=书包&s=44')

    
