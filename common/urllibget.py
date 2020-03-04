# 导入urllib 包 实现爬取
import urllib.request
from common.uapools import UaPools as ua


def get_data(url, encode="utf-8", changeNo=1, type=1):
    data = ""
    try:
        if url:
            # 设置浏览器标识伪装
            opener = urllib.request.build_opener()
            # 放入请求头 list
            opener.addheaders = [ua.get_ua(type, changeNo)]
            # 安装为全局
            urllib.request.install_opener(opener)
            # 打开一个网页到内存中  .read()读数据  decode('utf-8' , ignore)解码(编码，忽略问题)
            data = urllib.request.urlopen(url).read().decode(encode, "ignore")
    except Exception:
        pass
    return data
