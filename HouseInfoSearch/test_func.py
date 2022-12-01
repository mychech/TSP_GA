# -*- coding: utf-8 -*-
"""
@Time ： 2022/12/1 21:50
@Auth ： XM
@File ：test_func.py
@IDE ：PyCharm
"""
import requests

def test_search(url, cases):
    success = 0
    for case in cases:
        try:
            r = requests.post(url, json={'city_name':case})
            if r.status_code == 200:
                print(r.json())
                success += 1
        except Exception as e:
            print(e)
    print("success {} / {} !".format(success, len(cases)))


def test_readData(url, cases):
    success = 0
    for case in cases:
        try:
            r = requests.post(url, json={'city_name':case})
            if r.status_code == 200:
                print(r.json())
                success += 1
        except Exception as e:
            print(e)
    print("success {} / {} !".format(success, len(cases)))


def test_get_city_house_info(url):
    success = 0
    for i in range(5):
        try:
            r = requests.get(url)
            if r.status_code == 200:
                print(r.json())
                success += 1
        except Exception as e:
            print(e)
    print("success {} / {} !".format(success, 5))

if __name__ == '__main__':
    url = 'http://127.0.0.1:8080/search'
    cases = ['长', 'xa', '长春', '', '沈阳']
    test_search(url, cases)
    test_readData(url.replace('search', 'read'), cases)
    test_get_city_house_info(url.replace('search', 'show'))