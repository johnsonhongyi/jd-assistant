#!/usr/bin/env python
# -*- coding:utf-8 -*-
from jd_assistant import Assistant
import requests
import datetime,json,time
# import win32api
# import sys
# sys.path.insert(0,'C:\\Users\\Johnson\\Anaconda2\\envs\\pytorch_gpu\\Library\\bin')
# sys.path.append('C:\\Users\\Johnson\\Anaconda2\\envs\\pytorch_gpu\\Library\\bin')
# print(sys.path)
def setSystemTime():
    url = 'https://a.jd.com//ajax/queryServerData.html'
    session = requests.session()
    # get server time
    t0 = datetime.datetime.now()
    ret = session.get(url).text
    t1 = datetime.datetime.now()
    js = json.loads(ret)
    t = float(js["serverTime"]) / 1000
    dt = datetime.datetime.fromtimestamp(t) + ((t1 - t0) / 2)
    print("Time:",datetime.datetime.fromtimestamp(t),t1,dt)
    tm_year, tm_mon, tm_mday, tm_hour, tm_min, tm_sec, tm_wday, tm_yday, tm_isdst = time.gmtime(time.mktime(dt.timetuple()))
    msec = dt.microsecond / 1000
    # win32api.SetSystemTime(tm_year, tm_mon, tm_wday, tm_mday, tm_hour, tm_min, tm_sec, int(msec))
    print("jd:%snow:%s"%(session.get(url).text,datetime.datetime.now()))
setSystemTime()

if __name__ == '__main__':
    """
    重要提示：此处为示例代码之一，请移步下面的链接查看使用教程👇
    https://github.com/tychxn/jd-assistant/wiki/1.-%E4%BA%AC%E4%B8%9C%E6%8A%A2%E8%B4%AD%E5%8A%A9%E6%89%8B%E7%94%A8%E6%B3%95
    """
    # 下单里面要增加get_checkout_page_detail 否则默认地址不会生效 ，或者你改了默认地址之后 自己随便下一单，然后再进行秒杀

    '''
    Time: {"serverTime":1606211981804} 2020-11-24 17:59:41.559953
    jd:{"serverTime":1606211981839}now:2020-11-24 17:59:41.859895
    2020-11-24 17:59:42,005 INFO: 二维码获取成功，请打开京东APP扫描
    2020-11-24 17:59:42,362 INFO: Code: 201, Message: 二维码未扫描，请扫描二维码
    2020-11-24 17:59:44,377 INFO: Code: 201, Message: 二维码未扫描，请扫描二维码
    2020-11-24 17:59:46,394 INFO: Code: 201, Message: 二维码未扫描，请扫描二维码
    2020-11-24 17:59:48,411 INFO: Code: 201, Message: 二维码未扫描，请扫描二维码
    2020-11-24 17:59:50,427 INFO: Code: 201, Message: 二维码未扫描，请扫描二维码
    2020-11-24 17:59:52,442 INFO: Code: 201, Message: 二维码未扫描，请扫描二维码
    2020-11-24 17:59:54,471 INFO: Code: 201, Message: 二维码未扫描，请扫描二维码
    2020-11-24 17:59:56,485 INFO: Code: 201, Message: 二维码未扫描，请扫描二维码
    2020-11-24 17:59:58,498 INFO: Code: 201, Message: 二维码未扫描，请扫描二维码
    2020-11-24 18:00:00,513 INFO: Code: 201, Message: 二维码未扫描，请扫描二维码
    2020-11-24 18:00:02,530 INFO: Code: 202, Message: 请手机客户端确认登录
    2020-11-24 18:00:04,548 INFO: 已完成手机客户端确认
    2020-11-24 18:00:04,624 INFO: 二维码登录成功
    2020-11-24 18:00:04,693 INFO: 下单模式：['100001324422'] 任一商品有货并且未下架均会尝试下单
    2020-11-24 18:00:04,919 INFO: 100001324422 满足下单条件，开始执行
    2020-11-24 18:00:05,302 INFO: 购物车信息：{}
    2020-11-24 18:00:05,302 INFO: 100001324422 不在购物车中，开始加入购物车，数量 1
    2020-11-24 18:00:05,492 INFO: 100001324422 x 1 已成功加入购物车
    2020-11-24 18:00:05,492 INFO: 第[1/3]次尝试提交订单
    2020-11-24 18:00:05,842 INFO: 下单信息：{'address': '北京 朝阳区 平房乡   北京市朝阳区姚家园南路1号惠通时代广场9号院2号楼A区及B区二层后门', 'receiver': '邹弘 逸 185****1300', 'total_price': '149.00', 'items': []}
    2020-11-24 18:00:05,967 INFO: 订单提交成功! 订单号：133100118037
    2020-11-24 18:00:05,968 INFO: 第1次提交订单成功
    '''



    sku_ids = '100001324422'  # 商品id
    # sku_ids = '100016578654'  # 商品id 6800xt
    # sku_ids = '100012043978'  # 商品id 飞天
    area = '1_72_4211'  # 区域id
    asst = Assistant()  # 初始化
    asst.login_by_QRcode()  # 扫码登陆
    # asst.buy_item_in_stock(sku_ids=sku_ids, area=area, wait_all=False, stock_interval=5)  # 根据商品是否有货自动下单
    asst.submit_order_by_time(buy_time='2020-11-24 21:52:00.000', retry=4, interval=5)  # 根据商品是否有货自动下单
    # 6个参数：
    # sku_ids: 商品id。可以设置多个商品，也可以带数量，如：'1234' 或 '1234,5678' 或 '1234:2' 或 '1234:2,5678:3'
    # area: 地区id
    # wait_all: 是否等所有商品都有货才一起下单，可选参数，默认False
    # stock_interval: 查询库存时间间隔，可选参数，默认3秒
    # submit_retry: 提交订单失败后重试次数，可选参数，默认3次
    # submit_interval: 提交订单失败后重试时间间隔，可选参数，默认5秒
