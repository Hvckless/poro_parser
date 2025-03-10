from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from parserapp.type.Champion import Champion

class ChampionParser():

    driver:webdriver.Chrome

    def __init__(self, driver:webdriver.Chrome):
        self.initial = 1

        self.driver = driver


    def parseAllChampionNames(self)->dict[str, Champion]:
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#content-container > div > div.flex.flex-wrap.items-start.gap-0.p-x-2 > section > ul > li:nth-child(170) > a > span"))
            )

            champion_elements = self.driver.find_elements(By.CSS_SELECTOR, ".mx-auto.min-w-64px")

            #return에 사용할 빈 딕셔너리
            champion_dictionary:dict[str, Champion] = {}

            #모든 챔피언 목록에 대해 반복
            for champion_element in champion_elements:

                

                champion_anchor_element = champion_element.find_element(By.TAG_NAME, "a")
                champion_name_element = champion_element.find_element(By.XPATH, ".//span[contains(@class, 'w-full') and contains(@class, 'text-[#999]') and contains(@class, 'text-12px') and contains(@class, 'text-center') and contains(@class, 'leading-16px') and contains(@class, 'ellipsis')]")
                champion_portrait_element = champion_element.find_element(By.CSS_SELECTOR, "div[role=img]")
                champion_portrait_css_style:str = champion_portrait_element.get_attribute("style")
                
                
                #None 검증을 위해 source_url 선추출
                champion_source_url:str|None = champion_anchor_element.get_attribute("href")

                _champion:Champion

                #print(f"챔피언 이름 : {champion_name_element.text} / 초상화 URL : {champion_source_url} 초상화 CSS : {champion_portrait_css_style}")

                #None을 검증하여 champion_dictionary 구성
                if champion_source_url is not None:
                    #champion_dictionary[champion_name_element.text] = champion_source_url
                    _champion = Champion(champion_name_element.text, champion_source_url, champion_portrait_css_style)
                else:
                    #champion_dictionary[champion_name_element.text] = "ERR"
                    _champion = Champion(champion_name_element.text, "ERR", "ERR_CSS")

                champion_dictionary[champion_name_element.text] = _champion.__dict__


            return champion_dictionary

        except TimeoutException as e:
            return {"response":"timeout"}