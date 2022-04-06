"""
Objectif : Instentier les actions liées à la page home page 
Date de la dernière grosse maj : 23/03/2022
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

class HomePage:
    
    def __init__(self, driver):
        self.Action = common_Actions(driver)
        
    def clickaccepterTCF(self):
        self.Action.click(Locators.accepter_btnTCF_CSS)

    def clickaccepterConsent(self):
        self.Action.click(Locators.consent_accepter_Class)

    def clickMonCompteBtn(self):
        self.Action.click(Locators.moncompte_btn_xml)

    def clickHomeBtn(self):
        self.Action.click(Locators.HomeBtn_CSS)

    def clickBtnListeChaines(self):
        self.Action.click(Locators.btnListe_chaines_Class)
    
    def listeChaines(self):
        "returne la liste de tous les elements de la liste chaine - "
        "cette action m'a donné un file à retordre, review et a ANALYSER"
        return self.Action.get_list_elements(Locators.liste_chaines_class)

    def clickChaineBtn(self, index):
        self.Action.hover_to_list(Locators.liste_chaines_class,index)
        self.Action.click_one_ofElements(Locators.liste_chaines_class, index)

    def checkObjetHomePage(self):
        self.Action.is_visible(Locators.objetHomePage_CSS)

    def clickdeco(self):
        self.Action.click(Locators.btn_deconnexion_CSS)
    
    def clickMesInfos(self):
        self.Action.click(Locators.mesinfo_btn_xml)

    def getdonneesEmail(self):
        # self.Action.get_value(Locators.donneesperso_email)
        return self.Action.get_property(Locators.donneesperso_email, "value")

    def clickDernierReplay(self):
        "cette action m'a donné un file à retordre, review et a ANALYSER"
        self.Action.click(Locators.liste_dernierReplay_Class)
        
    def clickSurRecherche(self):
        self.Action.click(Locators.recherche_btn_CSS)
     
    def clickAjoutFavoris(self):
        self.Action.click(Locators.AjoutFavoris_btn_Class_3)
        self.Action.get_property(Locators.AjoutFavoris_btn_Class_3, "aria-pressed")
        "Faut que trouve une solution pour cliquer un element dans une liste d'elements ..."

       