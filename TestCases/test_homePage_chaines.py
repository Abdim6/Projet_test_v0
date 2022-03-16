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
from TestCases.conftest import setup_SansConnexionUser
from Utilities.readProperties import ReadTitlePage
from Utilities.customLogger import LogGen
from selenium.webdriver.common.action_chains import ActionChains


class Test_003_Login:
    
    logger = LogGen.loggen()

    def test_homePageTitle(self,setup_SansConnexionUser):
        self.logger.info("***************** DEBUT - Test_003_Login ****************")
        self.driver = setup_SansConnexionUser
        time.sleep(2)

        "Clique sur la liste des chaines puis selectionne une chaine à la suite"
        # self.driver.find_element(By.CLASS_NAME, "sc-1ajxxj-0.sc-1c6u83a-3.iUrMAG").click()
        # chaine = self.driver.find_elements(By.CLASS_NAME, "b8xld8-1")
        # nb_chaine = len(chaine)

        self.hp = HomePage(self.driver)
        self.hp.clickBtnListeChaines()
        time.sleep(2)
        chaines = self.hp.listeChaines()
        nb_chaine = len(chaines)

        print("Le nb de chaine est :",nb_chaine)
        self.tabTitles = [ReadTitlePage.getTitleM6(), ReadTitlePage.getTitleW9(), 
                          ReadTitlePage.getTitle6ter(),ReadTitlePage.getTitleguilli(), 
                          ReadTitlePage.getTitleparis_premiere(),ReadTitlePage.getTitleteva(),
                          ReadTitlePage.getTitleLelive()]

        # import pdb; pdb.set_trace()
        for nb in range(nb_chaine):
            actions = ActionChains(self.driver)
            actions.move_to_element(chaines[nb])
            actions.perform()
            time.sleep(3)
            chaines[nb].click()
            time.sleep(2)
            ####
            act_title = self.driver.title
            time.sleep(2)
            assert act_title == self.tabTitles[nb], self.logger.error("***************** Test titre de la page - KO ****************")
            self.logger.info(f"***************** Test titre de la page {nb} - OK ****************")

            time.sleep(2)
            self.driver.back()
            if nb == nb_chaine-1 :
                break
            # self.driver.find_element(By.CLASS_NAME, "sc-1ajxxj-0.sc-1c6u83a-3.iUrMAG").click()
            self.hp.clickBtnListeChaines()
            # chaines = self.driver.find_elements(By.CLASS_NAME, "b8xld8-1")
            chaines = self.hp.listeChaines()
        time.sleep(5)
        self.logger.info("***************** FIN - Test_003_homePage_content ****************")
        # self.driver.close()