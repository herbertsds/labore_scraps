# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 03:30:29 2020

@author: henrique
"""

import os
from bs4 import BeautifulSoup
import pandas as pd
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def login(driver,email,password):
    driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")
    input_email = driver.find_element_by_id("username")
    input_email.click()
    input_email.send_keys(email)

    input_pass = driver.find_element_by_id("password")
    input_pass.click()
    input_pass.send_keys(password)

    div_login = driver.find_element_by_class_name("login__form_action_container")
    button_login = div_login.find_element_by_tag_name("button")
    button_login.click()

path = "/home/henrique/Documents/scraps/labore_scrap/"

SELENIUM_PATH = "/home/henrique/Documents/selenium/geckodriver"
CSV_FILENAME = "sample.csv"
CSV_FILENAME_COMPLETE = "complete.json"


if not os.path.exists(path+'htmls'):
    os.makedirs(path+'htmls')




