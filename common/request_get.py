from common.uapools import UaPools as ua
import requests


def req(url, params={}, type="get", headers={}, proxies={}, cookies={}):
    """
    获取请求结果对象
    :param type:  请求类型
    :param url:  请求地址
    :param params:  get 参数
    :param headers: 请求头 自动添加浏览器伪装
    :param proxies: 用户代理
    :param cookies:
    :return:  返回请求结果对象
    """
    headers["User-Agent"] = ua.get_ua_str()
    if url:
        if type == "get":
            return requests.get(url, params=params, headers=headers, proxies=proxies, cookies=cookies)
        else:
            return requests.post(url, data=params, headers=headers, proxies=proxies, cookies=cookies)
    return None
