"Ici est un cdt de connexion - lié aux objets de la page loginPage."
"Trouve une solution pour un time out auto de 1sec automatique"

import pytest
from selenium import webdriver
from PageObjects.ObPage import LoginmaPage
from PageObjects.HomePage import HomePage
from PageObjects.Divers.MonCompte import MonCompte
import time
from TestCases.conftest import setup_AvecConnexionUser
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen

class Test_002_ModifierDonneesUser:
    logger = LogGen.loggen()

    @pytest.mark.mesTests
    def test_homePageTitle(self,setup_AvecConnexionUser):
        self.logger.info("***************** DEBUT - test_002_ModifierDonneesUser ****************")
        self.driver = setup_AvecConnexionUser

        "Modifier les données de User"
        self.hp=HomePage(self.driver)
        time.sleep(2)
        self.hp.clickMonCompteBtn() 
        time.sleep(2)
        self.mn = MonCompte(self.driver)
        self.mn.clickgenerInfo()
        time.sleep(1)
        self.mn.clickModifier()
        time.sleep(1)
        self.mn.setPrenom("abdi")
        time.sleep(1)
        self.mn.setNom("Bileh")
        time.sleep(2)
        self.mn.clickValider()
        time.sleep(2)
        "Retour sur la home page + ajout de programme dans le favoris"
        self.hp.clickHomeBtn()
        time.sleep(2)
        self.hp.clickSurRecherche()
        time.sleep(1)
        self.hp.clickDernierReplay()
        time.sleep(3)
        self.hp.clickAjoutFavoris()
        time.sleep(2)
        self.hp.clickMonCompteBtn()
        time.sleep(5)
        self.hp.clickdeco()
        time.sleep(3)

        self.logger.info("***************** FIN - test_002_ModifierDonneesUser ****************")