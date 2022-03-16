"Ce fichier a pour objectif de localiser les objets de la home page + la modale TCF"
"& une classe qui permetra d'éffectuer la connexion"
"!!! AVEC UNE CONNEXION EN BOUCLE LOCALISATION AVEC XML FONCTIONNE !!! "
# auteur 
# dernier date de modif


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
        element = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, Locators.accepter_btnTCF_CSS)))
        # self.driver.find_element(By.CSS_SELECTOR,self.accepter_btnTCF_CSS).click()
        element.click()

    def clickaccepterConsent(self):
        self.driver.find_element(By.CLASS_NAME,Locators.consent_accepter_Class).click()

    def clickMonCompteBtn(self):
        # self.driver.find_element(By.XPATH,self.moncompte_btn_xml).click()
        element = self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators.moncompte_btn_xml)))
        element.click()

    def clickHomeBtn(self):
        self.driver.find_element(By.CSS_SELECTOR,Locators.HomeBtn_CSS).click()

    def clickBtnListeChaines(self):
        self.driver.find_element(By.CLASS_NAME, Locators.btnListe_chaines_Class).click()
    
    def listeChaines(self):
        return self.driver.find_elements(By.CLASS_NAME, Locators.liste_chaines_class)
    
    def checkObjetHomePage(self):
        self.driver.find_element(By.CSS_SELECTOR,Locators.objetHomePage_CSS).is_displayed()

    def clickdeco(self):
        # self.driver.find_element(By.CSS_SELECTOR, Locators.btn_deconnexion_CSS).click()
        element = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, Locators.btn_deconnexion_CSS)))
        # element = self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators.btn_deconnexion_Xpath)))
        element.click()
    
    def clickMesInfos(self):
        element = self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators.mesinfo_btn_xml)))
        element.click()
        # self.driver.find_element(By.XPATH, Locators.mesinfo_btn_xml).click()

    def getdonneesEmail(self):
        monEmail = self.driver.find_element(By.ID, Locators.donneesperso_email)
        # import pdb; pdb.set_trace()
        return monEmail.get_property("value")

    def clickDernierReplay(self):
        "cette action m'a donné un file à retordre, review et a ANALYSER"
        liste = self.driver.find_elements(By.CLASS_NAME, Locators.liste_dernierReplay_Class)
        liste[0].click()
        
        
    def clickSurRecherche(self):
        self.driver.find_element(By.CSS_SELECTOR, Locators.recherche_btn_CSS).click()
     
    def clickAjoutFavoris(self):
        # import pdb; pdb.set_trace()
        btn_ajouter = self.driver.find_elements(By.CLASS_NAME, Locators.AjoutFavoris_btn_Class_2)
        btn_ajouter[1].click()
        # self.driver.find_element(By.CSS_SELECTOR, self.AjoutFavoris_btn_CSS).click()
        # self.driver.find_element(By.XPATH,Locators.AjoutFavoris_btn_Xpath).click()
        
    