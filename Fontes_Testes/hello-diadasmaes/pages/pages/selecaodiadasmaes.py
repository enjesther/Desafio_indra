class DiaMaes:
    def __init__(self, driver):
        self.URL='https://www.americanas.com.br/'
        self.driver = driver

    def go_home(self):
        self.driver.get(self.URL)

    def menu_maes(self):
        self.driver.find_element_by_xpath('//*[@id="list-level-1"]/li[3]/a').click()

    def categoria_moda(self):
        self.driver.find_element_by_xpath('//*[@id="main-top"]/div[3]/div/div/div/div[2]/div[2]/div/div/a/div/div/picture/img').click()

    def moda_praia(self):
        self.driver.find_element_by_xpath('//*[@id="content-top"]/div[2]/div/div/div/div[1]/div/div[3]/div/div/a/div/div/picture/img').click()

    def seleciona_produto(self):
        self.driver.find_element_by_xpath('//*[@id="content-middle"]/div[3]/div/div/div/div[1]/div[17]/div').click()

    def verificacao(self):
        assert self.driver.find_element_by_xpath('//*[@id="content"]/div/div/section/div/div[2]/div[2]/section[1]/div[1]')