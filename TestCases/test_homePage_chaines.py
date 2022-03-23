"""
Objectif : tester la redirection vers de la page homePage de différentes chaines - hors connexion
Date de la dernière grosse maj : 23/03/2022
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
            #la vérification du titre de la page home page de la chaine se fait ICI
            assert act_title == self.tabTitles[nb], self.logger.error("***************** Test titre de la page - KO ****************")
            self.logger.info(f"***************** Test titre de la page {nb} - OK ****************") #le nom de la chaine sera variabiliser dans un tuple

            time.sleep(2)
            self.driver.back()
            if nb == nb_chaine-1 :
                break
            self.hp.clickBtnListeChaines()
            chaines = self.hp.listeChaines()
        time.sleep(5)
        self.logger.info("***************** FIN - Test_003_homePage_content ****************")
        # self.driver.close()