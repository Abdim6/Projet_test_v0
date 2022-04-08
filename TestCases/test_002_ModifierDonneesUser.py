"""
Objectif : Vérifier la modification des données mon compte + Ajout dans le favoris d'un programme 
Dernière mise à jour importante : 23/03/2022
Owner : Abdi
"""
from PageObjects.HomePage import HomePage
from PageObjects.MonCompte import MonCompte
from Utilities.customLogger import LogGen
from TestCases import conftest
import time
# from faker import Faker
# import datetime


class Test_002_ModifierDonneesUser:
    logger = LogGen.loggen()

    def test_modifierDonnees(self,setup_AvecConnexionUser):
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
        prenom = self.mn.get_prenom()
        num=int(prenom[5:])
        prenom = "abdi_"+str(num+1)
        self.mn.setPrenom(prenom)
        time.sleep(1)
        self.mn.setNom("Bileh")
        time.sleep(2)

        # self.mn.setAge(self.random_date_fr)
        self.mn.setAge(conftest.genere_date())
        time.sleep(2)
        if self.mn.get_genre()=='f':self.mn.choixGenre(1)
        else : self.mn.choixGenre(2)
        time.sleep(2)
        """
        Modifier la date de naissance  - ok 
        Modifier le genre              - ok 
        Page des favoris => recup nb prog favoris (donc vérifie sur le nb-1 après avoir enlever un)
        Choisi un prog et clique dessus - ok 
        Sort le de la liste de favoris + vérifie le toaster - ok 
        Retour à la page des favoris + vérif si le prog est bien enlévé de la selection () (donc vérifie sur le nb-1 après avoir enlever un)
        => fais en sorte qu'il aie tjrs un pro favoris au moins dans la liste, ajout lors dans un autre scénario
        Si il n'a pas de favoris dans la liste sort directement et afficher un message ("ALERTE! ou ERREUR!)
        Sauvegarder le prog mis en favoris dans un fichier excel pour le tester dans un autre test, si toujours présent
        """
        self.mn.clickValider()
        time.sleep(2)
        self.mn.clickListeFavorisBtn()
        time.sleep(1)
        titleProgFavoris = self.mn.get_titleProgFavoris_0()
        # print(titleProgFavoris)
        self.mn.click_ProgFavoris_0()
        time.sleep(2)

        "Retour sur la home page + ajout de programme dans le favoris"
        # self.hp.clickHomeBtn()
        # time.sleep(2)
        # self.hp.clickSurRecherche()
        # time.sleep(3)
        # self.hp.clickDernierReplay()
        # time.sleep(5)
        self.hp.clickAjoutFavoris()
        time.sleep(2)
        self.hp.clickMonCompteBtn()
        time.sleep(2)
        self.mn.clickListeFavorisBtn()
        time.sleep(2)
        """ICI faut reflechir comment vérifier que le prog supprimer ne soit pas affiche dans cette liste
         => utilise plutot une liste et prevoit le cas ou il n'y'a pas de favoris
         peut etre comparer le titre du 1er prog, 
         premièrement fallait recupérer le nb de prog favoris pour comparre plus tard ... à voir si c'est faisable
         peut etre utilise l'action invisibility?
         """
        # isVisible = self.mn.verif_visibilityProgFavoris_0()
        # print(isVisible)

        # titleProgFavoris = self.mn.get_titleProgFavoris_0()
        # print("vérifie titre :", titleProgFavoris)

        self.hp.clickSurRecherche()
        time.sleep(1)
        self.hp.chercheProgramme(titleProgFavoris)
        "ICI la page se charge pas vite, d'où le wait long, à terme faudra parametrer en auto"
        time.sleep(3)
        self.hp.clickDernierReplay()
        time.sleep(3)
        self.hp.clickAjoutFavoris()
        time.sleep(2)
        self.hp.clickMonCompteBtn()
        time.sleep(2)
        self.mn.clickListeFavorisBtn()
        time.sleep(2)
        # titleProgFavoris = self.mn.get_titleProgFavoris_0()
        assert titleProgFavoris == self.mn.get_titleProgFavoris_0()
        # print("vérifie titre :", titleProgFavoris)

        # import pdb;pdb.set_trace()

        time.sleep(3)    #ce time out est tres important, reflechi comment l'optimiser
        self.hp.clickdeco()
        time.sleep(2)
        self.logger.info("***************** FIN - Test_002_ModifierDonneesUser ****************")