from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from BeautifulReport import BeautifulReport
from webdriver_manager.chrome import ChromeDriverManager
import time
import unittest

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option("prefs", {
    "profile.password_manager_enabled": False,
    "credentials_enable_service": False
})
                                
class Test(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(chrome_options=options)
        self.action = ActionChains(self.driver)
        self.URL = "https://youtube.com"
        self.driver.get(self.URL)
        self.driver.maximize_window()
    
    @classmethod
    def tearDownClass(self):
        self.driver.quit()
        
    def test_01_search(self):
        """
        前往Youtube網站後，搜尋Gura的影片
        """
        time.sleep(2)
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@id='search']"))
            )
        finally:
            time.sleep(2)

        input_search = self.driver.find_element_by_xpath("//input[@id='search']")
        input_search.send_keys("Gawr Gura 熟肉")
        button_search = self.driver.find_element_by_id("search-icon-legacy")
        button_search.click()
    
    def test_02_open_target(self):
        """
        在搜尋結果找到特定的影片並點進去
        """
        time.sleep(5)
        self.driver.execute_script("window.scrollBy(0,1200)")
        time.sleep(2)
        
        youtube_target = self.driver.find_element_by_xpath("//a[@href='/watch?v=9SfsF_6fY9c']")
        youtube_target.click()
        time.sleep(5)
        
    def test_03_back_to_list(self):
        """
        回上頁列表，重新整理網頁後，切換另一則影片，五秒後回到首頁
        """
        self.driver.back()
        time.sleep(2)
        self.driver.refresh()
        time.sleep(3)
        youtube_target = self.driver.find_element_by_xpath("//a[@href='/watch?v=MhVh01k_Wg0']")
        youtube_target.click()
        time.sleep(5)
        logo = self.driver.find_element_by_id("logo-icon")
        logo.click()
        time.sleep(5)

basedir = "D:/web/nocodenolife/2021_selenium"
if __name__ == '__main__':
    test_suite = unittest.defaultTestLoader.discover(basedir, pattern='*.py')
    result = BeautifulReport(test_suite)
    result.report(filename='report',description='我的第一個測試', log_path='D:/web/nocodenolife/2021_selenium')
                 