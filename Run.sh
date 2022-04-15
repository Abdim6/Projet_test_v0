#!/bin/bash
pytest --alluredir=allure-results /Users/abdi.bileh17/Documents/Selenium/Projet_test_v0/TestCases/test_001_Connexion.py --capture=tee-sys
sleep 3
pytest --alluredir=allure-results /Users/abdi.bileh17/Documents/Selenium/Projet_test_v0/TestCases/test_002_ModifierDonneesUser.py --capture=tee-sys
sleep 3
pytest --alluredir=allure-results /Users/abdi.bileh17/Documents/Selenium/Projet_test_v0/TestCases/test_003_HomePage.py --capture=tee-sys
sleep 3




