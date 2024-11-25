import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as chromeService
from webdriver_manager.chrome import ChromeDriverManager
from ..pom.googlePom import google

#pytest steps/googleSteps.copy
#pytest --html=report.html

@pytest.fixture(scope="module")
def setUp_driver():
    driver = webdriver.Chrome(service=chromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()

def test_usuario_abre_google(setUp_driver):
    driver = setUp_driver
    google_page = google(driver)
    google_page.goto()
    assert "Google" in google_page.getTitle()
    
@pytest.mark.parametrize("search",["casa","perro"],ids=["buscar casa","buscar perro"])
def test_buscar_google(setUp_driver,search):
    driver=setUp_driver
    google_page = google(driver)
    google_page.goto()
    google_page.buscar(search)
    assert google_page.consulta_realizada,"Consulta realizada, correctamente"
    
