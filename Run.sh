#!/bin/bash
pytest --alluredir=Reports/my_allure_report /Users/abdi.bileh17/Documents/Selenium/Projet_test_v0/TestCases/test_001_Connexion.py --capture=tee-sys
sleep 3
pytest --alluredir=Reports/my_allure_report /Users/abdi.bileh17/Documents/Selenium/Projet_test_v0/TestCases/test_002_ModifierDonneesUser.py --capture=tee-sys
sleep 3
pytest --alluredir=Reports/my_allure_report /Users/abdi.bileh17/Documents/Selenium/Projet_test_v0/TestCases/test_003_HomePage.py --capture=tee-sys
sleep 3

#allure serve Reports/my_allure_report   

# "commande avec allure"
# pytest --alluredir TestCases/test_modif_profil.py
# python -m pytest --alluredir=Reports/my_allure_report /Users/abdi.bileh17/Documents/Selenium/Projet_test_v0/TestCases/test_IDenBoucle.py
# s


