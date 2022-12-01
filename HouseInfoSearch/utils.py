import random
import requests
from lxml import html
etree = html.etree
import os
import sqlite3
import time
import logging
from tqdm import tqdm
from collections import Counter


class SearchEngine:

    def __init__(self, ori_file, log_file):
        self.log_init(log_file)
        self.GenerateCities(ori_file)

    def GenerateCities(self, ori_file):
        self.file_logger.info('正在初始化城市文件...')
        self.possible_infos = {}
        self.index2name = {}
        with open(ori_file, 'r', encoding='utf-8') as f:
            infos = f.readlines()
            for i in tqdm(range(len(infos)), desc='正在生成城市数据 :'):
                fullname, simple = infos[i].strip().split()
                self.possible_infos[simple] = self.GetNgarm(fullname)
                self.index2name[i] = (simple, fullname)
        self.file_logger.info('初始化城市信息完成！')
        return

    def GetNgarm(self, strs):
        res = set()
        for L in range(1, len(strs) + 1):
            for i in range(len(strs)):
                if i + L <= len(strs) and strs[i:i + L] not in res:
                    res.add(strs[i:i + L])

        res = sorted(list(set(res)), key=lambda x: len(x))
        return res

    def Search(self, info):
        self.file_logger.info('正在进行模糊查找...')
        final = []
        for i, value in enumerate(self.possible_infos.values()):
            if info in value:
                final.append(self.index2name[i])
        self.file_logger.info('查找完成!')
        if len(final) < 1:
            return "没找到对应的城市数据！", -1
        elif len(final) == 1:
            return "{} 的简称是 -> {}。".format(info, final[0][0]), final[0][1]
        else:
            return "你想找的是右边的哪一个：（{}）？".format("，".join([item[1] for item in final])), 0

    def log_init(self, log_file):
        self.file_logger = logging.getLogger('Search Engine')
        self.file_logger.setLevel('INFO')
        file_handler = logging.FileHandler(filename=log_file, mode='a', encoding='GBK')
        file_handler.setLevel('INFO')
        file_handler.setFormatter(logging.Formatter('[%(name)s]- %(asctime)s - [%(levelname)s]: %(message)s'))
        self.file_logger.addHandler(file_handler)

    def record(self, info):
        self.file_logger.info(info)


class DB:
    def __init__(self, db_file, infos_file=None):
        self.curr_idx = 0
        self.db_file = db_file
        if not os.path.exists(self.db_file):
            self.create_sheet()
            self.upload_data(infos_file)
        else:
            conn = sqlite3.connect(self.db_file)
            cursor = conn.cursor()
            sql = "select id from city"
            cursor.execute(sql)
            ll = [idx[0] for idx in cursor.fetchall()]
            self.curr_idx = max(ll) + 1 if len(ll) > 0 else 0


    def search(self, city):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        sql = "select * from city where city.name ='" + city + "'"
        cursor.execute(sql)
        res = cursor.fetchall()
        conn.close()
        # print(res)
        return res

    def upload_data(self, info_file):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        with open(info_file, 'r', encoding='gbk') as f:
            for line in tqdm(f.readlines(), desc='writing to database...'):
                infos = line.replace('\n', '').split(',')
                infos = tuple([self.curr_idx] + infos)
                cursor.execute("insert into city values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", infos)
                self.curr_idx += 1
            conn.commit()
            conn.close()

    def create_sheet(self):
        print('start creating database...')
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        cursor.execute("create table IF NOT EXISTS city "
                       "(id integer primary key,"
                       "name varchar(20),"
                       "loc varchar(20),"
                       "huxing varchar(30),"
                       "mianji varchar(30),"
                       "chaoxiang varchar(30),"
                       "zhuangxiu varchar(30),"
                       "louceng varchar(30),"
                       "jiegou varchar(30),"
                       "price varchar(30))")
        conn.commit()
        conn.close()


    def getNums(self):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        sql = "select name from city"
        cursor.execute(sql)
        res = cursor.fetchall()
        res = Counter(res)
        conn.close()
        return res


    def refresh(self, file_name):
        self.upload_data(file_name)


class Spyider:


    def run(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.55'
        }

        cities = {}
        with open('ori_info.txt', 'r', encoding='utf-8') as f:
            infos = f.readlines()
            for i in range(len(infos)):
                fullname, simple = infos[i].strip().split()
                cities[simple.lower()] = fullname
        print(cities)

        start = False
        with open('cities.csv', 'w', encoding='gbk') as my_csv:
            res = []
            for simple, city in tqdm(cities.items()):

                # if simple.lower() == 'xn':
                #     start = True
                # if not start: continue
                try:
                    print(city)
                    for page in range(1, 3):
                        if page == 1:
                            page = ''
                        url = f'https://{simple}.lianjia.com/ershoufang/pg' + str(page) + '/'
                        # print(url)
                        response = requests.get(url=url, headers=headers)  # 向网站发起请求，并获取响应对象
                        # print(page_text)
                        html = etree.HTML(response.text)
                        for j in range(1, 31):
                            loc = html.xpath(f'//*[@id="content"]/div[1]/ul/li[{j}]/div[1]/div[2]/div/a[1]/text()')[0]
                            infos = str(html.xpath(f'//*[@id="content"]/div[1]/ul/li[{j}]/div[1]/div[3]/div/text()')[0])
                            price = str(
                                html.xpath(f'//*[@id="content"]/div[1]/ul/li[{j}]/div[1]/div[6]/div[1]/span/text()')[0])
                            others = [item.strip().replace(',', ' ') for item in infos.split(' | ')]
                            if len(others) == 6:
                                pass
                            else:
                                others = [others[i] for i in range(5)] + ["_".join(others[5:])]
                            res.append([city, loc] + others + [price + '万'])
                            my_csv.write(",".join(res[-1]) + '\n')
                        time.sleep(0.25 + random.random() * 1)
                except:
                    pass


if __name__ == '__main__':
    sp = Spyider()
    sp.run()




