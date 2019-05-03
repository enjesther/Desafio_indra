class Pesquisa:
    
    def __init__(self,driver):
        self.URL='https://www.americanas.com.br/'
        self.driver = driver

    def go_home(self):
        self.driver.get(self.URL)
    
    def fazer_pesquisa(self, value):
        self.driver.implicitly_wait(10)
        element1 = self.driver.find_element_by_xpath('//*[@id="h_search-input"]')
        element1.send_keys(value)
        element1.submit()
    
    def selecionar_produto(self):
        element2 = self.driver.find_element_by_xpath('//*[@id="content-middle"]/div[5]/div/div/div/div[1]/div[9]/div')
        element2.click()
        assert self.driver.find_element_by_xpath('//*[@id="product-name-default"]')
    
    def produto_no_carrinho(self):
        element3 = self.driver.find_element_by_xpath('//*[@id="btn-buy"]')
        element3.click()
    
    def sem_seguro(self):
        self.driver.find_element_by_xpath('//*[@id="btn-continue"]').click()

    def validacao(self):
        assert self.driver.find_element_by_xpath('//*[@id="app"]/section/section/div[1]/div[1]/section/ul/li/div[2]/div[1]/h2/a')