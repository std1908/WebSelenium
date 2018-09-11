#coding=utf-8

from selenium import webdriver
import unittest
import sys
import logging

# logger
logger = logging.getLogger()
logFormatter = logging.Formatter(
    '[%(asctime)-15s][%(filename)s][%(funcName)s#%(lineno)d] %(message)s')
ch = logging.StreamHandler(sys.stdout)
ch.setFormatter(logFormatter)
logger.addHandler(ch)
logger.setLevel(logging.INFO)

class BaseTests(unittest.TestCase):
    """
    The base class is for all testcase.
    """
    def setUp(self):
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless')
        # options.add_argument('--no-sandbox')
        # options.add_argument('--disable-gpu')

        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(10)
        self.driver.get("https://www-staging.soocii.me")
        self.action = webdriver.ActionChains(self.driver)
        
    def tearDown(self):

        self.driver.close()

        self.driver.quit()
