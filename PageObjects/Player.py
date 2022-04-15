"""
Objectif : Instentier les actions liées au player 
Date de la dernière grosse maj : 15/04/2022
Owner : Abdi
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from PageObjects.Locator import Locators
import time
from PageObjects.common_Actions import common_Actions

class Player :
    def __init__(self, driver):
        self.Action = common_Actions(driver)
    
    def clickBtnPlayer(self):
        self.Action.click(Locators.playVideoBtn)

    def getTitreClip(self):
        return self.Action.get_attribute(Locators.playVideoBtn,"aria-label")
    
    def verifierPresencePubPreroll(self):
        return self.Action.is_visible(Locators.labelPubPlayer)
    
    "Ici il attend au moins 1000sec - c'est large"
    def attendreLaPreroll(self):
        self.Action.waitInvisibility(Locators.labelPubPlayer)
    
    def verifierDebutClip(self):
        return self.Action.is_visible(Locators.labelTitrePlayer)
    
    def getTitreProg(self):
        return self.Action.get_text(Locators.labelTitrePlayer)

    def Avancer15Secondes(self):
        self.Action.hover_to_list(Locators.listeBtnPlayer,3)
        self.Action.click_one_ofElements(Locators.listeBtnPlayer, 3)

    def getTempsEcouler(self):
        self.Action.hover_to_oneElement(Locators.tempsEcouler)
        return self.Action.get_text(Locators.tempsEcouler)

    def clickPlayStopPlayer(self):
        self.Action.hover_to_list(Locators.listeBtnPlayer,2)
        self.Action.click_one_ofElements(Locators.listeBtnPlayer, 2)

    def clickRetourAlaNavigation(self):
        self.Action.click(Locators.retourNavigateur)