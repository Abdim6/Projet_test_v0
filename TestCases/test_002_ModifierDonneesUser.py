"""
Objectif : Vérifier la modification des données mon compte + Ajout dans le favoris d'un programme 
Dernière mise à jour importante : 23/03/2022
Owner : Abdi
"""
from PageObjects.HomePage import HomePage
from PageObjects.MonCompte import MonCompte
from Utilities.customLogger import LogGen
import time


class Test_002_ModifierDonneesUser:
    logger = LogGen.loggen()

    def test_homePageTitle(self,setup_AvecConnexionUser):
        self.logger.info("***************** DEBUT - Test_002_ModifierDonneesUser ****************")
        self.driver = setup_AvecConnexionUser

        "Modifier les données de User"
        self.hp=HomePage(self.driver)
        time.sleep(2)
        self.mn = MonCompte(self.driver)
        self.mn.clickgenerInfo()
        time.sleep(1)
        self.mn.clickModifier()
        time.sleep(1)
        var = self.mn.get_prenom()
        var=int(var[5:])
        prenom = "abdi_"+str(var+1)

        # if var == "abdi_1":
        #     self.mn.setPrenom("abdi")
        # else : 
        #     self.mn.setPrenom("abdi_1")
        self.mn.setPrenom(prenom)
        time.sleep(1)
        self.mn.setNom("Bileh")
        time.sleep(2)
        self.mn.clickValider()
        time.sleep(2)
        "Retour sur la home page + ajout de programme dans le favoris"
        self.hp.clickHomeBtn()
        time.sleep(2)
        self.hp.clickSurRecherche()
        time.sleep(3)
        self.hp.clickDernierReplay()
        time.sleep(5)
        self.hp.clickAjoutFavoris()
        time.sleep(2)
        self.hp.clickMonCompteBtn()
        time.sleep(5)    #ce time out est tres important, reflechi comment l'optimiser
        self.hp.clickdeco()
        time.sleep(3)
        self.logger.info("***************** FIN - Test_002_ModifierDonneesUser ****************")