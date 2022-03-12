"CE FICHIER A POUR BUT DE FAIRE UN TEST SUR UN FIXTURE QUI OUVRE PUIS FERME LE DRIVER"
"Très interessent avoir un setup et un tearndown en commun avec tous les cdt - voir dans conftest"


# from lib2to3.pgen2 import driver
# import pytest 
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


# @pytest.yield_fixture()
# def setUp(): 
#     print("opening URL ta Login") 
#     yield
#     print("Closing browser after Login") 

# def test_loginByemail(setUp): 
#     print("this is Login by email test") 
# def test_loginbyfacebook(setUp): 
#     print("this is Login by facebook test")

# def test_homePageTitle(setup_3):
#         driver = setup_3
#         driver.get("https://www.google.com")
#         time.sleep(5)
#         print("ATTENDRE 5 SEC ...")

# driver = webdriver.Chrome()
# driver.get("https://www.6play.fr")
# time.sleep(5)
# driver.find_element(By.XPATH,"#__brk > div > div.n913wo-5.cuyMWW > div.n913wo-4.fCmDdf > div > header > div > div > nav > div.m4392j-1.imWKGD > ul > li:nth-child(5) > button").click()
# driver.find_element(By.CSS_SELECTOR,"#__brk > div > div.n913wo-5.cuyMWW > div.n913wo-4.fCmDdf > div > main > aside > nav > ul > li:nth-child(3) > a > span").click()
    
# time.sleep(5)
# monEmail = driver.find_element(By.ID, "email")
# import pdb; pdb.set_trace()

# monEmail.value

# content of ./test_smtpsimple.py


###################################################

# def setup_module(module):
#     print("\n--> Setup module")

# def teardown_module(module):
#     print("--> Teardown module")

# class TestClass:
#     @classmethod
#     def setup_class(cls):
#         print("--> Setup class")

#     @classmethod
#     def teardown_class(cls):
#         print("--> Teardown class")

#     def setup_method(self, method):
#         print("--> Setup method")

#     def teardown_method(self, method):
#         print("\n--> Teardown method")

#     def test_one(self):
#         print("--> Run first test")

#     def test_two(self):
#         print("--> Run second test")

import pytest
from selenium import webdriver
from PageObjects.ObPage import LoginmaPage
from PageObjects.HomePage import HomePage
import time
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from TestCases.conftest import Connexion
# from testCases import conftest 


"ce bloc devrait se trouver dans un setup, en commun pour tous les tests"
class Test_001_Login:
    logger = LogGen.loggen()

    def test_homePageTitle(self, setup_4):
        # self.driver = setup_4
        self.logger.info("***************** DEBUT - Test_001_Login ****************")
        Connexion.Seconnecter(self, setup_4)
        self.logger.info("***************** FIN - Test_001_Login ****************")
        self.driver.close()
"""
re exécuter ce test puis analyser le resultat obtenu - des tests effectués avec la connexion mise dans conftest
"""
