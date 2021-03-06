"""
Objectif : Rassembler tous les bout de code/step utilisés plusieurs fois
Dernière mise à jour importante : 10/03/2022
Owner : Abdi
"""

import random
import pytest
# import string
from PageObjects.ObPage import Page_OB_Connexion
from PageObjects.HomePage import HomePage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen

import time
from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select
from faker import Faker
import datetime
import string


##### Un setup qui lance le driver et qui lance l'application AVEC connexion + un tearndown qui kill le driver à la fin de test #####
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
    lp=Page_OB_Connexion(driver) 
    lp.setUsername(username)
    time.sleep(1)
    lp.setPassword(password)
    time.sleep(1)
    lp.clickLogin()   
    time.sleep(2)

    logger.info("***************** FIN - Connexion User ****************")

    yield driver
    driver.quit()


##### Un setup qui lance le driver et lance l'application sans connexion + un tearndown qui kill le driver à la fin de test #####
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
# lance l'app sans être connecté 
@pytest.fixture
def setup_1(browser):
    baseURL = ReadConfig.getApplicationURL()
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
    # return driver
    "------------------"
    driver.get(baseURL)
    
    logger = LogGen.loggen()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()
    logger.info("***************** DEBUT - De la connexion ****************")
    
    "Cliquer sur la modale + btn mon compte"
    hp=HomePage(driver)
    hp.clickaccepterTCF() 
  
    logger.info("***************** FIN - Connexion User ****************")
    "-------------------"
    yield driver

    driver.quit()

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


#Génération d'une date de naissance random - date naissance User Majeur 
def genere_date():
    fake = Faker()
    random_date_en = fake.date_between(start_date='-50y', end_date='-16y')
    random_date_fr = datetime.datetime.strftime(random_date_en, '%d/%m/%Y')
    return random_date_fr

def genere_IdRandom():
    letters = string.ascii_lowercase
    letters_upper = string.ascii_uppercase
    rand_string = "".join(random.choice(letters) for i in range(15))
    rand_mail = rand_string + "@gmail.com"
    rand_password_lower = "".join(random.choice(letters) for i in range(5))
    rand_password_upper = "".join(random.choice(letters_upper) for i in range(5))
    rand_pwd = rand_password_lower+rand_password_upper + str(5)
    return rand_mail,rand_pwd



    ############### Un setup pour lancer le driver + permet de choisir le browser au choix #############
# lance l'app Avec user connecté 
@pytest.fixture
def setup_11(browser):
    baseURL = ReadConfig.getApplicationURL()
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
    # return driver
    "------------------"
    driver.get(baseURL)
    
    logger = LogGen.loggen()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()
    logger.info("***************** DEBUT - De la connexion ****************")
    
    "Cliquer sur la modale + btn mon compte"
    hp=HomePage(driver)
    hp.clickaccepterTCF() 
    
    time.sleep(2)
    hp.clickMonCompteBtn() 
    time.sleep(2)

    "Saisi des ID dans OB"
    lp=Page_OB_Connexion(driver) 
    lp.setUsername(username)
    time.sleep(1)
    lp.setPassword(password)
    time.sleep(1)
    lp.clickLogin()   
    time.sleep(2)

    logger.info("***************** FIN - Connexion User ****************")
    "-------------------"
    yield driver

    driver.quit()
