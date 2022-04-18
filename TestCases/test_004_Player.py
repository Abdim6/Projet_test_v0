"""
Objectif : Lancer un clip, utiliser les boutons dans le player et puis quitter le player 
Dernière mise à jour importante : 15/04/2022
Owner : Abdi
"""
from PageObjects.HomePage import HomePage
from PageObjects.Player import Player
from PageObjects.Recherche import Recherche
from Utilities.customLogger import LogGen
import time

class Test_004_Player:
    logger = LogGen.loggen()

    def test_lancerUnVOD(self,setup_11):
        self.logger.info("***************** DEBUT - Test_004_Player ****************")
        self.driver = setup_11
        
        "Instancier les classes des POM utilisées"
        self.homePage = HomePage(self.driver)
        self.player = Player(self.driver)
        self.recherche = Recherche(self.driver)

        self.homePage.clickSurRecherche()
        time.sleep(1)
        self.recherche.chercheProgramme("top chef")
        time.sleep(3)
        self.recherche.clickDernierReplay()
        time.sleep(1)
        titreClip = self.player.getTitreClip()
        self.player.clickBtnPlayer()
        time.sleep(2)
        if(self.player.verifierPresencePubPreroll()) : 
            print("Début du preroll ")
        start = time.time()
        self.player.attendreLaPreroll()
        time.sleep(2)
        self.player.verifierDebutClip()
        end = time.time()
        titreProgramme = self.player.getTitreProg()
        print("titreProgramme : ",titreProgramme)
        print("titreClip : ",titreClip)
        print(f"La Preroll a durée : {end - start} secondes.")
        assert titreProgramme in titreClip
        
        time.sleep(5)
        # TempsEcouler1 = self.player.getTempsEcouler()
        # self.player.Avancer15Secondes()
        # TempsEcouler2 = self.player.getTempsEcouler()
        # print(f"le temps ecouler est : {TempsEcouler1} et après avoir avancé un peu il est {TempsEcouler2}.")
        # time.sleep(2)
        # self.player.clickPlayStopPlayer()
        # TempsEcoulerFinal = self.player.getTempsEcouler()
        # print(f"le clip est arreté à {TempsEcoulerFinal}.")
        # self.player.clickRetourAlaNavigation()
        # import pdb; pdb.set_trace()
