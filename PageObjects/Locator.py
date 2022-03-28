"""
Objectif : Liste tous les objets de l'application pour les localiser dans les différentes pages
Date de la dernière grosse maj : 23/03/2022
Owner : Abdi
"""
from selenium.webdriver.common.by import By

class Locators():
    #--- Page Home Page ---
    # moncompte_btn = (By.CSS_SELECTOR, "---")
    moncompte_btn_CSS = (By.CSS_SELECTOR,"#__brk > div > div.n913wo-5.cuyMWW > div.n913wo-4.fCmDdf > div > header > div > div > nav > div.m4392j-1.imWKGD > ul > li:nth-child(5) > button")
    Chaines_btn_Class =(By.CLASS_NAME,"")
    recherche_btn_CSS = (By.CSS_SELECTOR,"#__brk > div > div.n913wo-5.cuyMWW > div.n913wo-4.fCmDdf > div > header > div > div > nav > div.m4392j-1.imWKGD > ul > li:nth-child(4) > a")
    consent_accepter_Class = (By.CLASS_NAME,"sc-1esye45-2.dVskuE.sc-1p0v3oj-0")
    accepter_btnTCF_CSS = (By.CSS_SELECTOR,"body > div:nth-child(12) > aside > div > div.suptlw-3.dTtZno > form > div.s9pqpz-4.eGAKcX.sc-18bqyzn-0.gXHDvG > div > button.sc-1esye45-2.dVskuE.sc-1veuio6-0.dktssj.s9pqpz-2.hEklsz.is-primary > span")
    HomeBtn_CSS = (By.CSS_SELECTOR,"#__brk > div > div.n913wo-5.cuyMWW > div.n913wo-4.fCmDdf > div > header > div > div > nav > div.m4392j-1.imWKGD > ul > li:nth-child(3)")
    btnListe_chaines_Class = (By.CLASS_NAME,"sc-1ajxxj-0.sc-1c6u83a-3.iUrMAG")
    liste_chaines_class = (By.CLASS_NAME,"b8xld8-1")
    objetHomePage_CSS = (By.CSS_SELECTOR,"#main > div > section:nth-child(3) > div.y84eg7-0.sc-8pi7if-0.LuxLU > h1")
    moncompte_btn_xml = (By.XPATH,'//*[@id="__brk"]/div/div[2]/div[2]/div/header/div/div/nav/div[1]/ul/li[5]/button')
    mesinfo_btn = (By.CSS_SELECTOR,"#__brk > div > div.n913wo-5.cuyMWW > div.n913wo-4.fCmDdf > div > main > aside > nav > ul > li:nth-child(3) > a > span")
    mesinfo_btn_xml = (By.XPATH,'//*[@id="__brk"]/div/div[2]/div[2]/div/main/aside/nav/ul/li[3]/a')
    donneesperso_email = (By.ID,"email")
    AjoutFavoris_btn_CSS = (By.CSS_SELECTOR,"#page_62209efac81c31\.51376685--4f8b12bd-ed93-4057-80fa-211a289dc3a4 > div.qd8avx-0.jwKxkB > div.nei5bm-2.cNRBFu > div.nei5bm-9.fEDJNC > button")
    AjoutFavoris_btn_Class = (By.CLASS_NAME,"oxwymj-0.jtrbaw.sc-1qpa8kx-4.eOyIfE.is-secondary.is-responsive")
    AjoutFavoris_btn_Class_2 = (By.CLASS_NAME,"f1uzip-0.hUbPBT")
    AjoutFavoris_btn_Xpath = (By.XPATH,'//*[@id="page_6230ac5c387d43.50469081--6a469067-d4c3-4e3f-a32f-46167d79122d"]/div[2]/div[2]/div[1]/button')

    #--- Page Mon Compte ---
    btn_gererInfos_CSS = (By.CSS_SELECTOR,"#__brk > div > div.n913wo-5.cuyMWW > div.n913wo-4.fCmDdf > div > main > div > div.r1if2e-1.bqqlfm.sc-1eq6ctx-0.kabTKW > div:nth-child(1) > article > div.gvmwfe-0.o6a45d-0.kfijhj > a")
    btn_modifier_CSS = (By.CSS_SELECTOR,"#__brk > div > div.n913wo-5.cuyMWW > div.n913wo-4.fCmDdf > div > main > div > div.r1if2e-1.bqqlfm.sc-1eq6ctx-0.kabTKW > div:nth-child(1) > article > div > div.gvmwfe-0.o6a45d-0.kfijhj > button")
    textbox_firstname_id = (By.ID,"firstName")
    textbox_lastname_id = (By.ID,"lastName")
    btn_valider_CSS = (By.CSS_SELECTOR,"#__brk > div > div.n913wo-5.cuyMWW > div.n913wo-4.fCmDdf > div > main > div > div.r1if2e-1.bqqlfm.sc-1eq6ctx-0.kabTKW > div:nth-child(1) > article > form > div.gvmwfe-0.o6a45d-0.kfijhj > button.sc-1esye45-2.bTcnKU.o6a45d-1.hCltVO.is-primary")
    btn_deconnexion_CSS = (By.CSS_SELECTOR,"#__brk > div > div.n913wo-5.cuyMWW > div.n913wo-4.fCmDdf > div > main > aside > button > span")
    btn_deconnexion_Xpath = (By.XPATH,'/html/body/div[2]/div/div[2]/div[2]/div/main/aside/button')
    #--- Page Recherche ---
    dernierReplay_CSS = (By.CSS_SELECTOR,"#page_62209fc7e252e0\.25802620--4443f32c-c6ee-4b72-86e1-8fbeb2625bc8 > div.sc-1jzygab-5.fNJpJi > ul > li:nth-child(1)")
    listReplay_CSS = (By.CSS_SELECTOR,"#page_62232bab6c0893\.70856363--4443f32c-c6ee-4b72-86e1-8fbeb2625bc8 > div.sc-1jzygab-5.fNJpJi > ul")
    section_replay_class = (By.CLASS_NAME,"sc-1jzygab-5")
    dernierReplay_XPATH = (By.XPATH,'//*[@id="page_622321a29b68f1.45716632--4443f32c-c6ee-4b72-86e1-8fbeb2625bc8"]/div[1]/ul/li[1]/a/article')
    liste_dernierReplay_Class = (By.CLASS_NAME,"sc-1jzygab-7")

    #--- Page Onboarding ---
    textbox_username_id = (By.ID,"email")
    textbox_password_id = (By.ID,"password")

    # button_login_CSS_Selector = 'body > div:nth-child(9) > div > div > div > div > div.izd9z0-4.jQonvK > form > button > span > span > span'
    button_login_xml = (By.XPATH,"/html/body/div[3]/div/div/div/div/div[2]/form/button")
    button_inscription = (By.CLASS_NAME,"body > div:nth-child(9) > div > div > div > div > div.izd9z0-5.jhrtwX > div > a")
    button_inscription_new = (By.CSS_SELECTOR,"body > div:nth-child(9) > div > div > div > div > div.izd9z0-5.jhrtwX > div > a")
    email_inscription =(By.ID,"email")
    pwd_inscription =(By.ID,"password")
    button_inscrire_new = (By.CSS_SELECTOR,"body > div:nth-child(9) > div > div > div > div > div.izd9z0-4.jQonvK > div.sc-1skm6pc-0.kosLNi.kqtu9n-2.hsHvHs > form > div.sc-1skm6pc-1.dkVizr > button")
    liste_genre = (By.ID,"gender")
    section_age = (By.ID,"birthdate")
    button_terminer = (By.CSS_SELECTOR,"body > div:nth-child(9) > div > div > div > div > div.izd9z0-4.jQonvK > div > form > div.sc-1skm6pc-1.dkVizr > button")
