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
        self.obj = common_Actions(driver)
        
    def clickaccepterTCF(self):
        self.obj.click(Locators.accepter_btnTCF_CSS)

    def clickaccepterConsent(self):
        self.obj.click(Locators.consent_accepter_Class)

    def clickMonCompteBtn(self):
        self.obj.click(Locators.moncompte_btn_xml)

    def clickHomeBtn(self):
        self.obj.click(Locators.HomeBtn_CSS)

    def clickBtnListeChaines(self):
        self.obj.click(Locators.btnListe_chaines_Class)
    
    def listeChaines(self):
        "returne la liste de tous les elements de la liste chaine - "
        "cette action m'a donné un file à retordre, review et a ANALYSER"
        return self.obj.get_list_elements(Locators.liste_chaines_class)
       
    def checkObjetHomePage(self):
        self.obj.is_visible(Locators.objetHomePage_CSS)

    def clickdeco(self):
        self.obj.click(Locators.btn_deconnexion_CSS)
    
    def clickMesInfos(self):
        self.obj.click(Locators.mesinfo_btn_xml)

    def getdonneesEmail(self):
        # self.obj.get_value(Locators.donneesperso_email)
        self.obj.get_property(Locators.donneesperso_email, "value")

    def clickDernierReplay(self):
        "cette action m'a donné un file à retordre, review et a ANALYSER"
        self.obj.click(Locators.liste_dernierReplay_Class)
        
        
    def clickSurRecherche(self):
        self.obj.click(Locators.recherche_btn_CSS)
     
    def clickAjoutFavoris(self):
        self.obj.click(Locators.AjoutFavoris_btn_Class_3)
        "Faut que trouve une solution pour cliquer un element dans une liste d'elements ..."