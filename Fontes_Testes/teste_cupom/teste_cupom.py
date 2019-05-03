from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

browser = webdriver.Chrome()

browser.get('https://www.americanas.com.br/')
element = browser.find_element_by_id('btn-expanded')
element.click()
time.sleep(2)
element = browser.find_element_by_xpath('//*[@id="list-level-2"]/li[13]/a')
element.click()
email = browser.find_element_by_id('email')
email.send_keys('a@gmail.com')
email2 = browser.find_element_by_id('mgmEmail')
email2.send_keys('a222@gmail.com')
botao = browser.find_element_by_xpath('//*[@id="main-top"]/div[3]/div/div/form/div/div[2]/div/div[3]/button/div')
botao.click()