import common.urllibget as urlget
import re
#  通过接口分析，然后获取接口调用规律。动态生成URL完成数据获取
# 获取后通过正则再解析出相关需要的数据
for i in range(0, 10):
    cid = "6637966581896596994"
    url = "https://video.coral.qq.com/varticle/4839510556/comment/v2?callback=_varticle4839510556commentv2&orinum=10&oriorder=o&pageflag=1&cursor=" + cid + "&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=132&_=1583041560956"
    data = urlget.get_data(url)
    pat = "\"content\":\"(.*?)\""
    dataList = re.compile(pat).findall(data)
    print("------------------------------------------第" + str(i) + "页-------------------------------------------------")
    for info in dataList:
        print(info)
        print("==================================================\n")
    patLast = "\"last\":\"(.*?)\""
    cid = re.compile(patLast).findall(data)[0]
