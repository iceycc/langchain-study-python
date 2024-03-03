# 导入所需的库
import json
import requests
import time


# 定义爬取微博用户信息的函数
def scrape_weibo(url: str):
    '''爬取相关鲜花服务商的资料'''
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Referer": "https://weibo.com/u/6053338099"
    }
    cookies = {
        "cookie": '''XSRF-TOKEN=YYPJrzcLdGeBewXY6ePbsbsU; PC_TOKEN=beb12fc36f; WBStorage=267ec170|undefined; login_sid_t=6142d8402563f6a1508df977f035fb68; cross_origin_proto=SSL; wb_view_log=1512*9822; _s_tentry=weibo.com; Apache=6918272981852.718.1709469592962; SINAGLOBAL=6918272981852.718.1709469592962; ULV=1709469592963:1:1:1:6918272981852.718.1709469592962:; WBtopGlobal_register_version=2024030320; crossidccode=CODE-tc-1RGL8W-22VkAY-9FiDEgnY0k7daMP96586b; UOR=,,graph.qq.com; ALF=1712061683; SUB=_2A25I4B-jDeRhGedJ4loV8ijKzD6IHXVrnB1rrDV8PUJbkNAGLWXnkW1NUZuU1glvd9GcBlHt-McThFFj1Ch2b8E7; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9Wh0d3EPvNFX.YxF2Rok5ngX5JpX5KzhUgL.Fo2N1KnXeoqcS0z2dJLoIEBLxKBLB.qLBK2LxKBLBonLBoqLxK-L1hqLBo5LxKqLBoBL12zt; WBPSESS=RNlnH8SfpE3xZek5ivi4LtvPHZkIkayyO7MJdnRy0lxkZvhsyhlixM3Rb1rhHEhEDIoRTeVrL2vUvpugflDMOVuUQMiN5SJG2gLF_qIamZApGVg0eD-Yk8sKhiG5fFzE1b3rco7hV2hsl6xas8B-Iw=='''
    }
    response = requests.get(url, headers=headers, cookies=cookies)
    time.sleep(3)  # 加上3s 的延时防止被反爬
    return response.text


# 根据UID构建URL爬取信息
def get_data(UID):
    url = "https://weibo.com/ajax/profile/detail?uid={}".format(UID)
    html = scrape_weibo(url)
    print(html)
    response = json.loads(html)

    return response
