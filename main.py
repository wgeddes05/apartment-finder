import re
import time
import plotly
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from matplotlib import pyplot as plt
from twilio.rest import Client
from bs4 import BeautifulSoup
import seaborn as sns
import pandas as pd


service = Service(
    r"C:\Users\wgedd\Documents\GitHub\apartment-finder\chromedriver-win64\chromedriver.exe"
)
driver = webdriver.Chrome(service=service)

url = "https://www.zillow.com/homes/for_rent/"
driver.get(url)  # Open Zillow website
driver.implicitly_wait(5)  # Allow time for the page to load fully

data = []
listings = driver.find_elements(By.CLASS_NAME, "list-card-info")

for listing in listings:
    title = listing.find_element(By.CLASS_NAME, "list-card-addr").text
    price = listing.find_element(By.CLASS_NAME, "list-card-price").text
    details = listing.find_element(By.CLASS_NAME, "list-card-details").text
    link = listing.find_element(By.TAG_NAME, "a").get_attribute("href")

    # print(f"Title:  {title}, Price:  {price}, Details:  {details}, Link:  {link}")
    data.append([title, price, details, link])

driver.quit()  # Close the browser

df = pd.DataFrame(data, columns=["Title", "Price", "Details", "Link"])
df.to_csv("Zillow_listings.csv", index=False)
