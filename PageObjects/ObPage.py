"""
Objectif : Instentier les actions liées à la page Onboarding 
Date de la dernière grosse maj : 23/03/2022
Owner : Abdi
"""

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from PageObjects.Locator import Locators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from PageObjects.common_Actions import common_Actions

class Page_OB_Connexion:
    def __init__(self, driver):
        self.Action = common_Actions(driver)
    
    def setUsername(self, username):
        self.Action.enter_text(Locators.textbox_username_id, username)
        
    def setPassword(self, password):
        self.Action.enter_text(Locators.textbox_password_id, password)
        
    def clickLogin(self):
        self.Action.click(Locators.button_login_xml)

    def clickInscription(self):
        self.Action.click(Locators.button_inscription_new)

    def setemail(self,email):
        self.Action.enter_text(Locators.email_inscription, email)
        
    def setpwd(self,pwd):
        self.Action.enter_text(Locators.pwd_inscription, pwd)

    def clickCheckBox_newletter(self):
        self.Action.click(Locators.checkBox_newsletter)

    def clickInscrire(self):
        self.Action.click(Locators.button_inscrire_new)
 
    def choixGenre(self, choix):
        self.Action.select_InList(Locators.liste_genre,choix)
       
    def setAge(self, age):
        self.Action.enter_text(Locators.section_age, age)
  
    def ClickTerminer(self):
        self.Action.click(Locators.button_terminer)

   