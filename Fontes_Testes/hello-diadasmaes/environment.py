from Pyautomators.contrib.scenario_autoretry import scenario_retry
from pages.pages.selecaodiadasmaes import DiaMaes

from selenium import webdriver

def before_all(context):
        context.driver=webdriver.Chrome('driver/chromedriver.exe')
        context.maes = DiaMaes(context.driver)

def after_all(context):
        context.driver.quit()




"""
from Pyautomators.contrib.scenario_autoretry import scenario_retry
def before_all(context):
	pass

def before_feature(context,feature):
	pass

def before_scenario(context,scenario):
	pass

def before_tag(context,tag):
	pass

def after_tag(context,tag):
	pass

def before_step(context,step):
	pass

def after_step(context,step):
	pass

def after_scenario(context,scenario):
	pass

def after_feature(context,feature):
	pass

def after_all(context):
	pass

"""