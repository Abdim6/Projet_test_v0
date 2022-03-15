"""
Objectif : De rassembler tous les bout de code/step reutilisés plusieurs fois
Dernière mise à jour importante : 10/03/2022
Owner : Abdi
"""

from random import random
from selenium import webdriver
import pytest
import string
from PageObjects.ObPage import LoginmaPage
from PageObjects.HomePage import HomePage
import time
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen

##### Un setup qui lance le driver et charge l'application AVEC connexion + un tearndown qui kill le driver à la fin de test #####
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

    "Vérification sur retour Home page"
    hp.clickHomeBtn()
    time.sleep(2)
    hp.checkObjetHomePage()
    time.sleep(2)
    logger.info("***************** FIN - Connexion User ****************")

    yield driver

    driver.quit()


##### Un setup qui lance le driver et charge l'application + un tearndown qui kill le driver à la fin de test #####
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
    # hp.clickaccepterConsent()
    # time.sleep(2)

    yield driver

    driver.quit()

##### Un setup qui lance le driver + un tearndown qui kill le driver à la fin de test #####
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

######################## Classe connexion Générique #######################

# class Connexion():
#     logger = LogGen.loggen()
#     username = ReadConfig.getUserEmail()
#     password = ReadConfig.getUserPassword()
    
#     def Seconnecter (self,setup_4):
#     # def test_homePageTitle(self,setup_4,username,password):
#         self.logger.info("***************** DEBUT - De la connexion ****************")
#         self.driver = setup_4

#         # act_title = self.driver.title
#         # time.sleep(2)
#         # if act_title == "6play, regardez des programmes TV en Replay ou en Direct":
#         #     self.logger.info("***************** Test titre de la page OK ****************")
#         #     assert True
#         # else:
#         #     print(act_title)
#         #     self.driver.save_screenshot(".\screenshot\\"+"page_title_1.png")
#         #     self.logger.error("***************** Test titre de la page KO ****************")
#         #     assert False
        
#         "Cliquer sur la modale + btn mon compte"
#         self.hp=HomePage(self.driver)
#         self.hp.clickaccepterTCF() 
#         time.sleep(2)
#         self.hp.clickMonCompteBtn() 
#         time.sleep(2)

#         "Saisi des ID dans OB"
#         self.lp=LoginmaPage(self.driver) 
#         self.lp.setUsername(Connexion.username)
#         time.sleep(1)
#         self.lp.setPassword(Connexion.password)
#         time.sleep(1)
#         self.lp.clickLogin()   
#         time.sleep(2)

#         "Vérification sur retour Home page"
#         self.hp.clickHomeBtn()
#         time.sleep(2)
#         self.hp.checkObjetHomePage()
#         time.sleep(2)
#         self.logger.info("***************** FIN - Connexion User ****************")
############################################ 
