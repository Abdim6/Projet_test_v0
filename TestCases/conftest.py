"""
Objectif : Rassembler tous les bout de code/step utilisés plusieurs fois
Dernière mise à jour importante : 10/03/2022
Owner : Abdi
"""

from random import random
import pytest
# import string
from PageObjects.ObPage import LoginmaPage
from PageObjects.HomePage import HomePage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


##### Un setup qui lance le driver et qui charge l'application AVEC connexion + un tearndown qui kill le driver à la fin de test #####
@pytest.fixture
def setup_AvecConnexionUser():
    baseURL = ReadConfig.getApplicationURL()
    driver=webdriver.Chrome()
    print("")
    print("Nous utilisons Chrome ......")
    # driver.implicitly_wait(3)
    driver.maximize_window()
    driver.get(baseURL)
    
    logger = LogGen.loggen()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()
    logger.info("***************** DEBUT - De la connexion ****************")
    
    "Cliquer sur la modale + btn mon compte"
    hp=HomePage(driver)
    hp.clickaccepterTCF() 
    # time.sleep(2)
    # hp.clickaccepterConsent()
    time.sleep(2)
    hp.clickMonCompteBtn() 
    time.sleep(2)

    "Saisi des ID dans OB"
    lp=LoginmaPage(driver) 
    lp.setUsername(username)
    time.sleep(1)
    lp.setPassword(password)
    time.sleep(1)
    lp.clickLogin()   
    time.sleep(2)

    logger.info("***************** FIN - Connexion User ****************")

    yield driver

    driver.quit()


##### Un setup qui lance le driver et charge l'application sans connexion + un tearndown qui kill le driver à la fin de test #####
@pytest.fixture
def setup_SansConnexionUser():
    baseURL = ReadConfig.getApplicationURL()
    driver=webdriver.Chrome()
    print("")
    print("Nous utilisons Chrome ......")
    # driver.implicitly_wait(3)
    driver.maximize_window()
    driver.get(baseURL)
    hp=HomePage(driver)
    hp.clickaccepterTCF() 
    time.sleep(2)
    "Une feature(page) desactivée mais qui reviendra bientôt"
    # hp.clickaccepterConsent()
    # time.sleep(2)

    yield driver

    driver.quit()

##### Un setup qui lance le driver seulement + un tearndown qui kill le driver à la fin de test #####
@pytest.fixture
def setup_3():
    driver=webdriver.Chrome()
    print("")
    print("Nous utilisons Chrome ......")
    # driver.implicitly_wait(3)
    driver.maximize_window()

    yield driver

    driver.quit()

######## Un setup qui lance le driver ##########
@pytest.fixture
def setup_2():
    driver=webdriver.Chrome()
    print("")
    print("Nous utilisons Chrome ......")
    driver.maximize_window()
    return driver

############### Un setup pour lancer le driver + permet de choisir le browser au choix #############
@pytest.fixture
def setup_1(browser):
    if browser == "chrome":
        driver=webdriver.Chrome()
        print("")
        print("Nous utilisons CHROME ......")
    elif browser == "firefox":
        driver=webdriver.Firefox()
        print("")
    else:
        driver=webdriver.Safari()
        print("")
        print("Nous utilisons IE ......")
    driver.maximize_window()
    return driver

############# Config pour le choix de browser souhaité : ###############
def pytest_addoption(parser):   #this will ger rhe value from CLI/hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  #this will return the browser value to setup method
    return request.config.getoption("--browser")

##################### Pytest HTML Report ########################

"Ceci est UNIQUEMENT des paramètrages dans le rapport d'exécution HTML"
"It is hook for adding environment info to HTML Reports"
def pytest_configure(config):
    config._metadata['Project Name'] = '6 play'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Abdi'

"It is hook for delete/Modify Environment info to HTML Report"
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

def pytest_html_report_title(report):
    report.title = "My very own title!"

class action_OnElem():

    # this function is called every time a new object of the base class is created.
    def __init__(self, driver):
        self.driver=driver

    # this function performs click on web element whose locator is passed to it.
    def click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()
    
    # this function asserts comparison of a web element's text with passed in text.
    def assert_element_text(self, by_locator, element_text):
        web_element=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        assert web_element.text == element_text

    # this function performs text entry of the passed in text, in a web element whose locator is passed to it.
    def enter_text(self, by_locator, text):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    # this function checks if the web element whose locator has been passed to it, is enabled or not and returns
    # web element if it is enabled.
    def is_enabled(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))

    # this function checks if the web element whose locator has been passed to it, is visible or not and returns
    # true or false depending upon its visibility.
    def is_visible(self,by_locator):
        element=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)
    
    # this function moves the mouse pointer over a web element whose locator has been passed to it.
    def hover_to(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        ActionChains(self.driver).move_to_element(element).perform()

    def select_InList(self,by_locator,index):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        drp = Select(element)
        drp.select_by_index(index)