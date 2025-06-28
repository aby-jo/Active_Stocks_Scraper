from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import tempfile
def create_browser(headless=True):
    options = webdriver.ChromeOptions()
    # Headless browser setting
    if headless:
        options.add_argument("--headless=new")  # Use the modern headless mode
    
    # Prevent profile conflict
    user_data_dir = tempfile.mkdtemp()  # Create a temp profile for Chrome
    options.add_argument(f"--user-data-dir={user_data_dir}")

    # Other common flags to improve compatibility and performance
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver