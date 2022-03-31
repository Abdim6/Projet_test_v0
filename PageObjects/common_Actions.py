"""
Objectif : Rassembler tous les bout de code/step utilisés plusieurs fois
Dernière mise à jour importante : 10/03/2022
Owner : Abdi
"""

from random import random
from xml.dom.minidom import Element
import pytest
# import string
# from PageObjects.HomePage import HomePage
# from Utilities.readProperties import ReadConfig
# from Utilities.customLogger import LogGen

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

    # this function performs click on web element whose locator is passed to it.
    def click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()
        
####A retravailler####
     # this function performs click on web element whose locator is passed to it. 
    def click_one_ofElements(self, by_locator):
        # elements = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        # elements[index].click()
        return self.driver.find_elements(by_locator)
        # elements[index].click()
    
    # this function asserts comparison of a web element's text with passed in text.
    def assert_element_text(self, by_locator, element_text):
        web_element=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        assert web_element.text == element_text

    # this function performs text entry of the passed in text, in a web element whose locator is passed to it.
    def enter_text(self, by_locator, text):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    # this function checks if the web element whose locator has been passed to it, is enabled or not and returns
    # web element if it is enabled.
    def is_enabled(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))

    # this function checks if the web element whose locator has been passed to it, is visible or not and returns
    # true or false depending upon its visibility.
    def is_visible(self,by_locator):
        element=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)
    
    # this function moves the mouse pointer over a web element whose locator has been passed to it.
    def hover_to(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        ActionChains(self.driver).move_to_element(element).perform()

    def select_InList(self,by_locator,index):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        drp = Select(element)
        drp.select_by_index(index)

    def get_value(self,by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.get_property("value")

    "cette fonction retourne la liste de tous elements"
    def get_list_elements(self,by_locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(by_locator))
        # self.driver.find_element(by_locator)
        # import pdb; pdb.set_trace()
        # self.driver.find_elements(By.CLASS_NAME,"b8xld8-1")