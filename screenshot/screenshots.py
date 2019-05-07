#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
import time
import os
import settings


class Screenshots(object):

    def __init__(self):
        """

        """
        self.carrier_code = ''
        self.storage_dir = settings.STORAGE_DIR
        self.browser = None
        self.wait = None

    def init_browser(self, browser):
        """
        :return:
        """
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 30)

    def open(self, url):
        """

        :param url:
        :return:
        """
        self.browser.delete_all_cookies()
        self.browser.get(url)

    def get_shot_as_file(self, tracking_number, human_order_id, send_time):
        """

        :param tracking_number:
        :param human_order_id:
        :param send_time:
        :return:
        """
        url = settings.CARRIER_SITE_DICT.get(self.carrier_code)
        if url.find('%s') > -1:
            self.open(url % tracking_number)
        else:
            self.open(url)

        self.shot(tracking_number, send_time)
        time.sleep(3)
        dir_path = self.get_dir_path(send_time)
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)

        file_name = self.get_file_path(tracking_number, human_order_id, send_time)
        file_path = os.path.join(dir_path, file_name)
        self.browser.get_screenshot_as_file(file_path)

        if len(self.browser.window_handles) > 1:
            self.browser.close()

    def get_file_path(self, tracking_number, human_order_id, send_time):
        """

        :param tracking_number:
        :param human_order_id:
        :param send_time:
        :return:
        """
        dir_path = self.get_dir_path(send_time)
        file_name = human_order_id + '_' + tracking_number + '.png'
        return os.path.join(dir_path, file_name)

    def get_dir_path(self, send_time):
        """

        :param send_time:
        :return:
        """
        return os.path.join(self.storage_dir, send_time.strftime('%Y-%m-%d'))

    def shot(self, tracking_number, send_time=None):
        """
        
        :param tracking_number: 
        :param send_time: 
        :return: 
        """
        raise NotImplementedError


class AuPostShots(Screenshots):
    """
    """

    def __init__(self):
        """

        """
        Screenshots.__init__(self)
        self.carrier_code = 'aupost'

    def shot(self, tracking_number, send_time=None):
        """

        :return:
        """
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="details"]')))


class DePostShots(Screenshots):
    """
    """

    def __init__(self):
        """

        """
        Screenshots.__init__(self)
        self.carrier_code = 'depost'

    def shot(self, tracking_number, send_time=None):
        """

        :return:
        """
        url = settings.CARRIER_SITE_DICT.get(self.carrier_code)
        self.open(url)

        element = self.wait.until(EC.presence_of_element_located((By.NAME, 'form.sendungsnummer')))
        element.clear()
        element.send_keys(tracking_number)

        Select(self.browser.find_element_by_id("form_einlieferungsdatum_monat")).select_by_index(send_time.month)
        Select(self.browser.find_element_by_id("form_einlieferungsdatum_tag")).select_by_index(send_time.day)
        Select(self.browser.find_element_by_id("form_einlieferungsdatum_jahr")).select_by_value(str(send_time.year))

        submit = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@href="JavaScript: bzlSearchSubmit()"]')))
        time.sleep(3)
        submit.click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="dp-table native-swipeable"]')))


class DHLShots(Screenshots):
    """
    """

    def __init__(self):
        """

        """
        Screenshots.__init__(self)
        self.carrier_code = 'dhl'

    def shot(self, tracking_number, send_time=None):
        """

        :return:
        """
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="tracking-result-header cl"]')))


class DHLDEShots(Screenshots):
    """
    """

    def __init__(self):
        """

        """
        Screenshots.__init__(self)
        self.carrier_code = 'dhl(de)'

    def shot(self, tracking_number, send_time=None):
        """

        :return:
        """
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//span[@class="mm_shipmentNameLabel"]')))


class DPDShots(Screenshots):
    """
    """

    def __init__(self):
        """

        """
        Screenshots.__init__(self)
        self.carrier_code = 'dpd'

    def shot(self, tracking_number, send_time=None):
        """

        :return:
        """
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//td[@translate="GUI_DELIVERY_STATUS"]')))


class DPDUKShots(Screenshots):
    """
    """

    def __init__(self):
        """

        """
        Screenshots.__init__(self)
        self.carrier_code = 'dpd(uk)'

    def shot(self, tracking_number, send_time=None):
        """

        :return:
        """
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="module-heading panel-dpd-red"]')))


class EMSShots(Screenshots):
    """
    """

    def __init__(self):
        """

        """
        Screenshots.__init__(self)
        self.carrier_code = 'ems'

    def shot(self, tracking_number, send_time=None):
        """

        :return:
        """
        pass


class FedexShots(Screenshots):
    """
    """

    def __init__(self):
        """

        """
        Screenshots.__init__(self)
        self.carrier_code = 'fedex'

    def shot(self, tracking_number, send_time=None):
        """

        :return:
        """
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="details"]')))


class P2PShots(Screenshots):
    """
    """

    def __init__(self):
        """

        """
        Screenshots.__init__(self)
        self.carrier_code = 'p2p'

    def shot(self, tracking_number, send_time=None):
        """

        :return:
        """
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//table[@class="display-ml"]')))


class ParcelForceShots(Screenshots):
    """
    """

    def __init__(self):
        """

        """
        Screenshots.__init__(self)
        self.carrier_code = 'parcelforce'

    def shot(self, tracking_number, send_time=None):
        """

        :return:
        """
        window_handles = self.browser.window_handles
        for handle in window_handles:
            if handle != self.browser.current_window_handle:
                self.browser.switch_to_window(handle)
                break

        url = settings.CARRIER_SITE_DICT.get(self.carrier_code)
        self.open(url)

        element = self.wait.until(EC.presence_of_element_located((By.NAME, 'szShippingNumber')))
        element.clear()
        element.send_keys(tracking_number)
        submit = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@onfocus="sz_Focus=\'trackButton\'"]')))
        time.sleep(3)
        submit.click()
        time.sleep(3)

        window_handles = self.browser.window_handles
        for handle in window_handles:
            if handle != self.browser.current_window_handle:
                self.browser.switch_to_window(handle)
                break


class RoyalMailShots(Screenshots):
    """
    """

    def __init__(self):
        """

        """
        Screenshots.__init__(self)
        self.carrier_code = 'royalmail'

    def shot(self, tracking_number, send_time=None):
        """

        :return:
        """
        pass


class TNTShots(Screenshots):
    """
    """

    def __init__(self):
        """

        """
        Screenshots.__init__(self)
        self.carrier_code = 'tnt'

    def shot(self, tracking_number, send_time=None):
        """

        :return:
        """
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, '__u-screen-only')))
        self.browser.execute_script("window.scrollBy(0,400)")


class TollShots(Screenshots):
    """
    """

    def __init__(self):
        """

        """
        Screenshots.__init__(self)
        self.carrier_code = 'toll'

    def shot(self, tracking_number, send_time=None):
        """

        :return:
        """
        self.wait.until(EC.presence_of_element_located((By.ID, 'dashboard-features-info')))


class UPSShots(Screenshots):
    """
    """

    def __init__(self):
        """

        """
        Screenshots.__init__(self)
        self.carrier_code = 'ups'

    def shot(self, tracking_number, send_time=None):
        """

        :return:
        """
        element = self.wait.until(EC.presence_of_element_located((By.ID, 'stApp_trackingNumber')))
        element.send_keys(tracking_number)
        submit = self.wait.until(EC.element_to_be_clickable((By.ID, 'stApp_btnTrack')))
        submit.click()
        self.wait.until(EC.presence_of_element_located((By.ID, 'stApp_lblTrackingNumber')))


class USPSShots(Screenshots):
    """
    """

    def __init__(self):
        """

        """
        Screenshots.__init__(self)
        self.carrier_code = 'usps'

    def shot(self, tracking_number, send_time=None):
        """

        :return:
        """
        pass


def generate_screenshots_dict():
    screenshots_dict = dict()
    for carrier_code, cls in settings.SCREENSHOTS_DICT.items():
        try:
            shots = globals()[cls]()
            screenshots_dict[carrier_code] = shots
        except Exception as e:
            print(e.args)
    return screenshots_dict
