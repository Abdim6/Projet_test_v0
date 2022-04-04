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
        self.obj = common_Actions(driver)
    
    def clickgenerInfo(self):
        self.obj.click(Locators.btn_gererInfos_CSS)

    def clickModifier(self):
        self.obj.click(Locators.btn_modifier_CSS)

    def setPrenom(self, prenom):
        self.obj.enter_text(Locators.textbox_firstname_id,prenom)

    def setNom(self, nom):
        self.obj.enter_text(Locators.textbox_lastname_id,nom)

    def clickValider(self):
        self.obj.click(Locators.btn_valider_CSS)
  