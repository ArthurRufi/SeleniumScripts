#recaptular alguns conceitos e tecnicas do selenium com python

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



# isso vai inicializar o navegador
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

#isso vai abrir o site
driver.get("https://www.google.com")

#fazendo pesquisa
search_box = driver.find_element(by=By.NAME, value="q")
search_box.send_keys("Asimov Academy")
search_box.submit()

driver.quit()