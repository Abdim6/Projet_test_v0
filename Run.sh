#!/bin/bash
python -m py.test --alluredir=Reports/my_allure_report_sh /Users/abdi.bileh17/Documents/Selenium/Projet_test_v0/TestCases/test_homePage_chaines.py 
sleep 3
allure serve Reports/my_allure_report_sh    