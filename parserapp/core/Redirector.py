from selenium import webdriver

class Redirector():

    driver:webdriver.Chrome

    def __init__(self, driver:webdriver.Chrome):
        self.initial = 1

        self.driver = driver

    def redirect(self, url:str)->None:
        self.driver.get(url)