#%%

#bibliotecas

from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui as pg

#navegar até o whatsapp

#campo de pesquisa e mensagem - "copyable-text selectable-text"

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://web.whatsapp.com/")
contatos =[""]
mensagem = ""

time.sleep(15)


def buscar_contato(contato):
    campo_pesquisa=driver.find_element_by_xpath("//div[contains(@class,'copyable-text selectable-text')]")
    time.sleep(3)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    try:
        campo_pesquisa.send_keys(Keys.ENTER)
    except:
        pg.press("Enter")

def enviar_mensagem (mensagem):
    campo_mensagem=driver.find_elements_by_xpath("//div[contains(@class,'copyable-text selectable-text')]")
    time.sleep(3)
    campo_mensagem[1].click()
    time.sleep(1)
    campo_mensagem[1].send_keys(mensagem)
    time.sleep(1)
    try:
        campo_mensagem[1].send_keys(Keys.ENTER)
    except:
        pg.press("Enter")
    
    pass


for contato in contatos:
    buscar_contato(contato)
    enviar_mensagem (mensagem)


#definir contatos


# %%
