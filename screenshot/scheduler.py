#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import datetime
# import logging
import os
from multiprocessing import Process
from screenshot import generate_screenshots_dict
from selenium import webdriver
from .dao import TrackingDAO
import settings

# logger = logging.getLogger(__name__)
# logger = logger.setLevel(logging.INFO)


class Scheduler(object):

    @staticmethod
    def shot(cycle=settings.CYCLE):
        while True:
            # 开始时间
            start_time = datetime.datetime.now() - datetime.timedelta(days=settings.TRACKING_CYCLE)
            # 追踪状态
            tracking_status = settings.TRACKING_STATUS

            tracking_list = TrackingDAO.get_tracking_list(start_time, tracking_status)

            if len(tracking_list) > 0:
                browser = webdriver.Firefox()
                browser.maximize_window()
                screenshots_dict = generate_screenshots_dict()

                for carrier_code, send_time, track_code in tracking_list:
                    Scheduler.do_shot(browser, screenshots_dict, carrier_code, send_time, track_code)

                browser.close()
            # sleep
            time.sleep(cycle)

    @staticmethod
    def do_shot(browser, screenshots_dict, carrier_code, send_time, track_code):
        tracking_order = TrackingDAO.get_tracking_order(track_code)
        for tracking_number, human_order_id in tracking_order:
            # 追踪单
            print(tracking_number, human_order_id, send_time)
            try:
                shots = screenshots_dict.get(carrier_code.lower())
                if shots:
                    file_path = shots.get_file_path(tracking_number, human_order_id, send_time)
                    if os.path.exists(file_path):
                        pass
                    else:
                        shots.init_browser(browser)
                        shots.get_shot_as_file(tracking_number, human_order_id, send_time)
            except Exception as e:
                print(e.args)

    @staticmethod
    def run():
        process = Process(target=Scheduler.shot)
        process.start()
