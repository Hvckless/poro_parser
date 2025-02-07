from selenium import webdriver

class CommandHandler:

    driver:webdriver.Chrome


    def __init__(self, driver:webdriver.Chrome)->None:

        self.driver = driver

    def captureImg(self, args:list[str])->None:

        if(len(args) < 1):
            self.driver.save_screenshot("somefile.png")
        else:
            self.driver.save_screenshot(args[0])