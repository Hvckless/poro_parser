import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class ChampionBuildParser():

    driver:webdriver.Chrome
    data_path:str

    url:str

    def __init__(self, driver:webdriver.Chrome, data_path:str)->None:

        self.driver = driver
        self.data_path = data_path

        pass
    
    def parseChampionBuild(self, champion_name:str)->None:

        with open(self.data_path, "r") as json_data:
            some_vars = json.load(json_data)
            print(some_vars[champion_name]["source_url"])

            self.url = some_vars[champion_name]["source_url"]

        try:
            self.driver.get(self.url)

            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#content-container > main > div.px-2 > section:nth-child(2) > div.flex.gap-2.flex-col > div:nth-child(1) > div > div > table > tbody > tr:nth-child(8) > td:nth-child(1) > div > div:nth-child(3) > div > div"))
            )

            region = self.driver.find_element(By.CSS_SELECTOR, "#content-container > main > div.px-2 > section:nth-child(1) > ul > li.relative.w-\\[30\\%\\] > button")

            print(region.text)

            pass
        except TimeoutException as e:
            print(f"{e.stacktrace}")
            print("시간 초과")
            pass

        pass