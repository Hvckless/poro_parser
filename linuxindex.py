from enum import Enum

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

import importlib
import shlex

from parserapp.parser.ChampionParser import ChampionParser
from parserapp.parser.ChampionBuildParser import ChampionBuildParser
from parserapp.core.Redirector import Redirector
from parserapp.command.CommandHandler import CommandHandler
from parserapp.file.JSONHandler import JSONHandler

from parserapp.type.Champion import Champion

from parserapp.enums.CMDStatus import CMDStatus




class Main():

    driver:webdriver.Chrome 
    options:Options


    redirector:Redirector
    cmdHandler:CommandHandler
    

    DATA_SOURCE_SERVER_URL:str = "https://naver.com"
    CHAMPION_LIST_SOURCE_SERVER_URL:str = "https://poro.gg/champions?gameMode=aram&hl=ko-kr"

    def __init__(self):
        self.initial = 1

        self.initialDriverOption()
        self.initialWebDriver()

        self.initialRedirector()
        self.initialCMDHandler


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

            if(len(arguments) < 1):
                self.cmdHandler.error_invalid_parameter()
                return
            
            self.driver.get(arguments[0])
        elif(command == "champions"):
            self.redirector.redirect(self.CHAMPION_LIST_SOURCE_SERVER_URL)
            champions:dict[str, Champion] = ChampionParser(self.driver).parseAllChampionNames()

            JSONHandler().createJSONFile("./champions/json.json", champions)

        elif(command == "findbuild"):
            if(len(arguments) < 1):
                self.cmdHandler.error_invalid_parameter()
                return

            ChampionBuildParser(driver=self.driver, data_path="./champions/json.json").parseChampionBuild(arguments[0])
            
            pass


    """
    커맨드 컨텍스트를 커맨드 컴포넌트 구조로 변환
    """
    def parseCommandComponent(self, context:str)->list[str]:
        return shlex.split(context)

    def initialDriverOption(self)->None:
        self.options = Options()
        self.options.add_argument("--headless")
        self.options.add_argument("--no-sandbox")
        self.options.add_argument("--disable-dev-shm-usage")
        pass

    def initialWebDriver(self)->None:
        self.driver = webdriver.Chrome(self.options)
        pass

    def initialRedirector(self)->None:
        self.redirector = Redirector(self.driver)
        pass

    def initialCMDHandler(self)->None:
        self.cmdHandler = CommandHandler(self.driver)
        pass
    







app:Main = Main()
