import unittest
import time
from idlelib import browser
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class CMS_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_cms(self):
        user = "svlasnik"
        pwd = "maverick1a"

        driver = self.driver
        driver.maximize_window()
        driver.get("http://gkohn.pythonanywhere.com/")
        elem = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/a[2]").click()
        time.sleep(1)
        elem = driver.find_element_by_xpath("/html/body/div[3]/div/form/input[3]").click()
        time.sleep(1)
        elem = driver.find_element_by_xpath("/html/body/div[1]/a").click()
        time.sleep(1)
        elem = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/a[2]").click()
        time.sleep(1)
        elem = driver.find_element_by_xpath("/html/body/div[3]/div/form/input[3]").click()
        time.sleep(1)
        elem = driver.find_element_by_xpath("/html/body/div[3]/p/a[2]").click()
        time.sleep(1)
        elem = driver.find_element_by_id("id_first_name")
        elem.send_keys("Sandy")
        elem = driver.find_element_by_id("id_last_name")
        elem.send_keys("Vlasnik")
        elem = driver.find_element_by_id("id_email")
        elem.send_keys("test@email.com")
        elem = driver.find_element_by_id("id_address")
        elem.send_keys("1234 east omaha Road")
        elem = driver.find_element_by_id("id_postal_code")
        elem.send_keys("68144")
        elem = driver.find_element_by_id("id_city")
        elem.send_keys("Omaha")
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/ul/li/a").click()
        elem = driver.find_element_by_xpath("/html/body/div[3]/table/tbody/tr[1]/td[4]/a").click()
        time.sleep(5)

    time.sleep(3)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()