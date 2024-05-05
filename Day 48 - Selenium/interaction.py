from selenium import webdriver
from selenium.webdriver.common.by import By

WIKIPEDIA_URL = "https://pt.wikipedia.org/wiki/Wikipédia:Página_principal"
TEST_URL = "http://secure-retreat-92358.herokuapp.com"

driver = webdriver.Chrome()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver.get(TEST_URL)

first_name = driver.find_element(By.NAME, value='fName')
last_name = driver.find_element(By.NAME, value='lName')
email = driver.find_element(By.NAME, value='email')

first_name.send_keys("gabriel")
last_name.send_keys("salles")
email.send_keys("email@teste.com")

botao = driver.find_element(By.CLASS_NAME, value="btn")
botao.click()

# qtd_artigos_portugues = driver.find_element(By.XPATH, value='//*[@id="mw-content-text"]/div[1]/div[1]/div/div[1]/table/tbody/tr/td[2]/div/p/b[1]')
# # qtd_artigos_portugues = driver.find_element(By.CSS_SELECTOR, value='#article-count a')
# numero = int(qtd_artigos_portugues.text.replace(" ", ""))
# print(numero)

driver.quit()