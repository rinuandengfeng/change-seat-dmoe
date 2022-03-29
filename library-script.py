#-*- coding: UTF-8 -*-

import json
import datetime
import logging
import time

import requests

today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)


# 得到用户的token
def login():
    logi = "https://leosys.cn/hnuahe/rest/auth?username=19131201051&password=146314"

    headers = {
        "Connection": "keep-alive",
        "User-Agent": "mozilla/5.0 (iphone; cpu iphone os 5_1_1 like mac os x) applewebkit/534.46 (khtml, like gecko) mobile/9b206 micromessenger/5.0"
    }

    content = requests.get(logi, headers=headers)

    raw = content.text
    # 将其转化为json格式
    raw_json = json.loads(raw)
    # 取出生成的token
    token = raw_json["data"]["token"]

    return token


# 抢座函数
def qiangzuowei(user_token):
    authid = ""
    Form_data = {
        "seat": "45001",
        "date": str(today),
        "startTime": "1080",
        "endTime": "1260",
        "authid": authid,
    }
    url = "https://leosys.cn/hnuahe/rest/v2/freeBook"

    headers = {
        "Referer": "https://servicewechat.com/wx8adafd853fc21fd6/24/page-frame.html",
        "content-type": "application/x-www-form-urlencoded",
        "token": user_token

    }
    content = requests.post(url, data=Form_data, headers=headers)
    raw = content.text
    # 将其转化为json格式
    raw_json = json.loads(raw)

    code = raw_json['status']
    data = raw_json["data"]
    message = raw_json["message"]

    return {
        "code": code,
        "data": data,
        "mess": message
    }


def qiangzuowei2(user_token):
    authid = ""
    Form_data = {
        "seat": "45001",
        "date": str(tomorrow),
        "startTime": "1080",
        "endTime": "1260",
        "authid": authid,
    }
    url = "https://leosys.cn/hnuahe/rest/v2/freeBook"

    headers = {
        "Referer": "https://servicewechat.com/wx8adafd853fc21fd6/24/page-frame.html",
        "content-type": "application/x-www-form-urlencoded",
        "User-Agent": "mozilla/5.0 (iphone; cpu iphone os 5_1_1 like mac os x) applewebkit/534.46 (khtml, like gecko) mobile/9b206 micromessenger/5.0",
        "token": user_token

    }
    content = requests.post(url, data=Form_data, headers=headers)
    raw = content.text
    # 将其转化为json格式
    raw_json = json.loads(raw)

    code = raw_json['status']
    data = raw_json["data"]
    messa = raw_json["message"]

    return {
        "code": code,
        "data": data,
        "mess": messa,
    }


def main():
    user_token = login()

    messages = qiangzuowei(user_token)
    tom_mess = qiangzuowei2(user_token)
    return {
        "user_token":user_token,
        # "code": messages['code'],
        "data": messages['data'],
        "mess": messages["mess"],
        # "code2": tom_mess['code'],
        "data2": tom_mess['data'],
        "mess2": tom_mess["mess"],
    }


if __name__ == "__main__":
    s = main()
    print(s)
    info = str(s)
    with open("loging.log", "a") as logings:
        print(str(datetime.datetime.now()) + "-" + "messages is :{}".format(info), file=logings)
