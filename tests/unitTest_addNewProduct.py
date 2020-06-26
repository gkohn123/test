import unittest
import time
from selenium import webdriver
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
        driver.get("http://gkohn.pythonanywhere.com/admin/login/?next=/admin/")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        time.sleep(3)
        elem.send_keys(Keys.RETURN)
        driver.get("http://gkohn.pythonanywhere.com/admin/login/?next=/admin/")
        time.sleep(3)
        # assert "Logged in"

        driver.get("http://gkohn.pythonanywhere.com/admin/shop/category/add/")
        time.sleep(3)
        elem = driver.find_element_by_id("id_name")
        elem.send_keys("Desserts")
        time.sleep(3)
        elem = driver.find_element_by_name("_save").click()
        time.sleep(3)
        time.sleep(3)

    time.sleep(3)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()