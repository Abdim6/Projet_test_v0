"""
Objectif : Instentier les actions liées à la page mon compte  
Date de la dernière grosse maj : 23/03/2022
Owner : Abdi
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from PageObjects.Locator import Locators
from PageObjects.common_Actions import common_Actions

class MonCompte:
    def __init__(self, driver):
        self.Action = common_Actions(driver)
    
    def clickgenerInfo(self):
        self.Action.click(Locators.btn_gererInfos_CSS)

    def clickModifier(self):
        self.Action.click(Locators.btn_modifier_CSS)

    def setPrenom(self, prenom):
        self.Action.clear_input(Locators.textbox_firstname_id)
        self.Action.enter_text(Locators.textbox_firstname_id,prenom)

    def setNom(self, nom):
        self.Action.clear_input(Locators.textbox_lastname_id)
        self.Action.enter_text(Locators.textbox_lastname_id,nom)

    def clickValider(self):
        self.Action.click(Locators.btn_valider_CSS)

    def get_prenom(self):
        # self.Action.get_value(Locators.donneesperso_email)
        return self.Action.get_property(Locators.textbox_firstname_id, "value")
    
    def clickNewslettersBtn(self):
        self.Action.hover_to_list(Locators.listeOnglet_monCompte_Class,2)
        self.Action.click_one_ofElements(Locators.listeOnglet_monCompte_Class, 2)
    
    def clickFiltreParentalBtn(self):
        self.Action.hover_to_list(Locators.listeOnglet_monCompte_Class,5)
        self.Action.click_one_ofElements(Locators.listeOnglet_monCompte_Class, 5)

    def clickListeFavorisBtn(self):
        self.Action.hover_to_list(Locators.listeOnglet_monCompte_Class,0)
        self.Action.click_one_ofElements(Locators.listeOnglet_monCompte_Class, 0)

    def getContenuPaperMesOptions(self):
        return self.Action.get_text(Locators.listPapersPageVuEnsemble, 2)

    def get_toggleState(self):
        return self.Action.get_attribute(Locators.unToggle, "aria-checked")

    def getEmailSousAvatar(self):
        return self.Action.get_text(Locators.emailSousAvatar, -1)

    def choixGenre(self, choix):
        self.Action.click(Locators.liste_genre)
        self.Action.select_InList(Locators.liste_genre,choix)
       
    def setAge(self, age):
        self.Action.clear_input(Locators.section_age)
        self.Action.enter_text(Locators.section_age, age)

    def get_genre(self):
        return self.Action.get_attribute(Locators.liste_genre, "value")

    def click_ProgFavoris_0(self):
        self.Action.click(Locators.listeProgFavoris)
    
    def get_titleProgFavoris_0(self):
        return self.Action.get_attribute(Locators.listeProgFavoris, "title")

    def verif_visibilityProgFavoris_0(self):
        return self.Action.is_visible(Locators.listeProgFavoris)
        
    # "A deplacer"
    def clickdeco(self):
        self.Action.click(Locators.btn_deconnexion_CSS)

    # "A deplacer"    
    def clickMesInfos(self):
        self.Action.click(Locators.mesinfo_btn_xml)

    # "A deplacer"
    def getdonneesEmail(self):
        # self.Action.get_value(Locators.donneesperso_email)
        return self.Action.get_property(Locators.email_Id, "value")
        
# "A deplacer"
    def getdonneesDate(self):
        # self.Action.get_value(Locators.donneesperso_email)
        return self.Action.get_property(Locators.date_naissance_Id, "value")

# "A deplacer"
    def getdonneesGenre(self):
        # self.Action.get_value(Locators.donneesperso_email)
        return self.Action.get_property(Locators.genre_Id, "value")

# "A deplacer" => recherche page
    def clickDernierReplay(self):
        "cette action m'a donné un file à retordre, review et a ANALYSER"
        self.Action.click(Locators.liste_dernierReplay_Class)

# "A deplacer" => generaliste page
    def getInfosToaster(self):
        affiche_etat = self.Action.is_visible(Locators.toaster)
        resultat_etat = self.Action.get_attribute(Locators.toaster, "type")
        message_toaster = self.Action.get_attribute(Locators.toaster, "innerText")
        return affiche_etat, resultat_etat, message_toaster

# "A deplacer" => recherche page
    def chercheProgramme(self, prog):
        self.Action.clear_input(Locators.recherche_input)
        self.Action.enter_text(Locators.recherche_input,prog)