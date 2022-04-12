"""
Objectif : Step 1 : Faire un test de connexion des différents compte en boucle - Recupération des ID depuis un fichier excel
           Step 2 : Créer un nouveau compte et l'ajouter dans le fichier excel 
Dernière mise à jour importante : 23/03/2022
Owner : Abdi
"""
from PageObjects.ObPage import Page_OB_Connexion
from PageObjects.HomePage import HomePage
from PageObjects.MonCompte import MonCompte
from Utilities.customLogger import LogGen
from Utilities import XLUtils
from TestCases import conftest
# from faker import Faker
# import datetime
# import string
# import random 
import time

class Test_001_Connexion:
    logger = LogGen.loggen()
    path = "./testData/LoginData.xlsx"

    def test_Connexion_PlusieursID_EnBoucle(self,setup_SansConnexionUser):
        self.logger.info("***************** DEBUT - Test_001_Connexion ****************")
        self.logger.info("***************** DEBUT - test_Connexion_PlusieursID_EnBoucle ***************")
        self.driver = setup_SansConnexionUser
        self.hp=HomePage(self.driver)
        self.mn=MonCompte(self.driver)
        infosToaster = self.mn.getInfosToaster()
        #Vérifier quelques données liées au Toaster - affichage + statut + message affiché
        #Faudra vérifier ailleurs pour s'assurer l'état d'affichage
        #Pense à sauvegarder certaines données dans un fichier .INI
        assert infosToaster[0] == True
        assert "SUCCESS" in infosToaster[1] 
        assert "Vos choix ont bien été enregistrés" in infosToaster[2]

        self.nbLigne = XLUtils.getRowCount(self.path, "List_ID")
        print(f"Le fichier excel contient {self.nbLigne} ID de connexion")
        print("Nous allons boucler uniquement les 4 premiers lignes/comptes")

        lst_status = [] #Un tab qui stock les statut de pass ou de fail de différents connexions des ID 

        for nb in range(2, 6):
            self.username = XLUtils.readData(self.path,"List_ID",nb,4)
            self.password = XLUtils.readData(self.path,"List_ID",nb,5)
            self.exp = XLUtils.readData(self.path,"List_ID",nb,6)
            
            time.sleep(2)
            self.hp.clickMonCompteBtn() 
            time.sleep(2)

            "Saisi des ID dans OB"
            self.lp=Page_OB_Connexion(self.driver) 
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
            "Essay avec if () && () puis plusieurs elif ... "
            if act_title == exp_title:
                if self.exp == "pass":
                    self.logger.info("***************** Pass OK ****************")
                    self.mn.clickdeco()
                    XLUtils.writeData(self.path,"List_ID",nb,7,"PASS")
                    time.sleep(2)
                    lst_status.append("pass")
                    # assert True
                elif self.exp == "fail":                   
                    self.logger.error("***************** Fail KO ****************")
                    lst_status.append("fail")
                    self.driver.save_screenshot("./screenshot/page_title_0.png")
                    XLUtils.writeData(self.path,"List_ID",nb,7,"FAIL")
                    self.driver.refresh()
            elif act_title != exp_title:
                if self.exp == "pass":
                    self.logger.error("***************** Fail KO ****************")
                    XLUtils.writeData(self.path,"List_ID",nb,7,"FAIL")
                    lst_status.append("fail")
                    self.driver.save_screenshot("./screenshot/page_title_0.png")
                    self.driver.refresh()
                elif self.exp == "fail":                   
                    self.logger.info("***************** Pass OK - FAUX COMPTE ****************")
                    lst_status.append("pass")
                    XLUtils.writeData(self.path,"List_ID",nb,7,"PASS")
                    self.driver.refresh()

        print("L'état d'exécution des ID : ",lst_status)
        #vérification de l'état de l'exacution des différents ID
        #Peut-on vérifier autrement?
        assert "fail" not in lst_status, "ERREUR"
        time.sleep(2)
        self.logger.info("***************** FIN - test_Connexion_PlusieursID_EnBoucle ***************")

######Refelexion PK je dois utiliser des self dans cette methode?###########
    def test_Souscription_NEW_USER(self, setup_SansConnexionUser):
        self.logger.info("***************** DEBUT - Test_SOUSCRIPTION_NEW_USER ***************")

        "Génération ID(mail + mdp) random"
        self.rand_ID = conftest.genere_IdRandom() 
        self.rand_mail = self.rand_ID[0]
        self.rand_pwd = self.rand_ID[1]
        "Génération date de naissance random"
        date = conftest.genere_date()
        
        self.driver = setup_SansConnexionUser
        self.hp=HomePage(self.driver)
        self.lp=Page_OB_Connexion(self.driver)
        self.mn=MonCompte(self.driver)

        time.sleep(1)
        self.hp.clickMonCompteBtn() 
        time.sleep(1)
        self.lp.clickInscription()
        time.sleep(2)
        self.lp.setemail(self.rand_mail)
        time.sleep(1)
        self.lp.setPassword(self.rand_pwd)
        time.sleep(1)
        self.lp.clickCheckBox_newletter()
        time.sleep(1)
        self.lp.clickInscrire()
        time.sleep(1)
        self.lp.choixGenre(1)
        time.sleep(1)
        self.lp.setAge(date)
        time.sleep(1)
        self.lp.ClickTerminer()
       
        "Une fois que la souscription est terminée, j'ajoute les ID dans le fichier excel"
        nbLigne = XLUtils.getRowCount("./testData/LoginData.xlsx", "List_ID")
        XLUtils.writeData(self.path,"List_ID",nbLigne+1,3,date)
        XLUtils.writeData(self.path,"List_ID",nbLigne+1,4,self.rand_mail)
        XLUtils.writeData(self.path,"List_ID",nbLigne+1,5,self.rand_pwd)
        XLUtils.writeData(self.path,"List_ID",nbLigne+1,6,"pass")

        time.sleep(2)
        textePaperMesoptions = self.mn.getContenuPaperMesOptions()
        assert "Vous n'avez souscrit à aucune option payante." in textePaperMesoptions
        self.logger.info("***************** Vérification - OK (User n'a pas un abonnement) ***************")

        self.mn.clickMesInfos()
        time.sleep(2)
        monEmail = self.mn.getdonneesEmail()
        date_naissance = self.mn.getdonneesDate()
        genre = self.mn.getdonneesGenre()
        assert monEmail == self.rand_mail
        # emailAvatar = self.mn.getEmailSousAvatar()
        assert self.mn.getEmailSousAvatar() == self.rand_mail
        self.logger.info("***************** Vérification - OK (Email correspond bien à celui utilisé lors de l'inscription) ***************")
        ### le genre, ça serait mieux soit le mettre dans le fichier .ini avec un tuple en retour (num @ le lettre coorespondant)
        ### Ou le générer en random et puis pareil faire correspond avec la lettre correspondante
        ### Ca serait mieux d'effectuer les asserts dirrectement sans passer par une variable intermédiaire
        assert date_naissance == date 
        assert genre == "m", "le genre n'est pas TOP"
        self.logger.info("***************** Vérification - OK (date de naissance et genre sont OK) ***************")
        time.sleep(2)
        
        self.mn.clickNewslettersBtn()
        time.sleep(1)
        etatToggleNewsletter = self.mn.get_toggleState()
        assert etatToggleNewsletter =="false"
        time.sleep(1)
        
        self.mn.clickFiltreParentalBtn()
        time.sleep(1)
        etatToggleFiltreParental = self.mn.get_toggleState()
        assert etatToggleFiltreParental =="false"
        self.logger.info("***************** Vérification - OK (Les toggles sont à Off, donc Ok) ***************")
        time.sleep(1)
        # assert monEmail == self.rand_mail+"1", "L'email sur mon compte ne correspond pas à celui utilisé pour la souscription"
        # print ("Ceci est l'email affiché : "+monEmail)
        # print ("Ceci est l'email random faux : "+self.rand_mail+"1")
        # import pdb; pdb.set_trace()        
        self.logger.info("***************** FIN - Test_SOUSCRIPTION_NEW_USER ***************")
        self.logger.info("***************** FIN - Test_001_Connexion ****************")