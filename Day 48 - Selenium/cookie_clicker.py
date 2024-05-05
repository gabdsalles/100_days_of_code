from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

GAME_URL = "https://orteil.dashnet.org/experiments/cookie/"

driver = webdriver.Chrome()

timeout = time.time() + 5
cinco_min = time.time() + 60*5

driver.get(GAME_URL)

cookie = driver.find_element(By.ID, value="cookie")

items = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
item_ids = [item.get_attribute("id") for item in items]

def checar_upgrades():
    dinheiro = driver.find_element(By.ID, value='money')
    dinheiro = int(dinheiro.text)
    print(f"Tenho {dinheiro} cookies.")

    # Get all upgrade <b> tags
    all_prices = driver.find_elements(by=By.CSS_SELECTOR, value="#store b")
    item_prices = []

    # Convert <b> text into an integer price.
    for price in all_prices:
        element_text = price.text
        if element_text != "":
            cost = int(element_text.split("-")[1].strip().replace(",", ""))
            item_prices.append(cost)

    cookie_upgrades = {}
    for n in range(len(item_prices)):
        cookie_upgrades[item_prices[n]] = item_ids[n]

    upgrades_compraveis = {}
    
    for custo, id in cookie_upgrades.items():
        if dinheiro > custo:
            upgrades_compraveis[custo] = id
    
    upgrade_mais_caro = max(upgrades_compraveis)
    print(upgrade_mais_caro)
    to_purchase_id = upgrades_compraveis[upgrade_mais_caro]

    driver.find_element(by=By.ID, value=to_purchase_id).click()
    

while True:
    cookie.click()
    if time.time() > timeout:
        #print("Passou 5 segundos")
        checar_upgrades()
        timeout = time.time() + 5

    if time.time() > cinco_min:
        cookie_per_s = driver.find_element(by=By.ID, value="cps").text
        print(cookie_per_s)
        break
