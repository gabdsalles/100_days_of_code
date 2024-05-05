from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://www.python.org"

driver = webdriver.Chrome()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver.get(url=url)

# captcha = driver.find_element(By.LINK_TEXT, "Try different image")
# captcha.click()
# price_dollar = driver.find_element(By.CLASS_NAME, value="a-offscreen")
# print(f"The price is {price_dollar.text}")

search_bar = driver.find_element(By.NAME, value="q")
print(search_bar)
print(search_bar.get_attribute("placeholder"))

button = driver.find_element(By.ID, value="submit")
print(button)
print(button.size)

documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
print(documentation_link.text)

bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)

# driver.close() fecha só uma aba
driver.quit() # fecha o browser inteiro

