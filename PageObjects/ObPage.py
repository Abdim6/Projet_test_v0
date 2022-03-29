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
        # self.driver = driver
        # self.wait = WebDriverWait(driver,30)
        self.obj = common_Actions(driver)
    
    def setUsername(self, username):
        # self.driver.find_element(Locators.textbox_username_id).clear
        # self.driver.find_element(Locators.textbox_username_id).send_keys(username)
        self.obj.enter_text(Locators.textbox_username_id, username)
        
    def setPassword(self, password):
        # self.driver.find_element(Locators.textbox_password_id).clear
        # self.driver.find_element(Locators.textbox_password_id).send_keys(password)
        self.obj.enter_text(Locators.textbox_password_id, password)
        
    def clickLogin(self):
        # self.driver.find_element(Locators.button_login_xml).click()
        self.obj.click(Locators.button_login_xml)

    def clickInscription(self):
        # self.driver.find_element(Locators.button_inscription_new).click()
        # element = self.wait.until(EC.element_to_be_clickable((Locators.button_inscription_new)))
        # element.click()
        self.obj.click(Locators.button_inscription_new)

    def setemail(self,email):
        # self.driver.find_element(Locators.email_inscription).clear
        # self.driver.find_element(Locators.email_inscription).send_keys(email)
        self.obj.enter_text(Locators.email_inscription, email)
        
    def setpwd(self,pwd):
        # self.driver.find_element(Locators.pwd_inscription).clear
        # self.driver.find_element(Locators.pwd_inscription).send_keys(pwd)
        self.obj.enter_text(Locators.pwd_inscription, pwd)

    def clickInscrire(self):
        # self.driver.find_element(Locators.button_inscrire_new).click()
        self.obj.click(Locators.button_inscrire_new)
 
    def choixGenre(self):
        # elem = self.driver.find_element(Locators.liste_genre)
        # drp = Select(elem)
        # drp.select_by_index(1)
        self.obj.select_InList(Locators.liste_genre,1)
       
    def setAge(self, age):
        # self.driver.find_element(Locators.section_age).click() 
        # self.driver.find_element(Locators.section_age).send_keys(age)
        self.obj.enter_text(Locators.section_age, age)
  
    def ClickTerminer(self):
        # self.driver.find_element(Locators.button_terminer).click() 
        self.obj.click(Locators.button_terminer)

   