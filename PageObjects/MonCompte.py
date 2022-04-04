"""
Objectif : Instentier les actions liées à la page mon compte  
Date de la dernière grosse maj : 23/03/2022
Owner : Abdi
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from PageObjects.Locator import Locators
from PageObjects.common_Actions import common_Actions

class MonCompte:
    def __init__(self, driver):
        self.Action = common_Actions(driver)
    
    def clickgenerInfo(self):
        self.Action.click(Locators.btn_gererInfos_CSS)

    def clickModifier(self):
        self.Action.click(Locators.btn_modifier_CSS)

    def setPrenom(self, prenom):
        self.Action.enter_text(Locators.textbox_firstname_id,prenom)

    def setNom(self, nom):
        self.Action.enter_text(Locators.textbox_lastname_id,nom)

    def clickValider(self):
        self.Action.click(Locators.btn_valider_CSS)
  