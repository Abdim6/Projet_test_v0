#!/bin/bash
pytest --alluredir=Reports/my_allure_report /Users/abdi.bileh17/Documents/Selenium/Projet_test_v0/TestCases/test_homePage_chaines.py 
sleep 3
pytest --alluredir=Reports/my_allure_report /Users/abdi.bileh17/Documents/Selenium/Projet_test_v0/TestCases/test_modif_profil.py 
sleep 3
pytest --alluredir=Reports/my_allure_report /Users/abdi.bileh17/Documents/Selenium/Projet_test_v0/TestCases/test_IDenBoucle.py
sleep 3
allure serve Reports/my_allure_report   

# "commande avec allure"
# pytest --alluredir TestCases/test_modif_profil.py
# python -m pytest --alluredir=Reports/my_allure_report /Users/abdi.bileh17/Documents/Selenium/Projet_test_v0/TestCases/test_IDenBoucle.py
# s