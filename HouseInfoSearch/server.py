# -*- coding: utf-8 -*-
"""
@Time ： 2022/12/1 15:52
@Auth ： XM
@File ：server.py
@IDE ：PyCharm
"""
import time

import cv2
import numpy as np
import flask
import json
import base64
from flask_apscheduler import APScheduler
from utils import Spyider, SearchEngine, DB

scheduler = APScheduler()

SE = SearchEngine('./ori_info.txt', 'log.txt')
db = DB('city_info.db', './cities.csv')
isUpdate = False

# @scheduler.task('cron', id='refresh db', week='*', day_of_week='sun')
@scheduler.task('interval', id='refresh db', seconds=3600*24*30, misfire_grace_time=900)
def refresh():
    global isUpdate
    isUpdate = True
    spy = Spyider()
    spy.run()
    db.refresh('cities.csv')
    print('Database refreshed!')
    isUpdate = False


api = flask.Flask(__name__)


@api.route('/search', methods=['post'])
def search(show_test=True):
    infos = flask.request.get_json()
    if isUpdate:
        ren = {'msg': '正在进行数据库更新', 'code': 1}
        return ren
    SE.record('start search...')
    try:
        city = infos['city_name']
        message, code = SE.Search(city)
        SE.record(message)
        ren = {'msg':message, 'code':code}
    except Exception as e:
        print(e)
        ren = {'msg':'查找失败', 'code':-100}
    return ren

@api.route('/read', methods=['post'])
def readData(show_test=True):
    if isUpdate:
        ren = {'msg': '正在进行数据库更新', 'code': 1}
        return ren
    SE.record('start read data...')
    infos = flask.request.get_json()
    try:
        city = infos['city_name']
        res = db.search(city)
        res = [item[1:] for item in res]
        SE.record(f'Get {city}\'s info ok!')
        ren = {'msg':res, 'code':0}
    except Exception as e:
        print(e)
        ren = {'msg':e, 'code':-101}
    return ren

@api.route('/show', methods=['get'])
def get_city_house_info(show_test=True):
    if isUpdate:
        ren = {'msg': '正在进行数据库更新', 'code': 1}
        return ren
    try:
        res = db.getNums()
        res = {k[0]:v for k, v in res.items()}
        print(res)
        SE.record('get city house info from database!')
        ren = {'msg':res, 'code':0}
    except Exception as e:
        print(e)
        ren = {'msg':e, 'code':-102}
    return ren


if __name__ == '__main__':
    scheduler.init_app(api)
    scheduler.start()
    api.run(port=8080, debug=True, host='127.0.0.1')  # 启动服务

