from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# Open website
driver.get("https://vinothqaacademy.com/demo-site/")
driver.maximize_window()

time.sleep(3)

print("Web form opened")

# --------------------------------
# FIRST NAME
# --------------------------------
FirstName = driver.find_element(By.NAME, "vfb-5")
FirstName.send_keys("Ramya")

# --------------------------------
# LAST NAME
# --------------------------------
LastName = driver.find_element(By.NAME, "vfb-7")
LastName.send_keys("R")

# --------------------------------
# RADIO BUTTON
# --------------------------------
female = driver.find_element(By.ID, "vfb-31-2")

if not female.is_selected():
    female.click()

# --------------------------------
# CHECKBOXES
# --------------------------------
for i in [0, 3]:

    print("Checking checkbox:", i)

    checkbox = driver.find_element(
        By.ID,
        f"vfb-20-{i}"
    )

    print("Checkbox found:", i)

    if not checkbox.is_selected():
        checkbox.click()

print("Checkboxes completed")

print("All fields completed")

input("Press Enter to close the browser...")

driver.quit()