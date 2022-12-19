import logging
import time

from selenium.webdriver import Keys
from utilities.Utils import utils
from base.basedriver import Basedriver
from selenium.webdriver.common.by import By
from configfiles.configuration_path import test_config
class launchpage(Basedriver):

    log = utils.customer_logging(logLevel=logging.DEBUG)
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
    def get_origin_city(self):
        return self.element_clickable(By.XPATH,test_config.depart_from)
    def get_all_origin_city(self):
        return self.presence_elements(By.XPATH,test_config.search_city)
    def get_depart_city(self):
        return self.element_clickable(By.XPATH, test_config.going_to)
    def get_all_depart_city(self):
        return self.presence_elements(By.XPATH,test_config.search_city)
    def get_calender(self):
        return self.element_clickable(By.XPATH,test_config.origin_date)
    def get_depart_date(self):
        return self.presence_elements(By.XPATH,test_config.date_search)
    def search_button(self):
        return self.element_clickable(By.XPATH,test_config.search_button)
    def Enter_search_origin(self,org):
        self.log.warning( f" origin city search  is {org}")
        self.get_origin_city().click()
        time.sleep(1)
        self.get_origin_city().send_keys(org)
        time.sleep(2)
        self.get_origin_city().send_keys(Keys.ENTER)
    def Enter_search_going_to(self,going):
        self.get_depart_city().click()
        time.sleep(1)
        self.get_depart_city().send_keys(going)
        time.sleep(2)
        self.get_depart_city().send_keys(Keys.ENTER)
    def Enter_search_date(self,trv_date):
        self.get_calender().click()
        time.sleep(2)
        all_dates=self.get_depart_date() #is ok
        # all_dates=self.get_depart_date().find_elements(By.XPATH,test_config.date_search) no ok
        time.sleep(2)
        # print(f"lenght of date {len(all_dates)}")
        self.log.warning(f"lenght of date is  {len(all_dates)}")
        for date in all_dates:
            if date.get_attribute("data-date")==trv_date:
                date.click()
                time.sleep(2)
                break

    def search_button_click(self):
        self.search_button().click()
        time.sleep(2)

    def search_flight(self,org,drp,date):
        self.Enter_search_origin(org)
        self.Enter_search_going_to(drp)
        self.Enter_search_date(date)
        # self.search_button_click()

