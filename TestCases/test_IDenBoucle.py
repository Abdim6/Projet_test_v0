"Ici est un cdt de connexion - lié aux objets de la page loginPage."
"PROBLEME RENCONTRE AVEC UNE BOUCLE DE DONNEES - SOIT PROB DE CLIC SUR LE BOUTON SE CONNECTER SOIT SUR LE LANCER DU DRIVER"
"EXECUTION EN BOUCLE DES id SUR §PLAY DEPUIS UN FICHIER EXCEL OK - 64SEC D'EXÉCUTION"
"!!!!! Pense à factoriser encore, url et TCF peuvent être dans conftest"
"""
Objectif :
Date de la dernière grosse maj :

"""
import pytest
from selenium import webdriver
from PageObjects.ObPage import LoginmaPage
from PageObjects.HomePage import HomePage
import time
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from Utilities import XLUtils
import string
import random 
from selenium.webdriver.support.ui import WebDriverWait

class Test_001_Login:
    logger = LogGen.loggen()
    path = "./testData/LoginData.xlsx"

    logger.info("***************** DEBUT - Test_001_Login ****************")
    logger.info("***************** vérification du titre de la page d'accueil ****************")

    def test_homePageTitle(self,setup_SansConnexionUser):
        self.driver = setup_SansConnexionUser
        self.hp=HomePage(self.driver)

        self.nbLigne = XLUtils.getRowCount(self.path, "Feuil1")
        print(f"Le fichier excel contient {self.nbLigne} ID de connexion")

        lst_status = [] #Un tab qui stock les statut de pass ou de fail de différents connexions des ID 

        for nb in range(2, self.nbLigne+1):
            self.username = XLUtils.readData(self.path,"Feuil1",nb,3)
            self.password = XLUtils.readData(self.path,"Feuil1",nb,4)
            self.exp = XLUtils.readData(self.path,"Feuil1",nb,5)
            
            time.sleep(2)
            self.hp.clickMonCompteBtn() 
            time.sleep(2)

            "Saisi des ID dans OB"
            self.lp=LoginmaPage(self.driver) 
            self.lp.setUsername(self.username)
            time.sleep(1)
            self.lp.setPassword(self.password)
            time.sleep(2)
            self.lp.clickLogin()   
            time.sleep(2)

            "Recupération du titre de la page mon compte"
            act_title = self.driver.title
            "Le titre de la page mon compte attendu"
            exp_title = "6play : Mon espace personnel"

            time.sleep(2)
            if act_title == exp_title:
                if self.exp == "pass":
                    self.logger.info("***************** Pass OK ****************")
                    self.hp.clickdeco()
                    XLUtils.writeData(self.path,"Feuil1",nb,6,"PASS")
                    time.sleep(2)
                    lst_status.append("pass")
                    # assert True
                elif self.exp == "fail":                   
                    self.logger.error("***************** Fail KO ****************")
                    lst_status.append("fail")
                    self.driver.save_screenshot("./screenshot/page_title_0.png")
                    XLUtils.writeData(self.path,"Feuil1",nb,6,"FAIL")
                    self.driver.refresh()
            elif act_title != exp_title:
                if self.exp == "pass":
                    self.logger.error("***************** Fail KO ****************")
                    XLUtils.writeData(self.path,"Feuil1",nb,6,"FAIL")
                    lst_status.append("fail")
                    self.driver.save_screenshot("./screenshot/page_title_0.png")
                    self.driver.refresh()
                elif self.exp == "fail":                   
                    self.logger.info("***************** Pass OK - FAUX COMPTE ****************")
                    lst_status.append("pass")
                    XLUtils.writeData(self.path,"Feuil1",nb,6,"PASS")
                    self.driver.refresh()

        print("L'état d'exécution des ID : ",lst_status)
        #vérification de l'état de l'exacution des différents ID
        assert "fail" not in lst_status, "ERREUR"
        time.sleep(2)
        self.logger.info("***************** vérification du titre de la page d'accueil ****************")
       
        
    "______-----_____"   
    @pytest.mark.skip
    def test_souscription(self, setup_SansConnexionUser):
        self.logger.info("***************** DEBUT - Test_SOUSCRIPTION_NEW_USER ***************")
        "fait appel à une fonction qui genère un email et mdp randoom pour créer un compte 6play "
        "rentre ces ID dans le fichier "
        letters = string.ascii_lowercase
        letters_upper = string.ascii_uppercase
        rand_string = "".join(random.choice(letters) for i in range(15))
        self.rand_mail = rand_string + "@gmail.com"
        self.rand_password_lower = "".join(random.choice(letters) for i in range(5))
        self.rand_password_upper = "".join(random.choice(letters_upper) for i in range(5))
        self.rand_pwd = self.rand_password_lower+self.rand_password_upper + str(5)

        self.driver = setup_SansConnexionUser
        self.hp=HomePage(self.driver)
        self.lp=LoginmaPage(self.driver)

        time.sleep(1)
        self.hp.clickMonCompteBtn() 
        time.sleep(1)
        self.lp.clickInscription()
        time.sleep(2)
        self.lp.setemail(self.rand_mail)
        time.sleep(1)
        self.lp.setPassword(self.rand_pwd)
        time.sleep(1)
        self.lp.clickInscrire()
        time.sleep(1)
        self.lp.choixGenre()
        time.sleep(1)
        self.lp.setAge("29/11/1999")
        time.sleep(1)
        self.lp.ClickTerminer()
       
        "Une fois que la souscription est terminée, j'ajoute les ID dans le fichier"
        nbLigne = XLUtils.getRowCount("./testData/LoginData.xlsx", "Feuil1")
        XLUtils.writeData(self.path,"Feuil1",nbLigne+1,3,self.rand_mail)
        XLUtils.writeData(self.path,"Feuil1",nbLigne+1,4,self.rand_pwd)
        XLUtils.writeData(self.path,"Feuil1",nbLigne+1,5,"pass")

        time.sleep(2)
        self.hp.clickMesInfos()
        time.sleep(2)
        monEmail = self.hp.getdonneesEmail()
        if monEmail == self.rand_mail:
            print("L'email récupéré correspond à celui utilisé lors de la souscription de compte")
            assert True
        time.sleep(2)
        self.logger.info("***************** FIN - Test_SOUSCRIPTION_NEW_USER ***************")
        self.logger.info("***************** FIN - Test_001_Login ****************")