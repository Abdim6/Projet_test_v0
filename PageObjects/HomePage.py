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
        # self.driver = driver 
        # self.wait = WebDriverWait(driver,30)
        self.obj = common_Actions(driver)
        
    "Pour cette fonction j'utilise un explicite wait"
    def clickaccepterTCF(self):
        # element = self.wait.until(EC.element_to_be_clickable((Locators.accepter_btnTCF_CSS)))
        # element.click()
        self.obj.click(Locators.accepter_btnTCF_CSS)

    def clickaccepterConsent(self):
        # self.driver.find_element(Locators.consent_accepter_Class).click()
        self.obj.click(Locators.consent_accepter_Class)

    def clickMonCompteBtn(self):
        # element = self.wait.until(EC.element_to_be_clickable((Locators.moncompte_btn_xml)))
        # element.click()
        self.obj.click(Locators.moncompte_btn_xml)

    def clickHomeBtn(self):
        # self.driver.find_element(Locators.HomeBtn_CSS).click()
        self.obj.click(Locators.HomeBtn_CSS)

    def clickBtnListeChaines(self):
        # self.driver.find_element(Locators.btnListe_chaines_Class).click()
        # element = self.wait.until(EC.element_to_be_clickable((Locators.btnListe_chaines_Class)))
        # element.click()
        self.obj.click(Locators.btnListe_chaines_Class)
    
    def listeChaines(self):
        # return self.driver.find_elements(Locators.liste_chaines_class)
        "returne la liste de tous les elements de la liste chaine - "
        "cette action m'a donné un file à retordre, review et a ANALYSER"
        return self.obj.get_list_elements(Locators.liste_chaines_class)
       
    def checkObjetHomePage(self):
        # self.driver.find_element(Locators.objetHomePage_CSS).is_displayed()
        self.obj.is_visible(Locators.objetHomePage_CSS)

    def clickdeco(self):
        # element = self.wait.until(EC.element_to_be_clickable((Locators.btn_deconnexion_CSS)))
        # element.click()
        self.obj.click(Locators.btn_deconnexion_CSS)
    
    def clickMesInfos(self):
        # element = self.wait.until(EC.element_to_be_clickable((Locators.mesinfo_btn_xml)))
        # element.click()
        self.obj.click(Locators.mesinfo_btn_xml)

    def getdonneesEmail(self):
        # monEmail = self.driver.find_element(Locators.donneesperso_email)
        # return monEmail.get_property("value")
        self.obj.get_value(Locators.donneesperso_email)

    def clickDernierReplay(self):
        "cette action m'a donné un file à retordre, review et a ANALYSER"
        # liste = self.driver.find_elements(Locators.liste_dernierReplay_Class)
        # liste[0].click()
        self.obj.click(Locators.liste_dernierReplay_Class)
        
        
    def clickSurRecherche(self):
        # self.driver.find_element(Locators.recherche_btn_CSS).click()
        self.obj.click(Locators.recherche_btn_CSS)
     
    def clickAjoutFavoris(self):
        # btn_ajouter = self.driver.find_elements(Locators.AjoutFavoris_btn_Class_2)
        # btn_ajouter[1].click()
        self.obj.click(Locators.AjoutFavoris_btn_Class_3)
        "Faut que trouve une solution pour cliquer un element dans une liste d'elements ..."