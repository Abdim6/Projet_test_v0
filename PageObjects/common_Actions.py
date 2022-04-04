"""
Objectif : Rassembler tous les bout de code/step utilisés plusieurs fois
Dernière mise à jour importante : 10/03/2022
Owner : Abdi
"""
###########  "Attention faut utiliser des fonction à la place de la classe" ############
##########   "Traduire tous les Commentaires" ############
from random import random
from xml.dom.minidom import Element
import pytest

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class common_Actions():

    # this function is called every time a new object of the base class is created.
    def __init__(self, driver):
        self.driver=driver
        self.wait = WebDriverWait(self.driver, 10)

    # this function performs click on web element whose locator is passed to it.
    def click(self, by_locator):
        self.wait.until(EC.visibility_of_element_located(by_locator)).click()
        
        ####A retravailler####
     # this function performs click on web element whose locator is passed to it. 
    def click_one_ofElements(self, by_locator,index):
        Element = self.wait.until(EC.visibility_of_all_elements_located(by_locator))
        Element[index].click()
        # return self.driver.find_elements(by_locator)
    
    # this function asserts comparison of a web element's text with passed in text.
    def assert_element_text(self, by_locator, element_text):
        web_element=self.wait.until(EC.visibility_of_element_located(by_locator))
        assert web_element.text == element_text

    # this function performs text entry of the passed in text, in a web element whose locator is passed to it.
    def enter_text(self, by_locator, text):
        return self.wait.until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    # this function checks if the web element whose locator has been passed to it, is enabled or not and returns
    # web element if it is enabled.
    def is_enabled(self, by_locator):
        return self.wait.until(EC.visibility_of_element_located(by_locator))

    # this function checks if the web element whose locator has been passed to it, is visible or not and returns
    # true or false depending upon its visibility.
    def is_visible(self,by_locator):
        element= self.wait.until(EC.visibility_of_element_located(by_locator))
        return bool(element)
    
    # this function moves the mouse pointer over a web element whose locator has been passed to it.
    def hover_to_oneElement(self, by_locator):
        element = self.wait.until(EC.visibility_of_element_located(by_locator))
        ActionChains(self.driver).move_to_element(element).perform()

    # this function moves the mouse pointer over a web element in list whose locator has been passed to it.
    def hover_to_list(self, by_locator,index):
        element = self.wait.until(EC.visibility_of_all_elements_located(by_locator))
        ActionChains(self.driver).move_to_element(element[index]).perform()

    def select_InList(self,by_locator,index):
        element = self.wait.until(EC.visibility_of_element_located(by_locator))
        drp = Select(element)
        drp.select_by_index(index)

    #this function return a property of an element value
    def get_property(self,by_locator, type_property):
        element = self.wait.until(EC.visibility_of_element_located(by_locator))
        return element.get_property(type_property)

    "cette fonction retourne la liste de tous elements"
    def get_list_elements(self,by_locator):
        return self.wait.until(EC.visibility_of_all_elements_located(by_locator))