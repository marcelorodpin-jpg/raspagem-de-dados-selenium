# autor: Marcelo
# Projeto: Raspagem de dados com Python 

''' 
1- onde está o item desejado?
 https://www.amazon.com.br/Smartphone-Samsung-Galaxy-C%C3%A2mera-Recursos/dp/B0DYVPCX34/ref=sr_1_5

2-qual o detalhe do item que eu desejo?
preço!
a-price-whole
a-price-fraction

3-capturar a informação do item desejado

'''
# Importando a biblioteca Selenium

# pip install selenium
# pip install webdriver-manager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
# driver do navegador
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))



# determinar a url do site
url = "https://www.amazon.com.br/gp/aw/d/B0GVT89H5W"
# get
driver.get(url)
time.sleep(5)
# Aguarda 5 segundos para o carregamento da página


# Mostrar od dados capturados

interiro = driver.find_element(By.CLASS_NAME, "a-price-whole").text
fracao = driver.find_element(By.CLASS_NAME, "a-price-fraction").text    

print(f"Preço capturado: R$ {interiro},{fracao}")

# Fechar o navegador
driver.quit()
