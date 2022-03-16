"""
Objectif :
Date dernière Maj : 
Owner : 
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from PageObjects.Locator import Locators

class LoginmaPage:
    def __init__(self, driver):
        self.driver = driver
    
    def setUsername(self, username):
        self.driver.find_element(By.ID,Locators.textbox_username_id).clear
        self.driver.find_element(By.ID,Locators.textbox_username_id).send_keys(username)
        
    def setPassword(self, password):
        self.driver.find_element(By.ID,Locators.textbox_password_id).clear
        self.driver.find_element(By.ID,Locators.textbox_password_id).send_keys(password)
        
    def clickLogin(self):
        self.driver.find_element(By.XPATH,Locators.button_login_xml).click()

    def clickInscription(self):
        self.driver.find_element(By.CSS_SELECTOR,Locators.button_inscription).click()

    def setemail(self,email):
        self.driver.find_element(By.ID,Locators.email_inscription).clear
        self.driver.find_element(By.ID,Locators.email_inscription).send_keys(email)

    def setpwd(self,pwd):
        self.driver.find_element(By.ID,Locators.pwd_inscription).clear
        self.driver.find_element(By.ID,Locators.pwd_inscription).send_keys(pwd)

    def clickInscrire(self):
        self.driver.find_element(By.CSS_SELECTOR,Locators.button_inscrire_new).click()
 
    def choixGenre(self):
        elem = self.driver.find_element(By.ID,Locators.liste_genre)
        drp = Select(elem)
        drp.select_by_index(1)
       
    def setAge(self, age):
        self.driver.find_element(By.ID,Locators.section_age).click() 
        self.driver.find_element(By.ID,Locators.section_age).send_keys(age)
  
    def ClickTerminer(self):
        self.driver.find_element(By.CSS_SELECTOR,Locators.button_terminer).click() 

   