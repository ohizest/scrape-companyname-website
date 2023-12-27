import time
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By

# Set up WebDriver
driver = webdriver.Firefox()
driver.get("https://clutch.co/agencies/design?reviews=10")
driver.maximize_window()
time.sleep(5)

# Check if the "Accept all cookies" popup is present and click if it is
try:
    accept_all_button = driver.find_element(By.XPATH, "//a[@id='CybotCookiebotDialogBodyButtonAccept']")
    accept_all_button.click()
except:
    pass

# Find elements. Ensure all found elements are from same container
company_names = driver.find_elements(By.XPATH, "//h3/a")
company_websites = driver.find_elements(By.XPATH, "//span[contains(text(),'Visit Website')]//parent::a")

# Create a list of dictionaries to store the data
company_dict = []

# Loop through each company element and print information
for i in range(len(company_names)):
    company_info = {
        # Get company name and URL
        "Company Name:": company_names[i].text,
        "Company Website:": company_websites[i].get_attribute('href')
    }
    company_dict.append(company_info)

# Close the WebDriver
driver.quit()

# Create a DataFrame from the list of dictionaries
df = pd.DataFrame(company_dict)

# Export the data to a CSV file
df.to_csv("Company.csv", index=False)

print("Data exported to Company Names and Website.csv")
