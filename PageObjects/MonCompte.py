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
        self.Action.clear_input(Locators.textbox_firstname_id)
        self.Action.enter_text(Locators.textbox_firstname_id,prenom)

    def setNom(self, nom):
        self.Action.clear_input(Locators.textbox_lastname_id)
        self.Action.enter_text(Locators.textbox_lastname_id,nom)

    def clickValider(self):
        self.Action.click(Locators.btn_valider_CSS)

    def get_prenom(self):
        # self.Action.get_value(Locators.donneesperso_email)
        return self.Action.get_property(Locators.textbox_firstname_id, "value")
    
    def clickNewslettersBtn(self):
        self.Action.hover_to_list(Locators.listeOnglet_monCompte_Class,2)
        self.Action.click_one_ofElements(Locators.listeOnglet_monCompte_Class, 2)
    
    def clickFiltreParentalBtn(self):
        self.Action.hover_to_list(Locators.listeOnglet_monCompte_Class,5)
        self.Action.click_one_ofElements(Locators.listeOnglet_monCompte_Class, 5)

    def clickListeFavorisBtn(self):
        self.Action.hover_to_list(Locators.listeOnglet_monCompte_Class,0)
        self.Action.click_one_ofElements(Locators.listeOnglet_monCompte_Class, 0)

    def getContenuPaperMesOptions(self):
        return self.Action.get_text(Locators.listPapersPageVuEnsemble, 2)

    def get_toggleState(self):
        return self.Action.get_attribute(Locators.unToggle, "aria-checked")

    def getEmailSousAvatar(self):
        return self.Action.get_text(Locators.emailSousAvatar, -1)