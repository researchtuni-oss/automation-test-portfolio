from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time

# If geckodriver is on PATH, you can just do webdriver.Firefox()
driver = webdriver.Firefox()

try:
    driver.get("https://www.google.com")
    print("Title is:", driver.title)

    # keep browser open 5 seconds so you see it
    time.sleep(5)
finally:
    driver.quit()
