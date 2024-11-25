from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

class google:
    


    def __init__(self,driver):
        self.driver=driver
        self.timeOut=10
        self.searchBar=(By.ID,'APjFqb')
        self.botonSearch=(By.CLASS_NAME,'gNO89b')
        self.opcionesFiltradas=(By.CLASS_NAME,'Ap1Qsc')

    def goto(self):
         self.driver.get('https://www.google.com/')
         self.findElment(self.searchBar)

    def getTitle(self):
        return self.driver.title

    def findElment(self,locator):
        return WebDriverWait(self.driver,self.timeOut).until(EC.presence_of_element_located(locator))
    
    def click(self,locator):
        self.findElment(locator).click()

    def enter_text(self,locator,texto):
        element=self.findElment(locator)
        element.clear()
        element.send_keys(texto)
        return element
        
    def buscar(self,texto):
        self.enter_text(self.searchBar,texto).submit()
       
    def consulta_realizada(self):
        return self.findElment(self.opcionesFiltradas)

        
    