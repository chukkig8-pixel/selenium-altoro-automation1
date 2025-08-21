from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch Chrome browser
driver = webdriver.Chrome()
driver.maximize_window()

# 1. Open target site
driver.get("http://demo.testfire.net/")
time.sleep(5)

# 2. Navigate to "Sign In"
driver.find_element(By.LINK_TEXT, "Sign In").click()
time.sleep(5)

# 3. Enter random username and password
driver.find_element(By.ID, "uid").send_keys("admin")
driver.find_element(By.ID, "passw").send_keys("admin")

# Click Login
driver.find_element(By.NAME, "btnSubmit").click()
time.sleep(5)

# 4. Crawl around 5 more pages
links_to_visit = [
    "View Account Summary",
    "Transfer Funds",
    "View Recent Transactions",
    "My Profile",
    "Contact Us"
]

for link in links_to_visit:
    try:
        driver.find_element(By.LINK_TEXT, link).click()
        print(f"Visited page: {link}")
        time.sleep(5)
    except Exception as e:
        print(f"Could not visit {link}: {e}")

# Done – close browser
driver.quit()
