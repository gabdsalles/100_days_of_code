from selenium import webdriver
from selenium.webdriver.common.by import By

PYTHON_URL = "https://www.python.org"

driver = webdriver.Chrome()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver.get(PYTHON_URL)

datas = driver.find_elements(By.CSS_SELECTOR, value='.event-widget time')
# for data in datas:
#     print(data.text)

nomes = driver.find_elements(By.CSS_SELECTOR, value='.event-widget li a')
# for nome in nomes:
#     print(nome.text)

dicionario = {i: {'data': datas[i].text, 'nome': nomes[i].text} for i in range(5)}

print(dicionario)

driver.quit()