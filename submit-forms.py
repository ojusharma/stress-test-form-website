from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import random

def submit_form():
    """Submit the contact form on ribhav.live using Selenium"""
    url = "https://www.ribhav.live/"
    
    try:
        chrome_options = Options()
        chrome_options.add_argument('--headless') 
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        
        # Initialize the driver
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)
        wait = WebDriverWait(driver, 10)
        
        try:
            name_input = wait.until(EC.presence_of_element_located((By.NAME, 'name')))
        except:
            try:
                name_input = driver.find_element(By.CSS_SELECTOR, 'input[placeholder*="Name" i]')
            except:
                name_input = driver.find_element(By.XPATH, '//input[contains(@placeholder, "name") or contains(@placeholder, "Name")]')
        
        try:
            email_input = driver.find_element(By.NAME, 'email')
        except:
            try:
                email_input = driver.find_element(By.CSS_SELECTOR, 'input[type="email"]')
            except:
                email_input = driver.find_element(By.XPATH, '//input[contains(@placeholder, "email") or contains(@placeholder, "Email")]')
        
        try:
            message_input = driver.find_element(By.NAME, 'message')
        except:
            try:
                message_input = driver.find_element(By.TAG_NAME, 'textarea')
            except:
                message_input = driver.find_element(By.XPATH, '//textarea[contains(@placeholder, "message") or contains(@placeholder, "Message")]')
        
        # Fill in the form
        name_input.clear()
        name_input.send_keys('Stress Testing')
        
        email_input.clear()
        email_input.send_keys('example@example.com')
        
        message_input.clear()
        message_input.send_keys('This is a stress test message.')
        
        # Find and click submit button
        try:
            submit_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        except:
            try:
                submit_button = driver.find_element(By.XPATH, '//button[contains(text(), "Send") or contains(text(), "Submit")]')
            except:
                submit_button = driver.find_element(By.TAG_NAME, 'button')
        
        submit_button.click()
        
        # Wait a bit for submission
        time.sleep(2)
        
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] ✓ Form submitted successfully!")
        driver.quit()
        return True
            
    except Exception as e:
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Error: {str(e)}")
        try:
            driver.quit()
        except:
            pass
        return False

def main():
    print("Starting form submission bot...")
    print("Submitting form. Ctrl+C to stop.")    
    try:
        while True:
            submit_form()
            time.sleep(10)
    except KeyboardInterrupt:
        print("Stopped by user.")

if __name__ == "__main__":
    main()
