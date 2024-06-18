import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from Config.config import TestData


@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        #web_driver = webdriver.Chrome(ChromeDriverManager().install())
        '''service = Service(executable_path=TestData.CHROME_EXECUTABLE_PATH)

        options = webdriver.ChromeOptions()
        web_driver = webdriver.Chrome(options=options)'''
    if request.param == "firefox":
        web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    request.cls.driver=web_driver
    yield
    web_driver.close()