#!/bin/bash
python -m py.test --alluredir=Reports/my_allure_report /Users/abdi.bileh17/Documents/Selenium/Projet_test_v0/TestCases/test_homePage_chaines.py 
sleep 3
python -m py.test --alluredir=Reports/my_allure_report /Users/abdi.bileh17/Documents/Selenium/Projet_test_v0/TestCases/test_modif_profil.py 
sleep 3
python -m py.test --alluredir=Reports/my_allure_report /Users/abdi.bileh17/Documents/Selenium/Projet_test_v0/TestCases/test_homePage_chaines.py c
sleep 3
allure serve Reports/my_allure_report   

