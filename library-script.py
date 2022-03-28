import json
import datetime
import logging
import time

import requests

date = datetime.date.today()


# 得到用户的token
def login():
    Form_data = {
        "username": 19131201051,
        "password": 146314,
    }

    logi = "https://leosys.cn/hnuahe/rest/auth?username=19131201051&password=146314"

    headers = {
        "Connection": "keep-alive",
    }

    content = requests.get(logi, data=Form_data, headers=headers)

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
        "date": str(date),
        "startTime": "1020",
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

    return {
        "code": code,
        "mes": data
    }


def main():
    user_token = login()

    messages = qiangzuowei(user_token)
    return {
        "code": messages['code'],
        "mes": messages['mes']
    }


if __name__ == "__main__":
    s = main()
    print(s)
    info = str(s)
    with open("loging.log", "a") as logings:
        print(str(datetime.datetime.now()) + "-" + "messages is :{}".format(info), file=logings)
