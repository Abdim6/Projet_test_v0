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

class HomePage:
    
    def __init__(self, driver):
        self.driver = driver 
        self.wait = WebDriverWait(driver,30)
        
    "Pour cette fonction j'utilise un explicite wait"
    def clickaccepterTCF(self):
        element = self.wait.until(EC.element_to_be_clickable((Locators.accepter_btnTCF_CSS)))
        element.click()

    def clickaccepterConsent(self):
        self.driver.find_element(Locators.consent_accepter_Class).click()

    def clickMonCompteBtn(self):
        element = self.wait.until(EC.element_to_be_clickable((Locators.moncompte_btn_xml)))
        element.click()

    def clickHomeBtn(self):
        self.driver.find_element(Locators.HomeBtn_CSS).click()

    def clickBtnListeChaines(self):
        # self.driver.find_element(Locators.btnListe_chaines_Class).click()
        element = self.wait.until(EC.element_to_be_clickable((Locators.btnListe_chaines_Class)))
        element.click()
    
    def listeChaines(self):
        return self.driver.find_elements(Locators.liste_chaines_class)
    
    def checkObjetHomePage(self):
        self.driver.find_element(Locators.objetHomePage_CSS).is_displayed()

    def clickdeco(self):
        element = self.wait.until(EC.element_to_be_clickable((Locators.btn_deconnexion_CSS)))
        element.click()
    
    def clickMesInfos(self):
        element = self.wait.until(EC.element_to_be_clickable((Locators.mesinfo_btn_xml)))
        element.click()

    def getdonneesEmail(self):
        monEmail = self.driver.find_element(Locators.donneesperso_email)
        return monEmail.get_property("value")

    def clickDernierReplay(self):
        "cette action m'a donné un file à retordre, review et a ANALYSER"
        liste = self.driver.find_elements(Locators.liste_dernierReplay_Class)
        liste[0].click()
        
        
    def clickSurRecherche(self):
        self.driver.find_element(Locators.recherche_btn_CSS).click()
     
    def clickAjoutFavoris(self):
        btn_ajouter = self.driver.find_elements(Locators.AjoutFavoris_btn_Class_2)
        btn_ajouter[1].click()
        
    