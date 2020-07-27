from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import selenium as sel
import pandas as pd
import matplotlib as mlt
print("Program started")
# load dataset
dataset = pd.read_csv("/Users/vikasnagare/Desktop/final_dataset.csv")
a = dataset.iloc[1:1]

browser = webdriver.Chrome()
browser.get("/Users/vikasnagare/Desktop/cromed/chromedriver")

driver.navigate().to("http://www.instagram.com/")
