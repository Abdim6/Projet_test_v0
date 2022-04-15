"""
Objectif : Instentier les actions liées recherche
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

class Recherche :
    def __init__(self, driver):
        self.Action = common_Actions(driver)
        
    # "A deplacer" => recherche page
    def chercheProgramme(self, prog):
        self.Action.clear_input(Locators.recherche_input)
        self.Action.enter_text(Locators.recherche_input,prog)

    # "A deplacer" => recherche page
    def clickDernierReplay(self):
        "cette action m'a donné un file à retordre, review et a ANALYSER"
        self.Action.click(Locators.liste_dernierReplay_Class)