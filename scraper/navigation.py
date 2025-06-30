from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def go_to_next_page(driver, prev_first_row):
    try:
        WebDriverWait(driver,120).until(EC.presence_of_element_located((By.XPATH, "//button[@data-testid='next-page-button']")))
        next_btn = WebDriverWait(driver, 120).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='next-page-button']"))
        )
        next_btn.click()
        # Wait until the previously passed row element becomes stale (i.e., the DOM changes)
        WebDriverWait(driver,120).until(lambda d : d.find_element(By.CSS_SELECTOR,"tbody tr").text!=prev_first_row)
        return True
    except:
        return False
