import requests
from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly
from twilio.rest import Client
import time


driver = webdriver.Chrome(executable_path="C:\Users\wgedd\Documents\GitHub\apartment-finder\chromedriver-win64\chromedriver.exe")

url = "https://www.zillow.com/homes/for_rent/"
driver.get(url)  # Open Zillow website
time.sleep(5)  # Allow time for the page to load fully

listings = driver.find_elements(By.CLASS_NAME, "list-card-info")

for listing in listings:
    title = listing.find_element(By.CLASS_NAME, "list-card-addr").text
    price = listing.find_element(By.CLASS_NAME, "list-card-price").text
    link = listing.find_element(By.TAG_NAME, 'a').get_attribute('href')

    print(f"Title: {title}, Price: {price}, Link: {link}")

driver.quit()  # Close the browser
