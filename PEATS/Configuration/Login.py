from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from PEATS import Configuration
from selenium.webdriver.chrome.service import service, Service


# from webdriver_manager.chrome import ChromeDriverManager


class LoginPEATS:
    def __init__(self):
        self.driver = webdriver.Chrome(
            executable_path="C:\\Users\\Sreenivasulu_Bheeman\\PycharmProjects\\TestPythonRequest\\PEATS\\Drivers\\chromedriver.exe")

    def test_login(self):
       # options = webdriver.chromeoptions()
        #options.add_experimental_option("detach", True)
       # self.driver = webdriver.chrome()

        #self.driver = webdriver.Chrome(service=service(ChromeDriverManager().install()))
        self.driver.get("http://10.253.219.247/")

        while True:
            pass
        launchBrowser()

        self.driver.maximize_window()
        #self.driver.implicitly_wait(20)
        self.driver.find_element_by_name("username")
        self.driver.Sendkeys("username")

        self.driver.Sendkeys("{TAB}")
        self.driver.Sendkeys("username")



login_obj = LoginPEATS()
login_obj.test_login()
