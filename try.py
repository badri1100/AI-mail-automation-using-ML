from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Function to send messages using Selenium
def send_whatsapp_message(phone_number, message):
    # Initialize Chrome WebDriver with explicit path to chromedriver
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--headless")  # Optional: Run in headless mode (without opening browser window)
    driver = webdriver.Chrome(options=options)

    # Open WhatsApp Web
    driver.get("https://web.whatsapp.com/")
    
    # Wait for 20 seconds to give time for the user to log in
    time.sleep(20)

    # Locate the search box and enter the recipient's phone number
    search_box = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="3"]')
    search_box.send_keys(phone_number)
    time.sleep(2)

    # Select the first search result (assuming it's the correct contact)
    first_result = driver.find_element_by_xpath('//span[@title="{}"]'.format(phone_number))
    first_result.click()
    time.sleep(2)

    # Locate the message input box and send the message
    message_box = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="1"]')
    message_box.send_keys(message)
    time.sleep(1)
    message_box.send_keys(Keys.ENTER)

    # Close the browser window
    driver.quit()

# Example usage
phone_numbers = ["+91 6361723454", "+91 9481914005"]  # Add recipient phone numbers here
message = "Hello! This is a test message sent using Python and Selenium."

for number in phone_numbers:
    send_whatsapp_message(number, message)
