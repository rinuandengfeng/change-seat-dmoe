FROM ubuntu:18.04

RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list \
&& sed -i s@/security.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list \
&& apt-get clean \
&& apt-get update \
&& apt-get install -y python3-pip python3-dev \
&& rm -rf /var/lib/apt/lists/*

RUN ln -s /usr/bin/python3 /usr/bin/python

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

WORKDIR /test
COPY ./library-script /test

#4. 升级pip版本
RUN pip3 install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple
#5.运行pip命令安装依赖
RUN pip3 install --no-cache-dir --upgrade -r /test/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple


CMD python3 main.py

