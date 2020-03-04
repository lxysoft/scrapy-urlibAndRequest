import common.urllibget as urlget
# 导入正则包
import re


data = urlget.get_data("http://www.yicommunity.com/")


# 正则表达式
pat = "<div class=\"content\".*?title.*?>(.*?)</div>"
# 正则匹配抓取数据 re.S多行， 在data中提取
content = re.compile(pat, re.S).findall(data)
for info in content:
    print(info)
    print("-----------------------------------------------\n")
