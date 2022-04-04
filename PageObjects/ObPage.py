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

class LoginmaPage:
    def __init__(self, driver):
        self.obj = common_Actions(driver)
    
    def setUsername(self, username):
        self.obj.enter_text(Locators.textbox_username_id, username)
        
    def setPassword(self, password):
        self.obj.enter_text(Locators.textbox_password_id, password)
        
    def clickLogin(self):
        self.obj.click(Locators.button_login_xml)

    def clickInscription(self):
        self.obj.click(Locators.button_inscription_new)

    def setemail(self,email):
        self.obj.enter_text(Locators.email_inscription, email)
        
    def setpwd(self,pwd):
        self.obj.enter_text(Locators.pwd_inscription, pwd)

    def clickInscrire(self):
        self.obj.click(Locators.button_inscrire_new)
 
    def choixGenre(self):
        self.obj.select_InList(Locators.liste_genre,1)
       
    def setAge(self, age):
        self.obj.enter_text(Locators.section_age, age)
  
    def ClickTerminer(self):
        self.obj.click(Locators.button_terminer)

   