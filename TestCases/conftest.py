"""
Objectif : De rassembler tous les bout de code/step reutilisés plusieurs fois
Dernière mise à jour importante : 10/03/2022
Owner : Abdi
"""

from random import random
from selenium import webdriver
import pytest
import string

##### Un setup qui lance le driver + le tearndown qui kill le driver à la fin de test #####
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
############### Un setup pour lancer le driver + choisir le browser au choix #############
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

############# Un setup pour lancer le driver avec le browser souhaité : ###############
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