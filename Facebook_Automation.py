#written by Arun Mathai S.K.
from selenium import webdriver
from getpass import getpass

usrnme = input("ENTER THE USERNAME/EMAIL-ID ")
psswrd = getpass("ENTER THE PASSWORD ")

driver = webdriver.Chrome()

driver.get("https://facebook.com")

username = driver.find_element_by_xpath('  //*[@id="email"]')
username.send_keys(usrnme)

password = driver.find_element_by_xpath('//*[@id="pass"]')
password.send_keys(psswrd)

login_button = driver.find_element_by_xpath('//*[@id="u_0_b"]')
login_button.click()
