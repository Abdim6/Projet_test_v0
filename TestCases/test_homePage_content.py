"""
Objectif : tester certains contenu de la page homePage de 6play - hors connexion
Date de la dernière grosse maj : 12/03/2022
Owner : Abdi
"""
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from PageObjects.ObPage import LoginmaPage
from PageObjects.HomePage import HomePage
import time
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from selenium.webdriver.common.action_chains import ActionChains


"ce bloc devrait se trouver dans un setup, en commun pour tous les tests"
class Test_003_Login:
    
    baseURL = "https://www.6play.fr/"
    logger = LogGen.loggen()

    def test_homePageTitle(self,setup_2):
        self.logger.info("***************** DEBUT - Test_003_Login ****************")
        self.driver = setup_2
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        time.sleep(2)
        if act_title == "6play, regardez des programmes TV en Replay ou en Direct":
            self.logger.info("***************** Test titre de la page OK ****************")
            assert True
            # self.driver.close()
        else:
            print(act_title)
            self.driver.save_screenshot(".\screenshot\\"+"page_title_1.png")
            self.logger.error("***************** Test titre de la page KO ****************")
            assert False
        
        "Cliquer sur la modale"
        self.hp=HomePage(self.driver)
        self.hp.clickaccepterTCF() 
        time.sleep(2)

        "Clique sur la liste des chaines puis selectionne une chaine à la suite"
        self.driver.find_element(By.CLASS_NAME, "sc-1ajxxj-0.sc-1c6u83a-3.iUrMAG").click()
        chaine = self.driver.find_elements(By.CLASS_NAME, "b8xld8-1")
        nb_chaine = len(chaine)
        print("Le nb de chaine est :",nb_chaine)
        
        # import pdb; pdb.set_trace()
        for nb in range(nb_chaine):
            actions = ActionChains(self.driver)
            actions.move_to_element(chaine[nb])
            actions.perform()
            time.sleep(3)
            chaine[nb].click()
            time.sleep(2)
            print(self.driver.title)
            time.sleep(2)
            self.driver.back()
            if nb == nb_chaine-1 : 
                print(nb)
                break
            self.driver.find_element(By.CLASS_NAME, "sc-1ajxxj-0.sc-1c6u83a-3.iUrMAG").click()
            chaine = self.driver.find_elements(By.CLASS_NAME, "b8xld8-1")
        time.sleep(5)

        self.logger.info("***************** FIN - Test_003_homePage_content ****************")
        self.driver.close()
        

    