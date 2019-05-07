#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymysql
from settings import DB_PARAMS


class TrackingDAO(object):

    @staticmethod
    def get_tracking_list(start_time, tracking_status):
        # 连接数据库
        connect = pymysql.Connect(**DB_PARAMS)

        # 获取游标
        cursor = connect.cursor()

        # sql
        sql = """
        select 
        package_tracking.`carrier_code`, package_tracking.`send_time`, package_tracking.`track_code` 
        from package_tracking where package_tracking.`status`=%s and package_tracking.`send_time` >= '%s' 
        and package_tracking.`track_code` >= 'depost' 
        order by package_tracking.`send_time` desc;"""
        sql = sql % (tracking_status, start_time)

        # 执行sql
        cursor.execute(sql)

        # 获取所有的数据
        rows = cursor.fetchall()
        print(len(rows))

        return rows

    @staticmethod
    def get_tracking_order(track_code):
        # 连接数据库
        connect = pymysql.Connect(**DB_PARAMS)

        # 获取游标
        cursor = connect.cursor()

        # sql
        sql = """
            select 
            report_orders.`tracking_number`, report_orders.`human_order_id` 
            from report_orders where report_orders.`tracking_number`='%s';"""
        sql = sql % track_code

        # 执行sql
        cursor.execute(sql)

        # 获取所有的数据
        rows = cursor.fetchall()
        print(len(rows))

        return rows

# sql = """
#                         select
#                         report_orders.`tracking_number`, report_orders.`human_order_id`,
#                         package_tracking.`carrier_code`, package_tracking.`send_time`
#                         from package_tracking
#                                 join report_orders on report_orders.`tracking_number`=package_tracking.`track_code`
#                                 where package_tracking.`status`=%s and package_tracking.send_time >= '%s'
#             order by package_tracking.send_time desc;"""
