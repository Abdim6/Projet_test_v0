"""
Objectif : tester la redirection vers de la page homePage de différentes chaines - hors connexion
Date de la dernière grosse maj : 23/03/2022
Owner : Abdi
"""
from PageObjects.HomePage import HomePage
from Utilities.readProperties import ReadTitlePage
from Utilities.customLogger import LogGen
import time


# Ce scénario vérifie si les home pages de différentes chaines se sont bien affichées
# Le test s'effectue au niveau de titre de la page - User n'est pas connecté  
class Test_003_HomePage:
    
    logger = LogGen.loggen()

    def test_homePageTitle(self,setup_SansConnexionUser):
        self.logger.info("***************** DEBUT - Test_003_HomePage ****************")
        self.driver = setup_SansConnexionUser
        time.sleep(2)

        # Création d'un objet HomePage pour pouvoir se service ses méthodes (actions sur des éléments de la home page)
        self.hp = HomePage(self.driver)
        self.hp.clickBtnListeChaines()
        time.sleep(2)
        chaines = self.hp.listeChaines() #On récupère la liste des chaines 
        nb_chaine = len(chaines)
        
        print("Le nb de chaines est :",nb_chaine)
        self.tabTitles = [ReadTitlePage.getTitleM6(), ReadTitlePage.getTitleW9(), 
                          ReadTitlePage.getTitle6ter(),ReadTitlePage.getTitleguilli(), 
                          ReadTitlePage.getTitleparis_premiere(),ReadTitlePage.getTitleteva(),
                          ReadTitlePage.getTitleLelive()]
        self.nomChaines = ["M6","W9","6ter","Guilli","Paris Prémière","Teva","Chaine Live"]
        for nb in range(nb_chaine):
            # actions = ActionChains(self.driver)
            # actions.move_to_element(chaines[nb])
            # actions.perform()
            # time.sleep(3)
            self.hp.clickChaineBtn(nb)
            # chaines[nb].click()
            time.sleep(2)
            ####
            act_title = self.driver.title
            time.sleep(2)
            #la vérification du titre de la page home page de la chaine se fait ICI
            assert act_title == self.tabTitles[nb], self.logger.error("***************** Test titre de la page - KO ****************")
            
            self.logger.info(f"***************** Test titre de la page {self.nomChaines[nb]} - OK ****************") 
            # le nom de la chaine sera variabiliser dans un tuple 
            # "L'idée serait de renvoyer deux valeurs dans le readpropreties, le titre et le nom de la chaine et puis le recupérer dans le LOg le nom de la chaine"
            
            time.sleep(2)
            self.driver.back()
            if nb == nb_chaine-1 : #Lorsqu'on atteint la dernière chaine, on sort de la boucle
                break
            self.hp.clickBtnListeChaines()
            # chaines = self.hp.listeChaines()
        time.sleep(5)
        self.logger.info("***************** FIN - Test_003_homePage_content ****************")
       