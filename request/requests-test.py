import time

import common.request_get as req
import re

url = "https://yq.aliyun.com/search/articles/"
# 请求一次获取总条数
text = req.req(url, {"q": "python"}).text
pat = "<div class=\"_search-info\">找到(.*?)条关于"
patHref = "<div class=\"media-body text-overflow\">.*?<a href=\"(.*?)\">"
detailPatTitle = '<h2 class="blog-title">(.*?)</h2>'
detailPatContent = "<div class=\"content-detail unsafe markdown-body\">(.*?)</div>"
listCount = re.compile(pat).findall(text)[0]
pages = int(listCount) / 15 + 1
for i in range(0, int(pages)):
    print("---------------------------------------------第" + str(
        i + 1) + "页-------------------------------------------------------")
    params = {"p": str(i + 1),
              "q": "python"
              }
    data = req.req(url, params).text
    listUrl = re.compile(patHref, re.S).findall(data)
    for info in listUrl:
        thisUrl = "https://yq.aliyun.com/" + info
        detailInfo = req.req(thisUrl).text
        title = re.compile(detailPatTitle, re.S).findall(detailInfo)[0].strip()
        content = re.compile(detailPatContent, re.S).findall(detailInfo)[0].strip()
        fn = open("F:\\pythonLoad\\" + str(i) + "-" + str(time.time()) + ".html", "w", encoding="utf-8")
        fn.write(title+"</br></br>"+content)
        fn.close()
