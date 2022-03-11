from selenium.webdriver.common.by import By

class Locators():
    #--- Page Home Page ---
    moncompte_btn_CSS = "#__brk > div > div.n913wo-5.cuyMWW > div.n913wo-4.fCmDdf > div > header > div > div > nav > div.m4392j-1.imWKGD > ul > li:nth-child(5) > button"
    accepter_btnTCF_CSS = "body > div:nth-child(12) > aside > div > div.suptlw-3.dTtZno > form > div.s9pqpz-4.eGAKcX.sc-18bqyzn-0.gXHDvG > div > button.sc-1esye45-2.dVskuE.sc-1veuio6-0.dktssj.s9pqpz-2.hEklsz.is-primary > span"
    HomeBtn_CSS = "#__brk > div > div.n913wo-5.cuyMWW > div.n913wo-4.fCmDdf > div > header > div > div > nav > div.m4392j-1.imWKGD > ul > li:nth-child(3)"
    objetHomePage_CSS = "#main > div > section:nth-child(3) > div.y84eg7-0.sc-8pi7if-0.LuxLU > h1"
    recherche_btn_CSS = "#__brk > div > div.n913wo-5.cuyMWW > div.n913wo-4.fCmDdf > div > header > div > div > nav > div.m4392j-1.imWKGD > ul > li:nth-child(4) > a"
    button_txt = "#__brk > div > div.n913wo-5.cuyMWW > div.n913wo-4.fCmDdf > div > main > aside > button > span"
    moncompte_btn_xml = '//*[@id="__brk"]/div/div[2]/div[2]/div/header/div/div/nav/div[1]/ul/li[5]/button'
    mesinfo_btn = "#__brk > div > div.n913wo-5.cuyMWW > div.n913wo-4.fCmDdf > div > main > aside > nav > ul > li:nth-child(3) > a > span"
    mesinfo_btn_xml = '//*[@id="__brk"]/div/div[2]/div[2]/div/main/aside/nav/ul/li[3]/a'
    donneesperso_email = "email"
    AjoutFavoris_btn_CSS = "#page_62209efac81c31\.51376685--4f8b12bd-ed93-4057-80fa-211a289dc3a4 > div.qd8avx-0.jwKxkB > div.nei5bm-2.cNRBFu > div.nei5bm-9.fEDJNC > button"

    #--- Page Mon Compte ---
    btn_gererInfos_CSS = "#__brk > div > div.n913wo-5.cuyMWW > div.n913wo-4.fCmDdf > div > main > div > div.r1if2e-1.bqqlfm.sc-1eq6ctx-0.kabTKW > div:nth-child(1) > article > div.gvmwfe-0.o6a45d-0.kfijhj > a"
    btn_modifier_CSS = "#__brk > div > div.n913wo-5.cuyMWW > div.n913wo-4.fCmDdf > div > main > div > div.r1if2e-1.bqqlfm.sc-1eq6ctx-0.kabTKW > div:nth-child(1) > article > div > div.gvmwfe-0.o6a45d-0.kfijhj > button"
    textbox_firstname_id = "firstName"
    textbox_lastname_id = "lastName"
    btn_valider_CSS = "#__brk > div > div.n913wo-5.cuyMWW > div.n913wo-4.fCmDdf > div > main > div > div.r1if2e-1.bqqlfm.sc-1eq6ctx-0.kabTKW > div:nth-child(1) > article > form > div.gvmwfe-0.o6a45d-0.kfijhj > button.sc-1esye45-2.bTcnKU.o6a45d-1.hCltVO.is-primary"
    
    #--- Page Recherche ---
    dernierReplay_CSS = "#page_62209fc7e252e0\.25802620--4443f32c-c6ee-4b72-86e1-8fbeb2625bc8 > div.sc-1jzygab-5.fNJpJi > ul > li:nth-child(1)"
    listReplay_CSS ="#page_62232bab6c0893\.70856363--4443f32c-c6ee-4b72-86e1-8fbeb2625bc8 > div.sc-1jzygab-5.fNJpJi > ul"
    section_replay_class = "sc-1jzygab-5"
    dernierReplay_XPATH = '//*[@id="page_622321a29b68f1.45716632--4443f32c-c6ee-4b72-86e1-8fbeb2625bc8"]/div[1]/ul/li[1]/a/article'
    
    #--- Page Onboarding ---
    textbox_username_id = "email"
    textbox_password_id = "password"
    # button_login_CSS_Selector = 'body > div:nth-child(9) > div > div > div > div > div.izd9z0-4.jQonvK > form > button > span > span > span'
    button_login_xml = "/html/body/div[3]/div/div/div/div/div[2]/form/button"
    button_inscription = "body > div:nth-child(9) > div > div > div > div > div.izd9z0-5.jhrtwX > div > a"
    email_inscription ="email"
    pwd_inscription ="password"
    button_inscrire_new = "body > div:nth-child(9) > div > div > div > div > div.izd9z0-4.jQonvK > div.sc-1skm6pc-0.kosLNi.kqtu9n-2.hsHvHs > form > div.sc-1skm6pc-1.dkVizr > button"
    liste_genre = "gender"
    section_age = "birthdate"
    button_terminer = "body > div:nth-child(9) > div > div > div > div > div.izd9z0-4.jQonvK > div > form > div.sc-1skm6pc-1.dkVizr > button"
