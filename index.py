from enum import Enum

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import importlib
import shlex

from parserapp.parser.ChampionParser import ChampionParser
from parserapp.core.Redirector import Redirector
from parserapp.command.CommandHandler import CommandHandler
from parserapp.file.JSONHandler import JSONHandler

from parserapp.enums.CMDStatus import CMDStatus




class Main():

    driver:webdriver.Chrome = webdriver.Chrome()
    redirector:Redirector = Redirector(driver)
    cmdHandler:CommandHandler = CommandHandler(driver)

    DATA_SOURCE_SERVER_URL:str = "https://naver.com"
    CHAMPION_LIST_SOURCE_SERVER_URL:str = "https://poro.gg/champions?gameMode=aram"

    def __init__(self):
        self.initial = 1


        JSONHandler().createJSONFile("somejson.json", {})


        self.driver.get(self.DATA_SOURCE_SERVER_URL)



        #Start CommandLine Interrupt
        self.cliinterrupt()


    """
    CLI Interrupt의 시작점

    cliinterrupt -> commandDispatcher -> commandExecutor 순의 체인
    """
    def cliinterrupt(self)->None:
        while True:
            if self.commandDispatcher() is CMDStatus.EXIT:
                break



    """
    커맨드 발행자. 커맨드가 KEEP 상태일지 EXIT일지 정한다
    """
    def commandDispatcher(self)->CMDStatus:

        cmd:str = input("> ")

        if cmd == "exit":
            self.driver.quit()
            return CMDStatus.EXIT
        else:
            self.commandExecutor(cmd)
            return CMDStatus.KEEP

        

    """
    커맨드 실행자. 실제 커맨드를 실행하는 로직을 포함
    """
    def commandExecutor(self, cmd:str)->None:

        cmd_components:list[str] = self.parseCommandComponent(cmd)

        command:str = cmd_components[0]
        arguments:list[str]

        """
        인자 정렬
        """
        if(len(cmd_components) > 1):
            arguments = cmd_components[1:]
        else:
            arguments = []



        """
        명령어 실행 로직
        """
        if(command == "capture"):
            self.cmdHandler.captureImg(arguments)
        elif(command == "redirect"):

            if(len(arguments) < 0):
                return
            
            self.driver.get(arguments[0])
        elif(command == "champions"):
            self.redirector.redirect(self.CHAMPION_LIST_SOURCE_SERVER_URL)
            champions:dict[str, str] = ChampionParser(self.driver).parseAllChampionNames()

            #print([key for key in champions.keys()])

            JSONHandler().createJSONFile("./champions/json.json", champions)

            # champion_elements = self.driver.find_elements(By.CSS_SELECTOR, ".mx-auto.min-w-64px")

            # for champion_element in champion_elements:
            #     champion_name_anchor = champion_element.find_element(By.TAG_NAME, "a")
            #     print(champion_name_anchor.get_attribute('href'))

            # champion_names = [champion_element.text for champion_element in champion_elements]

            # print(champion_names)

    """
    커맨드 컨텍스트를 커맨드 컴포넌트 구조로 변환
    """
    def parseCommandComponent(self, context:str)->list[str]:
        return shlex.split(context)









app:Main = Main()
