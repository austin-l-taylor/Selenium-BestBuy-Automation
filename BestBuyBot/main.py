from turtle import goto
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

PATH = "/Users/austintaylor/Documents/ProjectsFolder/Python Projects/BestBuyBot/chromedriver"
driver = webdriver.Chrome(PATH)

# input URL into the bot
website = input(
    "copy and past the full URL of the exact item you want into the bot")
driver.get(website)

# checks if the items is in stock
addtocart = driver.find_element(
    By.CLASS_NAME, "fulfillment-add-to-cart-button")
addtocart.click()
