import time
class DiaMaes:
    def __init__(self, driver):
        self.URL='https://www.americanas.com.br/'
        self.driver = driver

    def go_home(self):
        self.driver.get(self.URL)

    def entrar_menu(self):
        self.driver.find_element_by_xpath('//*[@id="list-level-1"]/li[3]/a').click()
        time.sleep(5)
        self.driver.find_element_by_xphat('//*[@id="main-top"]/div[4]/div/div/div/div[2]/div[2]').click()
        time.sleep(5)
        self.driver.find_element_by_xpath('//*[@id="content-top"]/div[2]/div/div/div/div[1]/div/div[3]').click()
        
    def seleciona_produto(self):
        self.driver.find_element_by_xpath('//*[@id="content-middle"]/div[4]/div/div/div/div[1]/div[1]/div/div[2]/a/section/div[1]/div/div/picture/img').click()

    def verificacao(self):
        assert self.driver.find_element_by_xpath('//*[@id="content"]/div/div/section/div/div[2]/div[2]/section[1]/div[1]')