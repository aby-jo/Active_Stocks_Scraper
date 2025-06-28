from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_field_names(driver):
    header = driver.find_element(By.CSS_SELECTOR, "thead tr")
    return header.text.split("\n")

def get_rows(driver):
    return WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "tbody tr"))
    )

def parse_row(row_element):
    raw = row_element.text.split("\n")
    return raw[:-1] + raw[-1].split()

def set_no_of_rows(driver):
    dropdown_clicker=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button.menuBtn.tertiary-btn")))
    dropdown_clicker.click()

    row_100=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//div[@role='option' and @data-value='100']")))
    row_100.click()
